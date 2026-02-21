"""
Many-time module
"""

import sys
import argparse

from manytime import analysis
from manytime.interactive import interactive, load_from_result

from typing import Iterable


def many_time_pad_attack(
    ciphertexts: Iterable[bytearray], results_filename: str
) -> None:
    """
    Perform a Many-time pad attack

    First we recover as much as the key we can using automated cryptanalysis,
    then drop the user into an interactive session to complete the decryption.
    """
    partial_key = analysis.recover_key(ciphertexts)
    interactive(ciphertexts, partial_key, results_filename)


def load_and_continue(
    ciphertexts: Iterable[bytearray], load_filename: str, results_filename: str
) -> None:
    """
    Load a previous session from result file and continue decryption

    Reconstructs the key and ciphertexts from the result file,
    then opens an interactive session to continue decryption.
    """
    load_from_result(ciphertexts, load_filename, results_filename)


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
