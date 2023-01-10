#!/usr/bin/env python3
"""
Author: Jakub Slatinsky <slatinskyj@gmail.com>
Purpose: Say Hello, World!
"""

import argparse


def get_args():
    """ Parse program arguments """
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()


def main():
    """ Print a greeting """
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
