#!/usr/bin/env python3

import sys
import argparse

from manytime import many_time_pad_attack, load_and_continue


def main() -> None:
    """
    Main entry point for CLI program
    """
    parser = argparse.ArgumentParser(
        description="Break One-Time Pad Encryption with key reuse"
    )
    parser.add_argument(
        "file",
        type=str,
        help="file containing hexadecimal ciphertexts, delimited by new lines",
    )
    parser.add_argument(
        "-o",
        type=str,
        dest="output_file",
        default="result.json",
        help="filename to export decryptions to",
    )
    parser.add_argument(
        "-l",
        "--load",
        type=str,
        dest="load_file",
        default=None,
        help="filename to load previous results from",
    )
    args = parser.parse_args()

    with open(args.file, "r") as f:
        ciphertexts = [line.rstrip() for line in f]

    try:
        ciphertexts = list(map(bytearray.fromhex, ciphertexts))
    except ValueError as error:
        sys.exit("Invalid hexadecimal: {error}")

    if args.load_file:
        load_and_continue(ciphertexts, args.load_file, args.output_file)
    else:
        many_time_pad_attack(ciphertexts, args.output_file)


if __name__ == "__main__":
    main()
