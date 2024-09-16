import unittest
from backend import vote

class TestBackend(unittest.TestCase):
    def test_vote(self):
        candidate_id = 1
        voter_private_key = "YOUR_PRIVATE_KEY"
        tx_hash = vote(candidate_id, voter_private_key)
        self.assertIsNotNone(tx_hash)

if __name__ == '__main__':
    unittest.main()

