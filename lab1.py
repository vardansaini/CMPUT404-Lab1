import requests

print(requests.__version__)

print(requests.get('https://www.google.com'))

print(requests.get('https://www.google.com').content)