import random
import secrets
import string
import datetime

__all__ = [
    "generate_wallet_address",
    "generate_token_contract",
    "fake_volume",
]

def generate_wallet_address() -> str:
    """Generate a random Ethereum-style wallet address."""
    return "0x" + secrets.token_hex(20)

def generate_token_contract(
    name: str | None = None,
    symbol: str | None = None,
    decimals: int = 18,
    total_supply: int | None = None,
) -> dict:
    """Generate fake token contract information.

    Parameters
    ----------
    name: optional token name. Random if not provided.
    symbol: optional ticker symbol. Random if not provided.
    decimals: token decimals. Defaults to 18.
    total_supply: total supply of tokens. Random if not provided.
    """
    name = name or "Token" + ''.join(random.choices(string.ascii_uppercase, k=5))
    symbol = symbol or ''.join(random.choices(string.ascii_uppercase, k=4))
    if total_supply is None:
        total_supply = random.randint(1_000_000, 1_000_000_000)
    return {
        "name": name,
        "symbol": symbol,
        "decimals": decimals,
        "total_supply": total_supply,
        "address": generate_wallet_address(),
    }

def fake_volume(
    days: int = 30,
    min_volume: int = 1_000,
    max_volume: int = 100_000,
) -> list[dict]:
    """Generate fake daily volume data.

    Returns a list of dictionaries with ``date`` and ``volume`` keys.
    """
    today = datetime.date.today()
    records = []
    for i in range(days):
        day = today - datetime.timedelta(days=days - i - 1)
        volume = random.randint(min_volume, max_volume)
        records.append({"date": day.isoformat(), "volume": volume})
    return records
