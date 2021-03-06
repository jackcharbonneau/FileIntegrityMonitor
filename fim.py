#!/usr/bin/env python3

# Jack Charbonneau 09/17/2018

import argparse
import csv
import hashlib
import datetime


def main():
    """Take a new file and create a checksum from it for future integrity
    checks or verify and output the integrity of all files currently in
    the monitors list
    """
    new_file = parse()

    #  If no file was provided, run integrity check.
    if new_file is None:
        valids = loadChecksums()
        checkIntegrity(valids)
    #  If a file was provided, add its checksum for future integrity checks.
    else:
        addFile(new_file)


def parse():
    """Parse argument for a new file"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, dest='new_file',
                        help='specify a new file to add to the' +
                        'integrity monitoring list')
    args = parser.parse_args()

    return args.new_file


def loadChecksums():
    """Load in valid_checksums.csv"""
    try:
        with open("valid_checksums.csv", newline='') as f:
            reader = csv.reader(f)
            valids = list(reader)
            return valids
    except:
        print("[-] Could not open file: valid_checksums.csv")
        exit(0)


def checkIntegrity(valids):
    """Verify the checksum for each file in the csv and print whether not the
    file has maintained its integrity.
    """

    for file in valids:
        hash = hashlib.sha256()
        try:
            with open(file[0], 'rb') as f:
                for data in iter(lambda: f.read(4096), b''):
                    hash.update(data)

                if hash.hexdigest() == file[1]:
                    file[2] = datetime.datetime.now()
                    print("[+] integrity secure: %s " % file[0])

                else:
                    print("[-] integrity not secure: %s " % file[0])
                    print("[-] last valid integrity check: %s " % file[2])
        except:
            print("[-] Could not open file: %s" % file[0])


def addFile(file_path):
    """Take the checksum of a new file and add it to valid_checksums.csv"""
    hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as new_file:
            for data in iter(lambda: new_file.read(4096), b''):
                    hash.update(data)
    except:
        print("[-] Could not open file: %s" % file_path)
        exit(0)

    try:
        with open('valid_checksums.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([file_path, hash.hexdigest(),
                            datetime.datetime.now()])
    except:
        print("[-] Could not open file: valid_checksums.csv")
        exit(0)


if __name__ == "__main__":
    main()
