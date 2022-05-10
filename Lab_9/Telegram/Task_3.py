from random import randint
import time
import telebot
from telebot import types
from random import randint
from tokens import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dice = types.KeyboardButton('Dice')
    timer = types.KeyboardButton('Timer')
    markup.add(dice, timer)
    bot.send_message(message.chat.id, 'Что вам нужно?', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.text == 'Dice':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        d6 = types.KeyboardButton('roll d6')
        d12 = types.KeyboardButton('roll 2*d6')
        d20 = types.KeyboardButton('roll d20')
        b = types.KeyboardButton('back')
        markup.add(d6, d12, d20, b)
        bot.send_message(message.chat.id, 'Dice', reply_markup=markup)
    elif message.text == 'roll d6':
        bot.send_message(message.chat.id, text=str(randint(1, 6)))
    elif message.text == 'roll 2*d6':
        bot.send_message(message.chat.id, text=str(randint(1, 6)) + "  " + str(randint(1, 6)))
    elif message.text == 'roll d20':
        bot.send_message(message.chat.id, text=str(randint(1, 20)))
    elif message.text == 'Timer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        w30 = types.KeyboardButton('30 секунд')
        w1 = types.KeyboardButton('1 минута')
        w5 = types.KeyboardButton('5 минут')
        b = types.KeyboardButton('back')
        markup.add(w30, w1, w5, b)
        bot.send_message(message.chat.id, 'Timer', reply_markup=markup)
    elif message.text == '30 секунд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton('Остановить таймер')
        bot.send_message(message.chat.id, 'Засек 30 секунд', reply_markup=markup)
        set_timer(30)
        bot.send_message(message.chat.id, 'Время вышло', reply_markup=markup)
    elif message.text == '1 минута':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton('Остановить таймер')
        bot.send_message(message.chat.id, 'Засек 1 минуту', reply_markup=markup)
        set_timer(60)
        bot.send_message(message.chat.id, 'Время вышло', reply_markup=markup)
    elif message.text == '5 минут':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton('Остановить таймер')
        bot.send_message(message.chat.id, 'Засек 5 минут', reply_markup=markup)
        set_timer(300)
        bot.send_message(message.chat.id, 'Время вышло', reply_markup=markup)
    elif message.text == 'back':
        start(message)
    elif message.text == 'Остановить таймер':
        message.text = 'Timer'
        bot_message(message)


def set_timer(a):
    for i in range(a):
        time.sleep(1)


@bot.message_handler(commands=['help'])
def bothelp(message):
    bot.send_message(message.chat.id, "Используйте кнопки")


bot.polling(none_stop=True)
