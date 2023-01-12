#!/usr/bin/env python3
"""
Author : px207 <px207@localhost>
Date   : 2023-01-12
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files_count=len(args.file)
    # Init counters for total number of lines,works and bytes if count of file is more than 2
    if files_count > 1:
        total_num_lines=0
        total_num_words=0
        total_num_bytes=0
    # Iterate over all files handles
    for file_handle in args.file:
        # Init counters
        num_lines = 0
        num_words = 0
        num_bytes = 0
        # Read a line from file handle
        for line in file_handle:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        file_handle.close()
        if files_count > 1:
            total_num_lines += num_lines
            total_num_words += num_words
            total_num_bytes += num_bytes
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {file_handle.name}')
    if files_count > 1:
        print(f'{total_num_lines:8}{total_num_words:8}{total_num_bytes:8} total')

# --------------------------------------------------
if __name__ == '__main__':
    main()
