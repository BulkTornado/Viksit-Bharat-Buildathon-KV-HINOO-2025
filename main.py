"""
Python project for Cybersecurity
"""

import pathlib, argparse, sys, os, json
from function_modules import ConnectToMySQL, MainWindow



def main():
    root = MainWindow()

    root.start()

if __name__ == '__main__':
    main()
