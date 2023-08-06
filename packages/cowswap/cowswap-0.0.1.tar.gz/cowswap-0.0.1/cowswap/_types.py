
from typing import TypedDict, Literal


Address = str

OrderPayload = TypedDict("OrderPayload", {
    "sellToken": Address,
    "buyToken": Address,
    "sellAmount": str,
    "buyAmount": str,
    "validTo": int,
    "appData": str,
    "feeAmount": str,
    "kind": Literal["sell"],
    "partiallyFillable": bool,
    "receiver": Address,
    "signature": str,
    "from": Address,
    "sellTokenBalance": Literal["erc20"],
    "buyTokenBalance": Literal["erc20"],
    "signingScheme": Literal["presign"],
})
