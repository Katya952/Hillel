import json
import random
from argparse import ArgumentParser

# Creating file config.json
# with open('config.json', 'w') as file:
#     json.dump({
#         "delta": 0.5,
#         "exchange_rate": 26.00,
#         "UAH": 10000.00,
#         "USD": 0.00
#     }, file)

# Creating file history.json
# with open('history.json', 'w') as file:
#     json.dump({
#         "exchange_rate": config_data.get('exchange_rate'),
#         "UAH": config_data.get('UAH'),
#         "USD": config_data.get('USD')
#     }, file)


def round_float(value):
    rounded_value = int(100 * value) / 100
    return rounded_value


def rewrite_balance(balance_uah, balance_usd):
    with open('history.json', 'w') as file:
        json.dump({
            "exchange_rate": history_data.get('exchange_rate'),
            "UAH": balance_uah,
            "USD": balance_usd
        }, file)


def return_rate():
    """
    Find current exchange rate.
    :return: current exchange rate
    """
    exchange_rate = history_data.get('exchange_rate')
    return exchange_rate


def available_balance():
    """
    Information about money on the accounts.
    :return: account balance USD and UAH
    """
    with open('history.json', 'r') as jsonfile:
        history_data = json.load(jsonfile)
    account_balance = f'UAH {history_data.get("UAH")}, USD {history_data.get("USD")}'
    return account_balance


def buy_currency(amount_to_exchange):
    """
    Exchange UAH for USD. If there are not enough money for buying, show message like UNAVAILABLE, REQUIRED BALANCE
    UAH 2593.00, AVAILABLE 1000.00
    add to history.json new data
    :param amount_to_exchange: amount of USD need to buy
    :return: new account balance
    """
    if amount_to_exchange == 'ALL':
        balance_usd = history_data.get('USD') + round_float(history_data.get('UAH') / history_data.get('exchange_rate'))
        balance_usd = round_float(balance_usd)
        balance_uah = history_data.get('UAH') - (balance_usd - history_data.get('USD')) \
                      * history_data.get('exchange_rate')
        balance_uah = round_float(balance_uah)
        rewrite_balance(balance_uah, balance_usd)
    elif float(amount_to_exchange) * history_data.get('exchange_rate') <= history_data.get('UAH'):
        balance_usd = history_data.get('USD') + float(amount_to_exchange)
        balance_usd = round_float(balance_usd)
        balance_uah = history_data.get('UAH') - float(amount_to_exchange) * history_data.get('exchange_rate')
        balance_uah = round_float(balance_uah)
        rewrite_balance(balance_uah, balance_usd)
    else:
        av_usd = history_data.get('UAH') / history_data.get('exchange_rate')
        av_usd = round_float(av_usd)
        return f"UNAVAILABLE, REQUIRED BALANCE UAH {history_data.get('UAH')}, AVAILABLE SUM TO BUY {av_usd}"
    return f"UAH {balance_uah}, USD {balance_usd}"


def sell_currency(amount_to_exchange):
    """
    Exchange USD for UAH. If there are not enough money for buying, show message like UNAVAILABLE, REQUIRED BALANCE
    USD 200.00, AVAILABLE 135.00
    add to history.json new data
    :param amount_to_exchange: amount of USD need to sell
    :return: new account balance
    """
    if amount_to_exchange == 'ALL':
        balance_usd = 0
        balance_uah = history_data.get('UAH') + history_data.get('USD') * history_data.get('exchange_rate')
        balance_uah = round_float(balance_uah)
        rewrite_balance(balance_uah, balance_usd)
    elif float(amount_to_exchange) <= history_data.get('USD'):
        balance_usd = history_data.get('USD') - float(amount_to_exchange)
        balance_usd = round_float(balance_usd)
        balance_uah = history_data.get('UAH') + float(amount_to_exchange) * history_data.get('exchange_rate')
        balance_uah = round_float(balance_uah)
        rewrite_balance(balance_uah, balance_usd)
    else:
        return f"UNAVAILABLE, REQUIRED BALANCE USD {history_data.get('USD')}, AVAILABLE SUM TO " \
               f"SELL {history_data.get('USD')}"
    return f"UAH {balance_uah}, USD {balance_usd}"


def generate_new_rate():
    """
    To create new exchange rate in diapason exchange_rate - delta < new_exchange_rate < exchange_rate + delta and add
    it to history.json
    :return: new exchange rate
    """
    new_exchange_rate = history_data.get('exchange_rate') \
                        + random.uniform(-1 * (config_data.get('delta')), (config_data.get('delta')))
    new_exchange_rate = round_float(new_exchange_rate)
    with open('history.json', 'w') as file:
        json.dump({
            "exchange_rate": new_exchange_rate,
            "UAH": history_data.get('UAH'),
            "USD": history_data.get('USD')
        }, file)
    return new_exchange_rate


def restart_app():
    """
    Copy data from config.json in history.json
    :return: file history.json
    """
    with open('history.json', 'w') as file:
        json.dump({
            "exchange_rate": config_data.get('exchange_rate'),
            "UAH": config_data.get('UAH'),
            "USD": config_data.get('USD')
        }, file)
    return


if __name__ == "__main__":

    with open('config.json', 'r') as jsonfile:
        config_data = json.load(jsonfile)

    with open('history.json', 'r') as jsonfile:
        history_data = json.load(jsonfile)

    args = ArgumentParser()

    args.add_argument("function", type=str)
    args.add_argument("amount_to_exchange", type=str, nargs='?', default='')

    args = vars(args.parse_args())

    function = args['function']
    amount_to_exchange = args['amount_to_exchange']

    if function == 'RATE':
        print(return_rate())
    elif function == 'AVAILABLE':
        print(available_balance())
    elif function == 'BUY':
        print(buy_currency(amount_to_exchange))
    elif function == 'SELL':
        print(sell_currency(amount_to_exchange))
    elif function == 'NEXT':
        print(generate_new_rate())
    elif function == 'RESTART':
        restart_app()
    else:
        print(f"Error. Try other command!")
