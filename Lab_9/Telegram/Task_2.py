import telebot
import datetime
from tokens import TG_TOKEN


bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я могу подсказать вам текущие дату и время!")


@bot.message_handler(commands=['help'])
def bothelp(message):
    bot.send_message(message.chat.id, "Ввдите '/time' чтобы узнать текущее время или '/date', чтобы узнать текущую дату.")


@bot.message_handler(commands=['time'])
def check_time(message):
    bot.send_message(message.chat.id, datetime.datetime.now().strftime("%X"))


@bot.message_handler(commands=['date'])
def check_date(message):
    bot.send_message(message.chat.id, datetime.datetime.now().strftime("%A, %d, %B, %Y"))


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, "Извините ни чем не могу вам помочь")


bot.polling(none_stop=True)
