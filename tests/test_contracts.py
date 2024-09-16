import unittest
from web3 import Web3
import json

class TestContracts(unittest.TestCase):
    def setUp(self):
        infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        with open('../contracts/Voting.json') as f:
            self.voting_abi = json.load(f)
        self.contract_address = "YOUR_CONTRACT_ADDRESS"
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.voting_abi)

    def test_add_candidate(self):
        candidates_count = self.contract.functions.candidatesCount().call()
        self.assertGreater(candidates_count, 0)

if __name__ == '__main__':
    unittest.main()

