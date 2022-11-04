#!/usr/bin/env python3
"""
Author: Robert Aguinaga
Purpose: Say hello
"""
from argparse import ArgumentParser


def get_args():
    """Get the command-line args"""
    parser = ArgumentParser(description="Say Hello!")
    parser.add_argument(
        "-n",
        "--name",
        default="World",
        type=str,
        metavar="name",
        help="Name to greet",
    )
    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
