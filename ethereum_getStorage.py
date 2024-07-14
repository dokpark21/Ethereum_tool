from web3 import Web3

# Infura를 통해 이더리움 메인넷에 연결
infura_url = "https://mainnet.infura.io/v3/MY_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# 컨트랙트 주소 설정
contract_address = "0x4b4438ea9340f9df6bbb13deb2129ee8450b5f24"
contract_address = web3.to_checksum_address(contract_address)

# 정확한 스토리지 주소
storage_slot = '0x00000000000000000000000000000000000000000000000000001337deadbeef'

# 스토리지 값 읽기
storage_value = web3.eth.get_storage_at(contract_address, storage_slot)

# 32바이트 정렬된 hex 형식으로 출력
hex_encoded_value = Web3.to_hex(storage_value)
print(hex_encoded_value)