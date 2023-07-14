#!/usr/local/bin/python3
import chevron
import os
import json


def main(files_str, content_str):
    files = files_str.split('\n')
    content = json.loads(content_str)
    for file_path in files:
        data = ""
        with open(file_path, "r") as f:
           data = chevron.render(f, content)
        with open(file_path, "w") as f:
            f.write(data)
        print(file_path)


if __name__ == '__main__':
    inject_files = os.getenv("INPUT_INJECT_FILES")
    if not inject_files:
        raise Exception("Please provide inject_files input data")
    secrets = os.getenv("INPUT_SECRETS")
    if not secrets:
        raise Exception("Please provide secrets input data")
    main(inject_files, secrets)
