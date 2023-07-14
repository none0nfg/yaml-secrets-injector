#!/usr/local/bin/python3
import chevron
import os


def main(files, content):
    print(files)
    print()
    print(content)


if __name__ == '__main__':
    inject_files = os.getenv("INPUT_INJECT_FILES")
    secrets = os.getenv("INPUT_SECRETS")
    main(inject_files, secrets)
