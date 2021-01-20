#!/usr/bin/python3
"""function that appends a string at the end
    of a text file (UTF8) and returns the
    number of characters added:
"""


def write_file(filename="", text=""):
    """method that append a string at the end
        of a text

    Args:
        filename (str): File to read. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
