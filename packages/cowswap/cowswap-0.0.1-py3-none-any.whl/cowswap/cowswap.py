
import json
import requests
from decimal import Decimal
from typing import Optional, Tuple

import eth_retry
from ape_safe import ApeSafe

from cowswap._constants import QUOTE_URL, ORDERS_URL, DEADLINE, APP_DATA, GNOSIS_SETTLEMENT_ADDRESS
from cowswap._types import Address, OrderPayload
from cowswap.exceptions import SellAmountDoesNotCoverFee


@eth_retry.auto_retry  # type: ignore
def get_quote(
    sell_token: Address,
    buy_token: Address,
    amount: int,
) -> Tuple[float, float]:
    """ Returns a tuple (buy_amount_after_fee_with_slippage, fee_amount) """
    if not isinstance(amount, int):
        raise TypeError(f"`amount` must be an integer. You passed a {amount.__class__.__name__}")

    # get the fee + the buy amount after fee
    quote_params = {"sellToken": sell_token, "buyToken": buy_token, "sellAmountBeforeFee": Decimal(amount)}
    r = requests.get(QUOTE_URL, params=quote_params)  # type: ignore

    # If request failed, raise appropriate Exception
    if not (r.ok and r.status_code == 200):
        response = r.json()
        if "errorType" in response:
            if response["errorType"] == "SellAmountDoesNotCoverFee":
                raise SellAmountDoesNotCoverFee({"amount": amount, "fee_amount": int(response["data"]["fee_amount"], 16)})
        # If we don't have err-specific handling, raise generic exception
        raise ValueError(f"Request for quote failed, response: {response}")
    
    # these two values are needed to create an order
    fee_amount = int(r.json()["fee"]["amount"])
    buy_amount_after_fee = int(r.json()["buyAmountAfterFee"])
    buy_amount_after_fee_with_slippage = int(buy_amount_after_fee * 0.99)  # 1% slippage. Website default is 0.05%
    return buy_amount_after_fee_with_slippage, fee_amount


def prepare_order_payload(
    safe: ApeSafe,
    sell_token: Address,
    buy_token: Address,
    amount: int,
    receiver: Optional[str] = None,
    deadline: int = DEADLINE,
    app_data: str = APP_DATA["yearn"],
) -> OrderPayload:
    if receiver is None:
        receiver = safe.address

    buy_amount_after_fee_with_slippage, fee_amount = get_quote(sell_token, buy_token, amount)
    assert fee_amount > 0, f"Fee should not be less than zero. Fee: {fee_amount}"
    assert buy_amount_after_fee_with_slippage > 0, f"Buy amount after fees and slippage should not be less than zero. Buy amount: {buy_amount_after_fee_with_slippage}"

    return {
        "sellToken": sell_token,
        "buyToken": buy_token,
        "sellAmount": str(amount - fee_amount),  # amount that we have minus the fee we have to pay
        "buyAmount": str(buy_amount_after_fee_with_slippage),  # buy amount fetched from the previous call
        "validTo": deadline,
        "appData": app_data,
        "feeAmount": str(fee_amount),
        "kind": "sell",
        "partiallyFillable": False,
        "receiver": receiver,
        "signature": safe.address,
        "from": safe.address,
        "sellTokenBalance": "erc20",
        "buyTokenBalance": "erc20",
        "signingScheme": "presign",  # Very important. this tells the api you are going to sign on chain
    }


@eth_retry.auto_retry  # type: ignore
def submit_sell_order(
    safe: ApeSafe,
    sell_token: Address,
    buy_token: Address,
    amount: int,
    receiver: Optional[str] = None,
    deadline: int = DEADLINE,
    app_data: str = APP_DATA["yearn"],
) -> None:
    order_payload = prepare_order_payload(safe, sell_token, buy_token, amount, receiver=receiver, deadline=deadline, app_data=app_data)

    r = requests.post(ORDERS_URL, json=order_payload)

    if not r.ok and r.status_code == 201:
        raise ValueError(f"Order submission failed, response: {r.json()}")

    order_uid = r.json()
    print("Payload:", json.dumps(order_payload, indent=2))
    print("Order uid:", json.dumps(order_uid, indent=2))
    
    # contract used to sign the order
    gnosis_settlement = safe.contract(GNOSIS_SETTLEMENT_ADDRESS)
    
    # with the order id, we set the flag, basically signing as the gnosis safe.
    gnosis_settlement.setPreSignature(order_uid, True)
