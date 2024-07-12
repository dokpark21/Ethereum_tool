import hashlib
import hmac
import binascii
from mnemonic import Mnemonic
from ecdsa import SigningKey, SECP256k1

def mnemonic_to_seed(mnemonic: str, passphrase: str = '') -> bytes:
    mnemonic = mnemonic.encode('utf-8')
    salt = ('mnemonic' + passphrase).encode('utf-8')
    return hashlib.pbkdf2_hmac('sha512', mnemonic, salt, 2048)

def seed_to_master_key(seed: bytes) -> (bytes, bytes):
    I = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    master_private_key = I[:32]
    master_chain_code = I[32:]
    return master_private_key, master_chain_code

def derive_private_key(master_private_key: bytes, master_chain_code: bytes, derivation_path: str) -> bytes:
    def hmac_sha512(key: bytes, data: bytes) -> bytes:
        return hmac.new(key, data, hashlib.sha512).digest()

    def parse_derivation_path(path: str) -> [int]:
        elements = path.split('/')
        return [int(x[:-1]) + 0x80000000 if x.endswith("'") else int(x) for x in elements if x != 'm']

    kL = master_private_key
    cL = master_chain_code
    for index in parse_derivation_path(derivation_path):
        data = b'\x00' + kL + index.to_bytes(4, 'big')
        I = hmac_sha512(cL, data)
        kL, cL = I[:32], I[32:]

    return kL

def private_key_to_ethereum_address(private_key: bytes) -> str:
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    vk = sk.get_verifying_key()
    public_key = b'\x04' + vk.to_string()

    keccak = hashlib.new('sha3_256')
    keccak.update(public_key[1:])
    address = '0x' + keccak.hexdigest()[24:]
    return address

mnemonic = "bus unfold gym admit know climb immune relax bridge sudden unhappy witness"
derivation_path_template = "m/44'/60'/0'/0/{}"  # BIP-44 표준 경로 (Ethereum)

target_address = "0x927C084Dc00884c21Cb7f11122B046E358588Cde"

seed = mnemonic_to_seed(mnemonic)

master_private_key, master_chain_code = seed_to_master_key(seed)

derivation_path = derivation_path_template.format(9287)
private_key = derive_private_key(master_private_key, master_chain_code, derivation_path)
eth_address = private_key_to_ethereum_address(private_key)

print(f"Derivation path: {derivation_path}")
print(f"Ethereum Address: {eth_address}")
print(f"Private Key: {binascii.hexlify(private_key).decode()}")