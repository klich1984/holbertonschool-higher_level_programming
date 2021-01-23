#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        str1 = str.replace(str[n], "")
        return (str1)

    else:
        return (str)
