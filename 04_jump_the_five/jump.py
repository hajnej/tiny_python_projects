#!/usr/bin/env python3
"""
Author : px207 <px207@localhost>
Date   : 2023-01-09
Purpose: Rock the Casbah
"""

import argparse

ENCODING_TABLE = {
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
    "0": "5"
}

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for character in args.text:
        print(ENCODING_TABLE.get(character,character),end="")
    print()



# --------------------------------------------------
if __name__ == '__main__':
    main()
