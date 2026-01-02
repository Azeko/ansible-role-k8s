#!/usr/bin/env python3

import argparse
import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_name')
    parser.add_argument('--env_value')
    parser.add_argument('--yaml_filename')
    return parser.parse_args()


def set_env_variable(filename: str, env_name: str, env_value: str) -> None:
    with open(filename) as fd:
        data = yaml.safe_load(fd)

    for container in data['spec']['containers']:
        env_exists = False
        for env in container['env']:
            if env['name'] == env_name:
                env['value'] = env_value
                env_exists = True
        if not env_exists:
            container['env'].append({'name': env_name, 'value': env_value })

    output_data = yaml.safe_dump(data)
    with open(filename, 'w') as fd:
        fd.write(output_data)


if __name__ == '__main__':
    args = parse_args()
    set_env_variable(args.yaml_filename, args.env_name, args.env_value)
