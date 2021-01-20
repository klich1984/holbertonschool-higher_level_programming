#!/usr/bin/python3
"""function that appends a string at the end of
    a text file (UTF8) and returns the number of
    characters added
"""


def append_write(filename="", text=""):
    """method that appends a string at the end of a text

    Args:
        filename (str): file to read and appends a string. Defaults to "".
        text (str): string for appends an file. Defaults to "".
    Return: returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
