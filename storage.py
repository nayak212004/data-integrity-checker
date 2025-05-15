import json
from block import Block, Blockchain

def save_chain(blockchain, filename='blockchain.json'):
    with open(filename, 'w') as f:
        json.dump(blockchain.to_dict(), f, indent=4)

def load_chain(filename='blockchain.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        chain = []
        for b in data:
            blk = Block(b['index'], b['timestamp'], b['data'], b['previousHash'])
            chain.append(blk)

        bc = Blockchain()
        bc.chain = chain
        return bc
    except FileNotFoundError:
        return Blockchain()
