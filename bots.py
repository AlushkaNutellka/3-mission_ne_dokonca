import telebot

token = '5950809236:AAFkP78oCICMqiO78zCJk39Jqb276RBuZaY'

bot = telebot.TeleBot(token)
# кловиятура
keybord = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# кнопки
button1 = telebot.types.KeyboardButton('Start')
button2 = telebot.types.KeyboardButton('Quit')

# обеденение
keybord.add(button1, button2)


@bot.message_handler(commands=['start', 'privet'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, выберите кнопку',reply_markup=keybord)

    bot.register_next_step_handler(message, check)

def check(message):
    if message.text == 'Yes':
        bot.send_(message.chat.id, 'CAACAgQAAxkBAAEGgCFjfGALIaBjVNorzBQ4OZwu7FIhjgAClRcAAqbxcR4BOaqKL395ICsE')
    elif message.text == 'No':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEGgDVjfGCm1WEyQ7WyEy6pnQF6uerHvwACGRUAAqbxcR54k5QMPt-zJisE')

bot.polling()