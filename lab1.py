import requests

print(requests.__version__)

print(requests.get('https://www.google.com'))

print(requests.get('https://www.google.com').content)

print('######################## VARDAN LAB 1 ############################')

print(requests.get(
    'https://raw.githubusercontent.com/vardansaini/CMPUT404-Lab1/main/lab1.py').content)

print('######################## VARDAN LAB 1 text ############################')

print(requests.get(
    'https://raw.githubusercontent.com/vardansaini/CMPUT404-Lab1/main/lab1.py').text)
