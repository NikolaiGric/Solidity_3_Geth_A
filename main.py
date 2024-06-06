from web3 import Web3
from web3.middleware import geth_poa_middleware

# Ваши данные конфигурации
addresses = [
    '0x5E0c29dB6a58E3281CFD997Bff80fa335fc8e8B4',
    '0xf918D22C83C1cdA979523824454473C07Cb15e64',
    '0xc5b1a1fd17d3e9dce35632df923ecb5892a7111b',
    '0xe294b3bf494d8ac84ff929effc79a76e38a80c3e',
    '0x03152371e4efa8bacd84139353d806f7ebe38564'
]

# Инициализация web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Функция для получения баланса
def get_balance(address):
    checksum_address = Web3.to_checksum_address(address)
    return w3.eth.get_balance(checksum_address)

# Печать балансов
for address in addresses:
    balance = get_balance(address)
    print(f"Баланс ({address}): {balance}")
