import telebot
from tokens import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


@bot.message_handler(commands=['help'])
def bothelp(message):
    bot.send_message(message.chat.id, "Я пока не умею помогать... Я только ваше эхо.")


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, "Я получил сообщение: " + '"' + message.text + '"')


bot.polling(none_stop=True)
