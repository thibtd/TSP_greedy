#!/usr/bin/env python3
import click


def get_minimum_coins_all_coins(amount):
    """Get the minimum number of coins for a given amount of money"""
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coin_names = {
        2: "2 Euro",
        1: "1 Euro",
        0.5: "50 Cent",
        0.2: "20 Cent",
        0.1: "10 Cent",
        0.05: "5 Cent",
        0.02: "2 Cent",
        0.01: "1 Cent",
    }
    result = {name: 0 for name in coin_names.values()}
    for coin in coins:
        while amount >= coin:
            amount = round(amount - coin, 2)
            result[coin_names[coin]] += 1

    return result


def get_minimum_coins_large(amount):
    """Get the minimum number of coins for a given amount of money using only 2, 1, and 0.5 Euro coins"""
    coins = [2, 1, 0.5]
    coin_names = {
        2: "2 Euro",
        1: "1 Euro",
        0.5: "50 Cent",
    }
    result = {name: 0 for name in coin_names.values()}
    for coin in coins:
        while amount >= coin:
            amount = round(amount - coin, 2)
            result[coin_names[coin]] += 1

    return result


def get_minimum_small_coins(amount):
    """Get the minimum number of coins for a given amount of money using only 0.5, 0.2, 0.1, 0.05, 0.02, and 0.01 Euro coins"""
    coins = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coin_names = {
        0.5: "50 Cent",
        0.2: "20 Cent",
        0.1: "10 Cent",
        0.05: "5 Cent",
        0.02: "2 Cent",
        0.01: "1 Cent",
    }
    result = {name: 0 for name in coin_names.values()}
    for coin in coins:
        while amount >= coin:
            amount = round(amount - coin, 2)
            result[coin_names[coin]] += 1

    return result


# create a command line interface
@click.group()
def cli():
    pass


@cli.command("all_coins")
@click.argument("amount", type=float)
def all_coins(amount):
    """Use all coins, i.e. 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, and 0.01 Euros"""
    coins = get_minimum_coins_all_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    click.echo(f"Minimum coins for {amount} Euros: {coins_non_zero}")


@cli.command("large_coins")
@click.argument("amount", type=float)
def large_coins(amount):
    """Use only large coins, i.e. 2, 1, and 0.5 Euros"""
    coins = get_minimum_coins_large(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    click.echo(f"Minimum large coins for {amount} Euros: {coins_non_zero}")


@cli.command("small_coins")
@click.argument("amount", type=float)
def small_coins(amount):
    """Use only small coins, i.e. 50cents and below"""
    coins = get_minimum_small_coins(amount)
    coins_non_zero = {key: value for key, value in coins.items() if value > 0}
    click.echo(f"Minimum small coins for {amount} Euros: {coins_non_zero}")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
