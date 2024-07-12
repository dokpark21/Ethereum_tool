from web3 import Web3

# Infura 또는 다른 이더리움 제공자 URL 사용
provider_url = "https://mainnet.infura.io/v3/34c821056a4443e69c731a619f706828"
web3 = Web3(Web3.HTTPProvider(provider_url))

validator_address = "0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97"

# The Merge가 발생한 블록 번호 (약 2022년 9월 15일)
merge_block = 15537393

# 블록의 범위를 설정 (예: 마지막 100000 블록을 검색)
start_block = 0

# Validator가 제안한 블록 찾기
def find_proposed_blocks(address, start_block, end_block):
    for block_number in range(start_block, end_block + 1):
        block = web3.eth.get_block(block_number)
        print(block_number)
        if block['miner'] == address:
            return block
    

# 블록 검색 실행 (The Merge 이전 블록만 검색)
block = find_proposed_blocks(validator_address, start_block, merge_block)

print(f"The first ETH1 block proposed by the validator is: {block}")
