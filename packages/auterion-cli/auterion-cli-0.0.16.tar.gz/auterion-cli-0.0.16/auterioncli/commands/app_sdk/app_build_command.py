import os
import shutil
import pathlib
import yaml
import tempfile
from auterioncli.commands.command_base import CliCommand
from auterioncli.commands.app_sdk.environment import ensure_docker, ensure_mender_artifact
from auterioncli.commands.app_sdk.slimify import slimify
import subprocess
import re

PLATFORM_ALIAS = {
    'skynode': 'linux/arm64',
    'ainode': 'linux/arm64'
}


def run_command(commands, cwd='.'):
    print(f'> Executing \'{" ".join(commands)}\'')
    result = subprocess.run(commands, cwd=cwd)
    return result.returncode


def error(msg, code=1):
    print(msg)
    exit(code)


class AppBuildCommand(CliCommand):

    @staticmethod
    def help():
        return 'Build Auterion OS app in current directory'

    def needs_device(self, args):
        return False

    def __init__(self, config):
        self._temp_dir = None
        self._config = config
        self._mender_artifact_path = os.path.join(self._config['persistent_dir'], 'mender-artifact')

    def setup_parser(self, parser):
        parser.add_argument('project_dir', help='Location of the project', nargs='?', default='.')
        parser.add_argument('--skip-docker-build', '-s', help='Do not execute docker build step. Just package.')

    def run(self, args):
        ensure_docker()
        ensure_mender_artifact(self._mender_artifact_path)

        self._temp_dir = tempfile.mkdtemp()
        meta = self._load_metadata(args)
        self._compose_from_meta(meta)

        image_path = self._generate_image(args, meta)

        if re.match('^v\d+$', meta['auterion-app-base']):
            v = meta['auterion-app-base']
            base_image_name = 'auterion/app-base:' + meta['auterion-app-base']
            slimify(image_path, base_image_name, self._config['persistent_dir'])
            print('┌──────────────────────────────────────────────────────────────────────────────────────┐')
            print('│                                                                                      │')
            print('│  Your app requires app auterion app-base-%s to be installed on your device.          │' % v)
            print('│                                                                                      │')
            print('│  Get app-base-v0.auterionos from                                                     │')
            print('│  https://github.com/Auterion/app-base/releases/download/%s/app-base-%s.auterionos    │' % (v, v))
            print('│                                                                                      │')
            print('└──────────────────────────────────────────────────────────────────────────────────────┘')

        else:
            print(f'.. {meta["auterion-app-base"]} does not match a valid app-base version. Skipping slimify step.')
        compressed_image = self._compress_image(image_path)

        self._mender_package_app(args, meta, compressed_image)
        shutil.rmtree(self._temp_dir)

    @staticmethod
    def _load_metadata(args):
        project_dir = args.project_dir
        meta_file = os.path.join(project_dir, 'auterion-app.yml')

        if not os.path.exists(meta_file):
            error(f'File \'{meta_file}\' does not exist. App structure invalid. Aborting...')

        with open(meta_file, 'r') as f:
            meta = yaml.safe_load(f)

        if 'app-name' not in meta or 'app-version' not in meta:
            error(f'{meta_file} does not contain app-name or app-version')

        return meta

    def _compose_from_meta(self, meta):
        compose = {
            'version': '3.7',
            **meta['compose']
        }

        for name, service in compose['services'].items():
            if 'image' not in service:
                service['image'] = name + ':' + meta['app-version']
            service['container_name'] = name
            service['platform'] = PLATFORM_ALIAS.get(meta['target-platform'], meta['target-platform'])

        compose_file = os.path.join(self._temp_dir, 'docker-compose.yml')
        with open(compose_file, 'w') as f:
            yaml.dump(compose, f)

    def _generate_image(self, args, meta):
        # Generate build dif
        project_dir = args.project_dir
        build_dir = os.path.join(project_dir, 'build')
        if not os.path.exists(build_dir):
            os.mkdir(build_dir)

        target_file = os.path.join(build_dir, meta['app-name'] + '.tar')
        compose_file = os.path.join(self._temp_dir, 'docker-compose.yml')

        if not args.skip_docker_build:
            # Just export the required images from the local docker
            target_platform = PLATFORM_ALIAS.get(meta['target-platform'], meta['target-platform'])
            run_command(['docker', 'compose', '-f', compose_file, 'build'], cwd=args.project_dir)

            non_built_images = [v['image'] for k, v in meta['compose']['services'].items() if 'build' not in v]
            if len(non_built_images) > 0:
                print(f'Need to pull {len(non_built_images)} images for this build..')
                for image in non_built_images:
                    run_command(['docker', 'pull', '--platform', target_platform, image])

        images = [v['image'] for k, v in meta['compose']['services'].items()]
        print('According to docker-compose, we have the following images:')
        for image in images:
            print(f'- {image}')

        print('Packaging those images...')
        run_command(['docker', 'save'] + images + ['-o', target_file], cwd=project_dir)

        return target_file

    def _compress_image(self, image):
        run_command(['gzip', image])
        p = pathlib.Path(image + '.gz')
        target_name = p.with_suffix('').with_suffix('.image')
        p.rename(target_name)
        return str(target_name)

    def _mender_package_app(self, args, meta, image_file):
        if not os.path.exists(image_file):
            error(f'Image {image_file} does not exist. Nothing to package. Aborting..')

        version = meta['app-version']
        name = meta['app-name']
        device = meta['target-device'] if 'target-device' in meta else 'skynode'
        out_file = os.path.join(args.project_dir, 'build', name + '.auterionos')

        meta_file = os.path.join(args.project_dir, 'auterion-app.yml')
        compose_file = os.path.join(self._temp_dir, 'docker-compose.yml')

        version_file = os.path.join(self._temp_dir, 'version')
        settings_file = os.path.join(self._temp_dir, 'settings.default.yml')
        app_file = os.path.join(self._temp_dir, 'app.yml')

        with open(version_file, 'w') as f:
            f.write(version)

        # Generate compose file with 'app.yml', and without the 'platform' line for older AuterionOS
        with open(compose_file, 'r') as fi:
            lines = fi.readlines()
        with open(app_file, 'w') as fo:
            for line in lines:
                if 'platform:' not in line and 'build:' not in line:
                    fo.write(line)

        pathlib.Path(settings_file).touch()

        run_command([
            self._mender_artifact_path, 'write', 'module-image',
            '-t', device,
            '-o', out_file,
            '-T', 'docker',
            '-n', name,
            '--software-filesystem', 'docker-app',
            '--software-name', name,
            '--software-version', version,
            '-f', app_file,
            '-f', version_file,
            '-f', image_file,
            '-f', settings_file,
            '-f', meta_file
        ])


