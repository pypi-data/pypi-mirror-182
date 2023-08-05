# Introduction

This is a library used to use `web3.py` on conflux-bridge(?). This library hacks the signing machanism of `web3.py`.

## Install

This library requires python >= 3.7

It is recommended to use this library in a virtual environment.

``` bash
python -m venv venv
source ./venv/bin/activate
```

or 

``` bash
conda create -n venv python=3.7
conda activate venv
```

Then install in the virtual environment

``` bash
pip install conflux-web3py-signer
```

## How to use

### Basic Usage

Import `conflux_we3py_signer` before import `web3`.

```python
import conflux_web3py_signer
import web3
```

### Use with Brownie

Firstly, you are supposed to install brownie and add [conflux-bridge endpoints](https://docs.nftrainbow.xyz/products/rpc-bridge) to brownie networks

``` bash
pip install conflux_web3py_signer[brownie]
cfx-brownie networks add Conflux cfx-testnet-bridge host=https://cfx2ethtest.nftrainbow.cn chainid=1
```

Then use with command-line with target network.

``` bash
cfx-brownie --network cfx-testnet-bridge
```

## What is Done

### Transaction Cast

When the modified `construct_sign_and_send_raw_middleware` is going to sign a transaction, it will convert an EIP-1559 transaction to conflux transaction following the rule:

* If `gasPrice` is missing, use `maxFeePerGas` as gas price.
* Fill `epochHeight` with `w3.eth.block_number`, which correspondes to `epoch_number` in conflux.
* Estimate the transaction and fill `storageLimit` from estimate result.

### Address Cast

EOA account addresses are all converted to begin with `0x1` and is encoded in checksum format
