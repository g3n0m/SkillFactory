# библиотека для форматирования полученных данных без лишних символов и знаков
import json

# библиотека для отправки запросов на сторонние сайты
import requests

# импортируем из стороннего сайта (Б - безопасность) словарь валют и TOKEN
from config import currency


# конструктор обработок ошибок, метод обработки try-except (после возникновения ошибки мы можем продолжать работу)
class APIException(Exception):
    pass


# класс обработки ошибок
class CurConvert:

    # декоратор передачи переменных (в нашем случае base, quote, amount)
    @staticmethod
    def price_get(base, quote, amount):

        # присвоение переменной base_key значения из слованя по ключу base и перевод значения в нижний регистр
        try:
            base_key = currency[base.lower()]

        # ошибка, вызванная значением переменных
        except KeyError:

            # описание ошибки
            raise APIException(f'Валюта {base} не найдена!')

        # присвоение переменной quote_key значение из словаря по ключу quote и перевод значения в нижний регистр
        try:
            quote_key = currency[quote.lower()]

        # ошбика, выфзванная значением переменных
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена!')

        # обработка ситуации, когда для конвертации дважды использовалась одна и та же валюта
        if base_key == quote_key:
            raise APIException(f'Невозможно конвертировать одинаковую валюту {base}!')

        # перевод переменной значения кол-ва валюты в число с точкой
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        # присвоение переменной сформированного get запроса с использованием значений base_key и quote_key
        rg = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')

        # обработка ответа от API, очистка его от лишних символов
        answer = json.loads(rg.content)

        # получение числового значения валюты по ключу из словаря answer
        price_value = answer[quote_key] * amount

        # ответ нашего бота с использованием полученных ранее переменных и значений
        result = f'Конвертация по курсу: {amount} {base} = {price_value} {quote}'

        # возможность обращаться к переменно result из других мест, не только из данной функции
        return result
