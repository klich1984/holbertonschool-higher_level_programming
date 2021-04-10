#!/usr/bin/python3
"""  script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    values = {
        'email': argv[2]
    }
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
