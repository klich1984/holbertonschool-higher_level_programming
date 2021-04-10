#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server
running on port 5000
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    bad_r = requests.get(url)

    if bad_r.status_code == 200:
        print(bad_r.text)
    else:
        print('Error code: {}'.format(bad_r.status_code))
