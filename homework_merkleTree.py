import requests
import hashlib

def double_sha256(s):
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def calculate_merkle_root(tx_hashes):
    # Convert hex strings to bytes and apply little-endian conversion
    tx_hashes = [bytes.fromhex(tx)[::-1] for tx in tx_hashes]

    while len(tx_hashes) > 1:
        if len(tx_hashes) % 2 != 0:
            tx_hashes.append(tx_hashes[-1])
        new_level = []
        for i in range(0, len(tx_hashes), 2):
            # Combine and hash in little-endian order
            combined = tx_hashes[i] + tx_hashes[i + 1]
            new_level.append(double_sha256(combined))
        tx_hashes = new_level

    return tx_hashes[0][::-1].hex()

# Provided data
mr = 'mekle root'
tx_list = [
    'transacions'
]

# Brute-force to find the missing tx hash
for i in range(65536):
    trial_hash = hashlib.sha256(i.to_bytes(2, byteorder='little')).digest()[::-1].hex()
    tx_list_copy = tx_list.copy()
    tx_list_copy[tx_list_copy.index('?' * 64)] = trial_hash
    result = calculate_merkle_root(tx_list_copy)
    if result == mr:
        print(f"Found hash: {trial_hash}")
        break
