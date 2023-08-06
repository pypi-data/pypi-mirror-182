
from time import time


APP_DATA = {
    "yearn": "0x2B8694ED30082129598720860E8E972F07AA10D9B81CAE16CA0E2CFB24743E24",  # maps to https://bafybeiblq2ko2maieeuvtbzaqyhi5fzpa6vbbwnydsxbnsqoft5si5b6eq.ipfs.dweb.link
    "keep3r": "0x3CCBD83BD785E95FBC5954B9CA8B3D2234C77C178025F52F80D1E0BBA0EEE1F8",  # maps to https://bafybeib4zpmdxv4f5fp3ywkuxhfiwpjcgtdxyf4aex2s7agr4c52b3xb7a.ipfs.dweb.link
}

GNOSIS_SETTLEMENT_ADDRESS = "0x9008D19f58AAbD9eD0D60971565AA8510560ab41"
BASE_URL = "https://protocol-mainnet.gnosis.io/api/v1"
QUOTE_URL = f"{BASE_URL}/feeAndQuote/sell"
ORDERS_URL = f"{BASE_URL}/orders"
DEADLINE = int(time()) + 60 * 60 * 24 * 2  # 2 days
