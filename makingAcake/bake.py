def bake_a_cake(batter, temperature, time):
    oven = {
        "type": "electric",
        "model": "GE",
        "volume": 17,
        "contents": None
    }
    oven["contents"] = batter
    oven["temperature"] = temperature

    return f"Your beautiful cake was baked for {time} minutes at {temperature}"
