import telebot
from telebot import types
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
import requests
import datetime as dt
import xlsxwriter
from tokens import TG_TOKEN
from links import *
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

bot = telebot.TeleBot(TG_TOKEN)

count = 1
logbook = xlsxwriter.Workbook('SinisterBot.xlsx')
logsheet = logbook.add_worksheet()
logsheet.write(0, 0, 'Date')
logsheet.write(0, 1, 'Time')
logsheet.write(0, 2, 'Message type ')
logsheet.write(0, 3, 'User')
logsheet.write(0, 4, 'ID(User)')
logsheet.write(0, 5, 'Message.text')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('📈Курсы валют')
    button2 = types.KeyboardButton('🌥Текущая погода')
    button3 = types.KeyboardButton('Check meta decks')
    button4 = types.KeyboardButton('🎲Roll some dice')
    stop = types.KeyboardButton('🕵️‍Включить режим инкогнито')
    markup.add(button1, button2, button3, button4, stop)
    bot.send_message(message.chat.id,
                     'Привет, *{0.first_name}!*\nПриветствую, данный бот может пригодиться игрокам в *Magic the '
                     'Gathering*, он умеет выдавть топ три метовых колод в выбраном формате.\n'.format(
                         message.from_user), parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '📈Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('💵Курс Доллара')
            item2 = types.KeyboardButton('💶Курс Евро')
            item3 = types.KeyboardButton('㊙Курс Иены')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, '📈Курсы валют', reply_markup=markup)
            log(message)
        elif message.text == '🔙Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('📈Курсы валют')
            button2 = types.KeyboardButton('🌥Текущая погода')
            button3 = types.KeyboardButton('Check meta decks')
            button4 = types.KeyboardButton('🎲Roll some dice')
            stop = types.KeyboardButton('🕵️‍Включить режим инкогнито')
            markup.add(button1, button2, button3, button4, stop)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
            log(message)
        elif message.text == '💵Курс Доллара':
            dollar(message)
            log(message)
        elif message.text == '💶Курс Евро':
            euro(message)
            log(message)
        elif message.text == '㊙Курс Иены':
            jpy(message)
            log(message)
        elif message.text == '🌥Текущая погода':
            full_page = requests.get(WK, headers=headers)
            html = BS(full_page.content, 'html.parser')
            convert = html.findAll("div", {"class": "weather-text"})
            bot.send_message(message.chat.id, convert[0].text)
            log(message)
        elif message.text == 'Check meta decks':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Standard')
            item2 = types.KeyboardButton('Pioneer')
            item3 = types.KeyboardButton('Explorer')
            item4 = types.KeyboardButton('Pauper')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Check meta decks', reply_markup=markup)
            log(message)
        elif message.text == '🎲Roll some dice':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Flip a coin')
            item2 = types.KeyboardButton('Roll d6')
            item3 = types.KeyboardButton('Roll d20')
            back = types.KeyboardButton('🔙Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, '🎲Roll some dice', reply_markup=markup)
            log(message)
        elif message.text == 'Standard':
            bot.send_message(message.chat.id,
                             '"Стандарт" - ротирующийся формат в котором легальны карты из только последних выпусков')
            decks(message, Standard)
            log(message)
        elif message.text == 'Pioneer':
            bot.send_message(message.chat.id,
                             '"Пионер" - неротирующийся формат в котором легальны карты из всех выпусков начиная с "Return to ravnica"')
            decks(message, Pioneer)
            log(message)
        elif message.text == 'Explorer':
            bot.send_message(message.chat.id,
                             '"Исследователь" - неротирующийся, "digital only" формат, в котором легальны карты формата "Пионер" доступные в "MTG Arena"')
            decks(message, Explorer)
            log(message)
        elif message.text == 'Pauper':
            bot.send_message(message.chat.id,
                             '"Бедняк" - неротирующийся формат в котором легальны все карты, когда либо напечатанные с редкостью "Обычная"')
            decks(message, Pauper)
            log(message)

        elif message.text == 'Flip a coin':
            side = str(randint(0, 1))
            if side == "0":
                side = "Орел"
            else:
                side = "Решка"
            bot.send_message(message.chat.id, side)
        elif message.text == 'Flip a coin':
            side = str(randint(0, 1))
            if side == "0":
                side = "Орел"
            else:
                side = "Решка"
            bot.send_message(message.chat.id, side)
        elif message.text == 'Roll d6':
            bot.send_message(message.chat.id, text=str(randint(1, 6)))
        elif message.text == 'Roll d20':
            bot.send_message(message.chat.id, text=str(randint(1, 20)))
        elif message.text == '🕵️‍Включить режим инкогнито':
            logbook.close()


def log(message):
    global count
    logsheet.write(count, 0, str(dt.datetime.now().date()))
    logsheet.write(count, 1, str(dt.datetime.now().time())[0:8])
    logsheet.write(count, 2, 'Текст')
    logsheet.write(count, 3, message.from_user.first_name)
    logsheet.write(count, 4, message.from_user.id)
    logsheet.write(count, 5, message.text)
    count += 1

    print('Строка: ', count)


def dollar(message):
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    bot.send_message(message.chat.id, "Текущий курс: 1 доллар = " + convert[0].text)


def euro(message):
    full_page = requests.get(EURO_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    bot.send_message(message.chat.id, "Текущий курс: 1 евро = " + convert[0].text)


def jpy(message):
    full_page = requests.get(JPY_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    bot.send_message(message.chat.id, "Текущий курс: 1 иена = " + convert[0].text)


def decks(message, Format):
    full_page = requests.get(Format, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    c = soup.find_all('tr', {"class": "tier-1 tier-all"})
    for i in range(3):
        links = c[i].find_next('a')
        deck_name = c[i].find_next('strong')
        deck_percent = c[i].find_next('b')
        price = c[i].find_next('span', {"class": "paper option"})
        bot.send_message(message.chat.id,
                         deck_name['name'] + " Meta: " + deck_percent.text + " Price: " + price.text + "\n" + (
                                 "mtgdecks.net" + links.get("href").replace("\t", "").replace("\n", "")))


if __name__ == '__main__':
    bot.polling(none_stop=True)
