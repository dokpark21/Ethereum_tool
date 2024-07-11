const { ethers } = require('ethers');

async function getPublicKeyFromTransactionHash(provider, txHash) {
  const tx = await provider.getTransaction(txHash);

  const unsignedTx = {
    gasLimit: tx.gasLimit,
    value: tx.value,
    nonce: tx.nonce,
    data: tx.data,
    chainId: tx.chainId,
    to: tx.to,
    type: tx.type,
    maxFeePerGas: tx.maxFeePerGas,
    maxPriorityFeePerGas: tx.maxPriorityFeePerGas,
  };

  const serializedTx = ethers.utils.serializeTransaction(unsignedTx);

  const { v, r, s } = tx;

  const signature = ethers.utils.joinSignature({ v, r, s });

  return ethers.utils.recoverPublicKey(
    ethers.utils.keccak256(serializedTx),
    signature
  );
}

// calculate account address from public key
async function getAccountAddressFromPublicKey(publicKey) {
  const address = ethers.utils.computeAddress(publicKey);
  return address;
}

(async () => {
  const provider = new ethers.providers.JsonRpcProvider(
    'https://mainnet.infura.io/v3/MY_INFURA_PROJECT_ID'
  );

  const txHash =
    '0x9a785725ad9a6ce23927d7965f946514c269914187201d3a3c51f22e9981a9a6';

  const address = await getPublicKeyFromTransactionHash(provider, txHash);

  console.log('publick key:', address);
  console.log('address:', await getAccountAddressFromPublicKey(address));
})();
