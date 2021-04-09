#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request

url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()

print('Body response:')
print(f'\t- type: {type(html)}')
print(f'\t- content: {html}')
print(f"\t- utf8 content: {html.decode('utf-8')}")
