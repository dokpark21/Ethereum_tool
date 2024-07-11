from web3 import Web3

# Infura를 통해 이더리움 메인넷에 연결
infura_url = "https://mainnet.infura.io/v3/64399f7381854c4ebb02ae69db93c72c"
web3 = Web3(Web3.HTTPProvider(infura_url))

# 컨트랙트 주소 및 ABI 설정
contract_address = "0x4b4438ea9340f9df6bbb13deb2129ee8450b5f24"
contract_address = web3.to_checksum_address(contract_address)  # 체크섬 주소로 변환
contract_abi = [
    {
        "type": "function",
        "name": "key",
        "inputs": [],
        "outputs": [{"name": "", "type": "string", "internalType": "string"}],
        "stateMutability": "view"
    }
]

# 컨트랙트 인스턴스 생성
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# key() 함수 호출
key_value = contract.functions.key().call()

# 반환 값을 hex 형식으로 인코딩
hex_encoded_key = key_value.encode('utf-8').hex()
print("0x" + hex_encoded_key)