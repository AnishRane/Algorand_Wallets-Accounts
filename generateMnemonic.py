from algosdk import kmd,mnemonic
from algosdk.wallet import Wallet


kmd_token = "f814f65164d9dc03efe4381a06d0b1cfcc424f1c8f4e491f99775e0bf4d6b54e"
kmd_address = "http://127.0.0.1:7833"

kcl = kmd.KMDClient(kmd_token,kmd_address)

walletid = None
wallets = kcl.list_wallets()
for item in wallets:
    if item.get("name")=="AnishWallet":
        walletid = item.get('id')
        break

wallethandle = kcl.init_wallet_handle(walletid,"testPassword")
accountKey = kcl.export_key(wallethandle,'testPassword',"PIFKEL4WB6NAAPEDLW4ZGE6XUGZN7EKL6YDCQIHFFWMIW5A233JG65FLEE")
mn = mnemonic.from_private_key(accountKey)
print("Account Mnemonic: {}",format(mn))
