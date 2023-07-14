#!/usr/local/bin/python3
import chevron
import sys


def main(files, content):
    print(files)
    print()
    print(content)


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 3:
        raise Exception("Provide files, content input data")
    main(sys.argv[1], sys.argv[2])
