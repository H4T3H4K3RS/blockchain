import requests
from hashlib import sha256

url = "http://188.225.24.93:5000/transaction"

data = requests.get(url).json()['transaction']
users = {data[0]['To']: data[0]['Amount']}
for i in range(1, len(data)):
    try:
        users[data[i]['To']] += data[i]['Amount']
    except Exception:
        users[data[i]['To']] = data[i]['Amount']
    try:
        users[data[i]['From']] -= data[i]['Amount']
    except Exception:
        users[data[i]['From']] = data[i]['Amount']
fro = input()
to = input()
am = float(input())
if users[fro] < am:
    print("NO")
else:
    print("YES")
