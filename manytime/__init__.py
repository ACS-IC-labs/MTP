"""
Many-time module
"""

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
