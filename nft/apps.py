from django.apps import AppConfig
import requests
import json


class NftConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "nft"

# Youtube guide I used to do this NFT: https://www.youtube.com/watch?v=4A-Ti_sb-Mo"

NFT_URI = "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F6097d" \
          "7ee81957044af68d9ce%2FSNL%2F960x0.jpg%3Ffit%3Dscale"
NFT_NAME = "Wario Musk"
NFT_SYMBOL = "WARIO"
NFT_DESCRIPTION = "The ONLY Wario NFT!"
NFT_METADATA = {
    "cleverness": 100,
    "intelligence": 100,
    "musk": 99,
    "warioness": 98
}

# signature = 5uiv6g3BWUb17MdjJ82EaP12K7ZfdHqHF9mHN5iq6Aze8tGFExfk76KdDsPc653Hd25N659BWHXRTnDo7We9gKa9

KEY_ID = "39x3inOdqYJQfYA"
SECRET_KEY = "VwPd8BXNCT77Xpb"
HEADERS = {
    "APIKeyID": KEY_ID,
    "APISecretKey": SECRET_KEY,
}

SECRET_PHRASE_ENDPOINT = "https://api.blockchainapi.com/v1/solana/wallet/generate/secret_recovery_phrase"
PUBLIC_KEY_ENDPOINT = "https://api.blockchainapi.com/v1/solana/wallet/public_key"
BALANCE_ENDPOINT = "https://api.blockchainapi.com/v1/solana/wallet/balance"
NFT_MINT_FEE_ENDPOINT = "https://api.blockchainapi.com/v1/solana/nft/mint/fee"
NFT_ENDPOINT = "https://api.blockchainapi.com/v1/solana/nft"

SECRET_PHRASE = "fuel battle orient upper fatigue logic infant few you salute piano rich"
DERIVATION_PATH = ""

PUBLIC_KEY = "2cQFPRPP1NmTbD14su4S43CYcSUXcHg2s1gLArf7raMr"

def get_secret_phrase():
    response = requests.post(
        SECRET_PHRASE_ENDPOINT,
        headers=HEADERS
    )
    print(response.json())

def derive_public_key():
    response = requests.post(
    PUBLIC_KEY_ENDPOINT,
    params={
        "derivation_path": DERIVATION_PATH,
        "secret_recovery_phrase": SECRET_PHRASE
    },
    headers=HEADERS,
    )
    print(response.json())

def get_balance():
    response = requests.get(
    BALANCE_ENDPOINT,
    params={
        "public_key": PUBLIC_KEY
    },
    headers=HEADERS,
    )
    print(response.json())

def get_nft_mint_fee():
    response = requests.get(
    NFT_MINT_FEE_ENDPOINT,
    headers=HEADERS,
    )
    print(response.json())

if __name__== "__main__":
    # print(json.dumps(NFT_METADATA))
    response = requests.post(
    NFT_ENDPOINT,
    params={
        "derivation_path": DERIVATION_PATH,
        "secret_recovery_phrase": SECRET_PHRASE,
        "nft_name": NFT_NAME,
        "nft_symbol": NFT_SYMBOL,
        "nft_description": NFT_DESCRIPTION,
        "nft_url": NFT_URI,
        "nft_metadata": json.dumps(NFT_METADATA),
        "network": "devnet",
        "nft_upload_method": "S3"
    },
    headers=HEADERS,
    )
    print(response.json())
