import telebot
from telebot import types
from random import choice

bot = telebot.TeleBot('***')

random_dialog = []

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую тебя, <b><u>{message.from_user. first_name} {message.from_user. last_name}</u></b>! ' \
           f'давай поговорим'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    task = choice(random_dialog)
    fraza = message.text
    random_dialog.append(fraza)
    bot.send_message(message.chat.id, task, parse_mode='html')

# команда принимает фото от пользователя и отвечает ему текстовым сообщением
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
     bot.send_message(message.chat.id, 'Вау крутое фото, ну ты крассава!')



bot.polling(none_stop=True)
