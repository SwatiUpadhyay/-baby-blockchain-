# blockchain/block.py

import hashlib
import json
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()  # current time in seconds
        self.data = data              # can be any info: message, transaction, etc.
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Converts block data into a hash string using SHA-256
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return (
            f"Block(\n"
            f"  Index: {self.index},\n"
            f"  Timestamp: {self.timestamp},\n"
            f"  Data: {self.data},\n"
            f"  Prev Hash: {self.previous_hash},\n"
            f"  Hash: {self.hash}\n"
            f")"
        )
