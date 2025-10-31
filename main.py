"""
Python project for Cybersecurity
"""

import pathlib, argparse, sys, os, json
from function_modules import ConnectToMySQL, MainWindow

def get_configuration():
    try:
        with open('configuration.json', 'r') as config_file:
            return json.load(config_file)
    except Exception as exc:
        print('Seems configuration file is missing or can\'t be accessed.')
        print(f'Here\'s the error traceback: {exc}')
        sys.exit()


def main():
    configuration: dict = get_configuration()

    geometry = configuration.get('geometry', (840,613))
    window_title = configuration.get('title', 'Cyber Security')

    assets: tuple[tuple[int, str, list[int]]] = configuration.get('assets', [])

    root = MainWindow()

    root.configure_window(geometry, window_title)
    for asset in assets:
        root.add_asset(asset) # type: ignore
        #print(tuple(asset[1:]))

    root.start()

if __name__ == '__main__':
    main()
