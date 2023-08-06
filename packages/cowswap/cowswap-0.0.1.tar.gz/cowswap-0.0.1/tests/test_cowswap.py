
from cowswap import get_quote
from pytest import raises

dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

def test_get_quote():
    amount = 1e18 * 100
    with raises(TypeError):
        # must pass in an integer
        get_quote(dai, weth, amount)

    quote = get_quote(dai, weth, int(amount))
    print(quote)
    assert quote
