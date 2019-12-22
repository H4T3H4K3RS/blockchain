import requests
from hashlib import sha256

url = "http://188.225.24.93:5000"

while True:
    data = requests.get(url).json()['blocks']
    object = data[-1]
    for nonce in range(100203402034023402340234023040234002030243040234002340203402034):
        if sha256(str(object['hash'] + 'Ovchinnikov Vsevolod, da, da, ya/' + str(nonce)).encode()).hexdigest().startswith('0000'):
            requests.post(url + "/add", data={'text': 'Ovchinnikov Vsevolod, da, da, ya/', 'nonce': nonce})
            exit(0)