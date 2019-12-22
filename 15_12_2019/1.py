import hashlib


for i in range(0, 150000):
    if hashlib.sha256(str(i).encode()).hexdigest() == "7b2ba3258f43a686441328f3f7823f9141b39f85cc6c0f187ed1c585cbb500e0":
        print(i)
        break
