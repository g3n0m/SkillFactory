import telebot
from config import TOKEN, currency
from lib import APIException, CurConvert

bot = telebot.TeleBot(TOKEN)


# декоратор реагирует на команды пользователя в чате при взаимодействии с ботом
@bot.message_handler(commands=['currency'])
def values(message: telebot.types.Message):

    # в ответ на обращение /currency вывести доступный список (из словаря) валют по ключу keys
    # и объединение значений в одну строку
    answer_text = 'Какая валюта Вас интересует?'
    for v in currency.keys():
        answer_text = '\n'.join((answer_text, v))

    # ответ бота к предыдущему сообщеню в чате
    bot.reply_to(message, answer_text)


# реакция бота на команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    answer_text = 'Для конвертацию введите следующую команду \n \
<имя валюты> <в какую валюты конвертировать> <кол-во> \n \
Вывести список доступных валют: /currency'
    bot.reply_to(message, answer_text)


# реакция бота на текст сообщения
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    # присвоение переменной значения раздробленного (split()) ответа
    value = message.text.split()
    try:

        # проверка на кол-во и правильность введенного запроса пользователем
        if len(value) != 3:
            raise APIException('Запрос содержит не верное кол-по параметров!')

        # присвоение переменной значения, для удаления лишних скобок, запятых и прочих знаков
        result = CurConvert.price_get(*value)
    except APIException as error:
        bot.reply_to(message, f'Ошибка в команде:\n{error}')
    else:
        # бот отвечается на сообщение без цитаты
        bot.send_message(message.chat.id, result)


# запуск бота без остановки, даже в случае возникновения ошибки
bot.polling(non_stop=True)
