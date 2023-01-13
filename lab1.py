import requests

print(requests.__version__)

print('######################## VARDAN LAB 1 Google ############################')

print(requests.get('https://www.google.com'))

print(requests.get('https://www.google.com').content)

print(requests.get('https://www.google.com').text)

print('######################## VARDAN LAB 1 Github ############################')

print(requests.get(
    'https://raw.githubusercontent.com/vardansaini/CMPUT404-Lab1/main/lab1.py').content)

print('######################## VARDAN LAB 1 text ############################')

print(requests.get(
    'https://raw.githubusercontent.com/vardansaini/CMPUT404-Lab1/main/lab1.py').text)
