#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()

r = response.info()
print(r)
print(dir(r))
print("***"*20)
print(dir(response))
print(r.__gt__)
print("***"*20)
print(response.getheader('X-Frame-Options'))