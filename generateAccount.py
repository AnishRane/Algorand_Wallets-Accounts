from algosdk import kmd,mnemonic
from algosdk import account
kmd_token = "f814f65164d9dc03efe4381a06d0b1cfcc424f1c8f4e491f99775e0bf4d6b54e"
kmd_address ="http://127.0.0.1:7833"

kcl = kmd.KMDClient(kmd_token,kmd_address)

walletid = None
wallets = kcl.list_wallets()
for arrayitem in wallets:
    if arrayitem.get("name") == "AnishWallet":
        walletid = arrayitem.get("id")
        break
print("Got Wallet Id",walletid)

wallethandle = kcl.init_wallet_handle(walletid,"testPassword")
print("Got wallet Handle",wallethandle)

private_key,address= account.generate_account()

print("Account Address: ",address)

mn = mnemonic.from_private_key(private_key)
print('Mnemonic: ',mn)

importAccount = kcl.import_key(wallethandle,private_key)
print("Account Successfully imported: ",importAccount)
