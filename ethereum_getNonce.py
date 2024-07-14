from web3 import Web3
import rlp
from eth_utils import keccak

# 배포자 주소와 nonce 설정
deployer_address = "MY_INFURA_PROJECT_ID"
nonce = 1337  # 해당 트랜잭션의 nonce 값

# RLP 인코딩
rlp_encoded = rlp.encode([Web3.to_bytes(hexstr=deployer_address), nonce])

# Keccak-256 해시 계산
contract_address_bytes = keccak(rlp_encoded)[12:]

# 컨트랙트 주소 추출
contract_address = Web3.to_checksum_address(contract_address_bytes)
print(f"Calculated contract address: {contract_address}")