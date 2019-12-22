from time import sleep

from web3 import Web3, HTTPProvider
from web3 import eth
import os

os.environ['WEB3_INFURA_PROJECT_ID'] = '860f688733f2410a94e2e085457cc54c'
os.environ['WEB3_INFURA_PROJECT_SECRET'] = 'c6054bec4e5e4f28bade2a934c255038'
w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/860f688733f2410a94e2e085457cc54c'))

for i in range(100):
    dict_eth = w3.eth.getBlock('latest')
    ABI = [{"constant": False, "inputs": [{"name": "_url", "type": "string"}], "name": "setUrl", "outputs": [],
            "payable": False, "stateMutability": "nonpayable", "type": "function"},
           {"constant": False, "inputs": [{"name": "_cost", "type": "uint32"}], "name": "setCost", "outputs": [],
            "payable": False, "stateMutability": "nonpayable", "type": "function"},
           {"constant": True, "inputs": [], "name": "getCost", "outputs": [{"name": "", "type": "uint32"}],
            "payable": False, "stateMutability": "view", "type": "function"},
           {"constant": True, "inputs": [], "name": "getUrl", "outputs": [{"name": "", "type": "string"}], "payable": False,
            "stateMutability": "view", "type": "function"},
           {"inputs": [{"name": "_url", "type": "string"}, {"name": "_cost", "type": "uint32"}], "payable": False,
            "stateMutability": "nonpayable", "type": "constructor"}]
    tmp_contract = w3.eth.contract(
        address="0xe6B17165fD4DB8A910BA20Ea1b05c00488DD3578",
        abi=ABI
    )
    # contract_value = tmp_contract.functions.getCost().call()
    w3.eth.account = '0xB0329a4B11143e2f57F0238805E05dd96DD1eC5A'
    # print(w3.eth.getBalance(w3.eth.account))
    # print(contract_value)
    CloseWalletKey = "346F49626F65F952B52CEF5678F9B4AD1DD2B065226CB49579B06F67065789D6"
    tmp_contract_txn = tmp_contract.functions.setCost(100).buildTransaction({
        'chainId': 3,
        'gas': 300000,
        'gasPrice': w3.eth.gasPrice,
        'nonce': w3.eth.getTransactionCount(w3.eth.account),
        'value': 0,
    })
# print(tmp_contract_txn)
    try:
        sign_txn = eth.Account.sign_transaction(tmp_contract_txn, CloseWalletKey)
        print(w3.eth.sendRawTransaction(sign_txn.rawTransaction))
    except ValueError:
        print("bad")
