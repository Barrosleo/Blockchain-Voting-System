from web3 import Web3
import json

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

with open('../contracts/Voting.json') as f:
    voting_abi = json.load(f)

contract_address = "YOUR_CONTRACT_ADDRESS"
contract = web3.eth.contract(address=contract_address, abi=voting_abi)

def vote(candidate_id, voter_private_key):
    nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
    txn = contract.functions.vote(candidate_id).buildTransaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.signTransaction(txn, private_key=voter_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

if __name__ == "__main__":
    candidate_id = 1  # Example candidate ID
    voter_private_key = "YOUR_PRIVATE_KEY"
    tx_hash = vote(candidate_id, voter_private_key)
    print(f"Transaction hash: {tx_hash}")
