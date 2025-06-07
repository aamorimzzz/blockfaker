import re
from blockfaker import generate_token_contract, fake_volume, generate_wallet_address


def test_generate_wallet_address():
    addr = generate_wallet_address()
    assert isinstance(addr, str)
    assert re.fullmatch(r"0x[0-9a-fA-F]{40}", addr)


def test_generate_token_contract_defaults():
    token = generate_token_contract()
    assert set(token) == {"name", "symbol", "decimals", "total_supply", "address"}
    assert token["decimals"] == 18
    assert re.fullmatch(r"0x[0-9a-fA-F]{40}", token["address"])


def test_fake_volume_length_and_range():
    records = fake_volume(days=10, min_volume=100, max_volume=200)
    assert len(records) == 10
    for record in records:
        assert 100 <= record["volume"] <= 200
        assert "date" in record

