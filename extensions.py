import json
import requests
from config import currency


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_key = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_key = currency[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}")
        total_base = json.loads(r.content)[currency[base]]

        return total_base
