#!/usr/bin/python3
"""  """
from urllib import request, parse
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.code)
