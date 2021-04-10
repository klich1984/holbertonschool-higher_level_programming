#!/usr/bin/python3
"""  script that fetches https://intranet.hbtn.io/status
- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example
(tabulation before -)
"""
import requests

r = requests.get('https://intranet.hbtn.io/status')
# print(dir(r))
print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))
