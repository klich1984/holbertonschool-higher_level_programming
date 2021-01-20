#!/usr/bin/python3
"""Function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """method that open, read and print a file (UTF8)

    Args:
        filename (str): File to read. Defaults to "".
    """
    print(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        read_file = f.read()
        print(read_file, end="")
