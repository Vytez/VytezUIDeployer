#!/usr/bin/env python3
import os
import json
import shutil

def main():
    with open('config.json') as config_file:
        config_data = json.load(config_file)

    source_directory = config_data['source_directory']
    target_directory = config_data['target_directory']

    for item in os.listdir(source_directory):
        if os.path.isdir(os.path.join(source_directory, item)) and item != '.git':
            DeployAddon(source_directory, target_directory, item)

def DeployAddon(source, target, dir):    
    try:
        shutil.rmtree(os.path.join(target, dir))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    shutil.copytree(os.path.join(source, dir), os.path.join(target, dir))
    
if __name__ == "__main__":
    main()


