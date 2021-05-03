from algosdk.v2client import algod
from algosdk import account, mnemonic

algod_address="http://127.0.0.1:42827"
algod_token ="b60526bde3e25049f8b0e3a81bcfff8d913c725d510c6f579e1303c1e9973f1b"

algod_client = algod.AlgodClient(algod_token,algod_address)

passphrase = "online ring decorate dinosaur hub common maid disease pledge labor snow breeze also agree devote spoil law ranch primary palm kit dress enemy about argue"

private_key = mnemonic.to_private_key(passphrase)
my_address = mnemonic.to_public_key(passphrase)

account_info = algod_client.account_info(my_address)

balance = account_info.get('amount')
# print(balance)

print("Balance for Account is: ",balance)
