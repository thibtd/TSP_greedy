from greedy_coin import (
    get_minimum_coins_all_coins,
    get_minimum_coins_large,
    get_minimum_small_coins,
)


def test_get_minimum_coins_all_coins():
    amount = 2.5
    coins = get_minimum_coins_all_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"2 Euro": 1, "50 Cent": 1}

    amount = 4
    coins = get_minimum_coins_all_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"2 Euro": 2}

    amount = 0.42
    coins = get_minimum_coins_all_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"20 Cent": 2, "2 Cent": 1}


def test_get_minimum_coins_large():
    amount = 3.5
    coins = get_minimum_coins_large(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"2 Euro": 1, "1 Euro": 1, "50 Cent": 1}

    amount = 4
    coins = get_minimum_coins_large(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"2 Euro": 2}

    amount = 1.5
    coins = get_minimum_coins_large(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"1 Euro": 1, "50 Cent": 1}

    amount = 0.5
    coins = get_minimum_coins_large(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"50 Cent": 1}


def test_get_minimum_coins_small():
    amount = 3.5
    coins = get_minimum_small_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"50 Cent": 7}

    amount = 1.43
    coins = get_minimum_small_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"50 Cent": 2, "20 Cent": 2, "2 Cent": 1, "1 Cent": 1}

    amount = 0.5
    coins = get_minimum_small_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"50 Cent": 1}

    amount = 0.07
    coins = get_minimum_small_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    assert coins_non_zero == {"5 Cent": 1, "2 Cent": 1}
