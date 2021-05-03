from algosdk import kmd
from algosdk.wallet import Wallet

kmd_token = "f814f65164d9dc03efe4381a06d0b1cfcc424f1c8f4e491f99775e0bf4d6b54e"
kmd_address="http://127.0.0.1:7833"

kcl = kmd.KMDClient(kmd_token,kmd_address)

#create Wallet
wallet = Wallet("AnishWallet","testPassword",kcl)

info = wallet.info()

#get wallet information
print("wallet name:",info["wallet"]["name"])



