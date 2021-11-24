"""
 1. Wallet Create
 2. GOM2 Withdraw
 3. GOM2 Balance
"""

import requests
from web3 import Web3, HTTPProvider

GETH_URL = ""
GOM2_CONTRACT_ADDRESS = "0x48783486ddD7fa85ECa6B0C4AE8920Bc25DfbcD7"
ABI = ""


def create_wallet():
    """ 지갑 생성 """

    wallet_password = ""
    web3 = Web3(HTTPProvider(GETH_URL))
    erc20_address = web3.personal.newAccount(wallet_password)


def gom2_withdraw():
    """ GOM2 송금 """

    from_address = ""
    from_password = ""
    to_address = ""
    amount = ""

    web3 = Web3(HTTPProvider(GETH_URL))
    contract = web3.eth.contract(GOM2_CONTRACT_ADDRESS, abi=ABI)

    from_check_address = web3.toChecksumAddress(from_address)
    to_check_address = web3.toChecksumAddress(to_address)

    web3.personal.unlockAccount(from_check_address, from_password)

    tx_hash = contract.functions.transfer(to_address, int(amount)).transact(
        {'from': from_check_address})
    tx_receipt = web3.eth.getTransaction(tx_hash)

    web3.personal.lockAccount(from_check_address)
    web3.personal.lockAccount(to_check_address)


def gom2_balance():
    """ GOM2 잔고조회 (이더스캔 API) """

    wallet_address = ""
    apikey = ""
    etherscan_api_url = f"https://api.etherscan.io/api?" \
                        f"module=account&action=tokenbalance&" \
                        f"contractaddress={GOM2_CONTRACT_ADDRESS}&" \
                        f"address={wallet_address}&" \
                        f"tag=latest&apikey={apikey}"

    gom2_balance = requests.get(etherscan_api_url)
    gom2_balance = gom2_balance.json()['result']