#!/usr/bin/env python3

import glob
import base64

def print_all_resources():
    for resource_path in glob.glob("./resources/*"):
        with open(resource_path, "r") as resource_file:
            print("\n=== Printing resource " + resource_path + " ===\n")
            resource = resource_file.read()
            decoded_resource = base64.b64decode(resource).decode()
            print(decoded_resource)

def main():
    print_all_resources()

if __name__ == "__main__":
    main()
