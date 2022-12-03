#!/usr/bin/env python3
"""
Author : px207 <px207@localhost>
Date   : 2022-12-03
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""Crow's Nest -- choose the correct article""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    parser.add_argument('--side', help='A boat side',metavar='str',type=str,default="larboard")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    validate_word(word)
    side = args.side
    article = "an" if word[0].lower() in "aeiou"  else "a"
    article = article.title() if word[0].istitle() else article

    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")

def validate_word(word):
    if not word.isalpha():
        print(f"FAIL: {word} is not valid alphabetic string")
        sys.exit(1)
    return

# --------------------------------------------------
if __name__ == '__main__':
    main()
