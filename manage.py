#!./venv/bin/python3

import subprocess
import argparse

import yaml

parser = argparse.ArgumentParser()

parser.add_argument('action')
parser.add_argument('subapp')
parser.add_argument('env')

args = parser.parse_args()


def replace_properties(source: str, dest: str):
    f = open(source)
    f_contents = f.read()
    f.close()

    config_file = open('./config.yml')
    config_contents = config_file.read()
    config_file.close()
    config = yaml.safe_load(config_contents)

    for c in config['env'][args.env]:
        f_contents = f_contents.replace(
            f'#{{{c}}}', f'{config["env"][args.env][c]}')

    f_dest = open(dest, 'w+')
    f_dest.write(f_contents)
    f_dest.close()


if args.subapp == 'minio':
    replace_properties('./docker-compose-minio-template.yml',
                       './docker-compose-minio.yml')

    if args.action == 'run':
        steps = [
            ('docker compose -f docker-compose-minio.yml up', '.')
        ]

        for (s, cwd) in steps:
            subprocess.run(s, shell=True, cwd=cwd)

elif args.subapp == 'nextcloud':
    replace_properties('./docker-compose-template.yml',
                       './docker-compose.yml')

    if args.action == 'run':
        steps = [
            ('docker compose up', '.')
        ]

        for (s, cwd) in steps:
            subprocess.run(s, shell=True, cwd=cwd)

else:
    print('Irrelevant')
