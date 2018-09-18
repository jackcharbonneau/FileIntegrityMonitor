#!/usr/bin/env python3

# Jack Charbonneau 09/17/2018

import csv


def main():
    #  TODO parse arguments
    parse()

    valids = loadChecksums()

    #  TODO for each file
        #  TODO get checksum
        #  TODO compare checksums
        #  TODO if valid report valid and update datetime
        #  TODO if invalid report invalid state last valid datetime
    pass


def parse():
    pass


def loadChecksums():
    #  Load in database/file
    with open("valid_checksums.csv", newline='') as f:
        reader = csv.reader(f)
        valids = list(reader)
        return valids


if __name__ == "__main__":
    main()
