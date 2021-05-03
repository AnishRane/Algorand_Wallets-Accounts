from algosdk import kmd,mnemonic
from algosdk.wallet import Wallet
import json

kmd_token = "f814f65164d9dc03efe4381a06d0b1cfcc424f1c8f4e491f99775e0bf4d6b54e"
kmd_address ="http://127.0.0.1:7833"
kcl = kmd.KMDClient(kmd_token,kmd_address)


walletid = None
wallet = None
wallets = kcl.list_wallets()
for items in wallets:
    if items.get("name") == "AnishWallet":
        walletid = items.get('id')
        break
wallet_handle = kcl.init_wallet_handle(walletid,"testPassword")

print(walletid)
addressesInWallet = kcl.list_keys(wallet_handle)
accounts = {}
counter = 1
for address in addressesInWallet:
    private_key =kcl.export_key(wallet_handle,"testPassword",address)
    accounts[counter]={}
    accounts[counter]['public-key'] = address
    accounts[counter]['menmonic'] = mnemonic.from_private_key(private_key)

    counter += 1
print("Accounts in wallet are: ")
print(json.dumps(accounts,indent=4))


