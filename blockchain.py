import hashlib
import time

# Our "blockchain"
blockchain = []

def add_block(data, verified=False):
    prev_hash = blockchain[-1]['hash'] if blockchain else "0"
    timestamp = time.time()
    data["verified"] = verified  # Store verification status
    block_content = str(data) + str(timestamp) + prev_hash
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()
    block = {
        "data": data,
        "timestamp": timestamp,
        "prev_hash": prev_hash,
        "hash": block_hash
    }
    blockchain.append(block)
    return block


def view_chain():
    for i, block in enumerate(blockchain):
        print(f"Block {i+1}: {block}\n")
    return blockchain

# Simulated token ledger
tokens = {}

def issue_tokens(user, trees_planted):
    tokens[user] = tokens.get(user, 0) + trees_planted
    print(f"Issued {trees_planted} tokens to {user}. Total: {tokens[user]}")
