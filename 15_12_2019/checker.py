import requests
from hashlib import sha256

url = "http://188.225.24.93:5000"

while True:
    # all_data = requests.get(url).json()
    all_data = {"blocks":[{"hash":"0000000000000000000000000000000000000000000000000000000000000000","nonce":"0","text":"Genesis block","time":"2019-10-27 15:24:21.262894"},{"hash":"0000463ce2ad0b2f7cc80ec565459ce78bacfc7ac922a3f0f2af49097617d308","nonce":"1000047937","text":"The server is used for control work.","time":"2019-10-27 15:25:41.220352"},{"hash":"000022df3b8dae081c7aea859d399452291595ab014769ca46fe79411563b6f1","nonce":"1000016330","text":"Cicada see you","time":"2019-10-27 15:26:16.820500"},{"hash":"00001cb58e8024f16f953dfdfe3106875238535b94759d6340013e3810fb54ab","nonce":"1000047109","text":"Liber primus","time":"2019-10-27 15:26:41.512413"},{"hash":"0000c7db931f310eba92fa6e6026946aa4f23b5b25fcbfd04e40b0206076c28a","nonce":"2663","text":"Ovchinnikov Vsevolod, da, da, ya/","time":"2019-10-27 16:06:40.884955"},{"hash":"00009466f9e8328f622d615a1c35999dcad0bcc1a52f13444d867a57212e6c0e","nonce":"47169","text":"Ovchinnikov Vsevolod, da, da, ya/","time":"2019-10-27 16:06:57.918133"}],"size":6}
    flag = True
    data = all_data['blocks']
    for block in range(1, len(data)):
        if sha256(str(data[block - 1]['hash'] + data[block]['text'] + data[block]['nonce']).encode()).hexdigest() != data[block]['hash'] or not(data[block]['hash'].startswith('0' * (4 + all_data['size'] // 30))):
            flag = False
            break
    if flag:
        print("CORRECT")
    else:
        print("FAKE")
