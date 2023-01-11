#!/usr/bin/env python3
"""
Author : px207 <px207@localhost>
Date   : 2023-01-11
Purpose: Rock the Casbah
"""

import argparse
import os.path
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    # Check if provided input is file path, return its contents
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Uncomment to use open(), write() and close()
    # if args.outfile:
    #     out_fh = open(args.outfile,'wt')
    # else:
    #     out_fh = sys.stdout
    # Oneliner for condition block above
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper()+'\n')
    out_fh.close()

    # Uncomment to use just print() function in oneliner
    #print(args.text.upper(), file=open(args.outfile,'wt')) if args.outfile else print(args.text.upper())
# --------------------------------------------------
if __name__ == '__main__':
    main()
