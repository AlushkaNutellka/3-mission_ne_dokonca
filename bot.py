import telebot
import requests
from bs4 import BeautifulSoup as b

URL = 'https://kaktus.media/?lable=8&date=2022-11-23&order=time'
TOKEN = '5955058809:AAGNL4vkhY7hPCtuv6oWFGQKxoPR9vHoq6Q'


keybord = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button = telebot.types.KeyboardButton('Выход')
bot = telebot.TeleBot(TOKEN)

keybord.add(button)
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    tel = soup.find_all('div', class_='Tag--Articles')
    return [c.text for c in tel]

@bot.message_handler(content_types=['Выход'])
def check(message):
    if message.text == 'Выход':
        message.text, 'До свидание'
    else:
        message


list_of_jokes = parser(URL)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','go','hello'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет,выберите число от 1 до 20: ')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите только цифру: ')

def photo(message):
    bot.send_photo(message.chat.id,'Tag--Articles')


bot.polling()