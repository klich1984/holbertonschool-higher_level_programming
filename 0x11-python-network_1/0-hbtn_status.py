#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request

url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()

print(dir(html))
print(html.decode('utf-8'))
print(type(html))
print(html)
print(dir(response))

