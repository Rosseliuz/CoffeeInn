import telebot
from telebot import types

bot = telebot.TeleBot('7885124101:AAHW2WovzEOIif18n2qA34DGgPVNmPc9Iag')
count = 0


@bot.message_handler(commands=['start'])
def handle_syrups(callback):
    text = callback.message.text
    print(text)


def handle_sugar(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Нет, продолжить', callback_data='next'))
    markup.add(types.InlineKeyboardButton('Да, добавить', callback_data='sugar'))
    bot.send_message(message.chat.id, 'Хотите добавить сахар?:', reply_markup=markup)