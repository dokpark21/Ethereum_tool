const bip39 = require('bip39');
const hdkey = require('hdkey');
const ethUtil = require('ethereumjs-util');

// Mnemonic 문구
const mnemonic =
  'bus unfold gym admit know climb immune relax bridge sudden unhappy witness';

// 목표 주소
const targetAddress =
  '0x927C084Dc00884c21Cb7f11122B046E358588Cde'.toLowerCase();

// Mnemonic을 사용하여 Seed 생성
const seed = bip39.mnemonicToSeedSync(mnemonic);

// HD Wallet 생성
const root = hdkey.fromMasterSeed(seed);

// 여러 파생 경로를 시도하여 목표 주소와 일치하는 주소를 찾기
let found = false;

for (let index = 0; index < 100000; index++) {
  // 필요에 따라 범위를 조정
  const derivationPath = `m/44'/60'/0'/0/${index}`;
  const derivedNode = root.derive(derivationPath);
  const privateKey = derivedNode.privateKey;
  const addressBuffer = ethUtil.privateToAddress(privateKey);
  const ethAddress = ethUtil.toChecksumAddress(
    '0x' + addressBuffer.toString('hex')
  );

  console.log(`Trying derivation path: ${derivationPath}`);
  console.log(`Ethereum Address: ${ethAddress}`);
  console.log(`Private Key: ${privateKey.toString('hex')}`);

  if (ethAddress.toLowerCase() === targetAddress) {
    console.log('Found matching address!');
    console.log(`Derivation Path: ${derivationPath}`);
    console.log(`Private Key: 0x${privateKey.toString('hex')}`);
    found = true;
    break;
  }
  if (found) break;
}

if (!found) {
  console.log('No matching address found.');
}
