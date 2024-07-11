const { ethers } = require('ethers');

// Function to extract the address associated with to a transaction
async function getPublicKeyFromTransactionHash(provider, txHash) {
  // Fetch the transaction using the transaction hash and provier
  const tx = await provider.getTransaction(txHash);

  // Extract the all the relevant fields from the transaction (We need all of them)
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

  // Serializing tx without the signature
  const serializedTx = ethers.utils.serializeTransaction(unsignedTx);

  // Extract the signature (v, r, s) from the transaction
  const { v, r, s } = tx;

  // Join splitted signature
  const signature = ethers.utils.joinSignature({ v, r, s });

  // Recover the address or public key with (replace recoverAddress by recoverPublicKey) associated with the transaction
  return ethers.utils.recoverAddress(
    ethers.utils.keccak256(serializedTx),
    signature
  );
}

// Call the function with a provider and a transaction hash
(async () => {
  // Public provider for Goerli
  const provider = new ethers.providers.JsonRpcProvider(
    'https://mainnet.infura.io/v3/64399f7381854c4ebb02ae69db93c72c'
  );

  // Transaction hash
  const txHash =
    '0xda86cb8fbfa5ec2cc3c1730d785b548df0de827ffb139c258a954128b1c463cd';

  // And finally call the function to extract the address associated with the transaction
  const address = await getPublicKeyFromTransactionHash(provider, txHash);

  console.log('Address:', address);
})();
