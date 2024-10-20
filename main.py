import telebot
from telebot import types

bot = telebot.TeleBot('7885124101:AAHW2WovzEOIif18n2qA34DGgPVNmPc9Iag')
volume = 0

@bot.message_handler(commands=['start'])
def main(message):
    photo = open('menu.jpg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Меню', callback_data='menu'))
    markup.add(types.InlineKeyboardButton('Как добраться', callback_data='map'))
    markup.add(types.InlineKeyboardButton('Помощь', callback_data='help'))
    bot.send_photo(message.chat.id, photo, caption='Здравствуйте! Я бот-мессенджер "Coffee inn" и я помогу Вам сделать заказ!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def count():

def callback_msg(callback):
    global volume
    if callback.data == 'menu':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Кофе', callback_data='coffee')
        btn2 = types.InlineKeyboardButton('Напитки', callback_data='drinks')
        btn3 = types.InlineKeyboardButton('Ланч', callback_data='lunch')
        btn4 = types.InlineKeyboardButton('Десерты', callback_data='desserts')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(callback.message.chat.id, 'Выберите категорию:', reply_markup=markup)
    if callback.data == 'coffee':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('На классическом молоке', callback_data='classic'))
        markup.add(types.InlineKeyboardButton('На растительном молоке', callback_data='plant'))
        markup.add(types.InlineKeyboardButton('Без кофеина', callback_data='without'))
        bot.send_message(callback.message.chat.id, 'Выберите категорию:', reply_markup=markup)
    if callback.data == 'classic' or callback.data == 'without':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Эспрессо', callback_data='espresso')
        btn2 = types.InlineKeyboardButton('Американо', callback_data='american')
        btn3 = types.InlineKeyboardButton('Капучино', callback_data='cappuccino')
        btn4 = types.InlineKeyboardButton('Латте', callback_data='latte')
        btn5 = types.InlineKeyboardButton('Флэт Уайт', callback_data='flat')
        btn6 = types.InlineKeyboardButton('Гляссе', callback_data='glasse')
        btn7 = types.InlineKeyboardButton('Мокко', callback_data='mocha')
        btn8 = types.InlineKeyboardButton('Венский', callback_data='viennese')
        btn9 = types.InlineKeyboardButton('Раф', callback_data='raf')
        btn10 = types.InlineKeyboardButton('Чиз', callback_data='cheese')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn6)
        markup.row(btn7, btn8)
        markup.row(btn9, btn10)
        bot.send_message(callback.message.chat.id, 'Выберите кофе:', reply_markup=markup)
    if callback.data == 'plant':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Кокосовое', callback_data='coconut'))
        markup.add(types.InlineKeyboardButton('Миндальное', callback_data='almond'))
        bot.send_message(callback.message.chat.id, 'Выберите вид молока:', reply_markup=markup)
    if callback.data == 'coconut' or callback.data == 'almond':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Капучино', callback_data='cappuccino'))
        markup.add(types.InlineKeyboardButton('Латте', callback_data='latte'))
        markup.add(types.InlineKeyboardButton('Флэт Уайт', callback_data='flat'))
        bot.send_message(callback.message.chat.id, 'Выберите кофе:', reply_markup=markup)
    if callback.data == 'drinks':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Какао', callback_data='cocoa')
        btn2 = types.InlineKeyboardButton('Глинтвейн', callback_data='mulled')
        btn3 = types.InlineKeyboardButton('Молочный коктейль', callback_data='milkshake')
        btn4 = types.InlineKeyboardButton('Чай', callback_data="tea")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(callback.message.chat.id, 'Выберите напиток:', reply_markup=markup)
    if callback.data == 'lunch':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Сэндвич', callback_data='sandwich')
        btn2 = types.InlineKeyboardButton('Бурито', callback_data='burrito')
        btn3 = types.InlineKeyboardButton('Блины', callback_data='pancakes')
        markup.row(btn1, btn2, btn3)
        bot.send_message(callback.message.chat.id, 'Выберите ланч:', reply_markup=markup)
    if callback.data == 'desserts':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Горячий шоколад', callback_data='hot_chocolate')
        btn2 = types.InlineKeyboardButton('Сырники по-венски', callback_data='cheesecakes')
        btn3 = types.InlineKeyboardButton('Трубочка со сгущёнкой', callback_data='tube')
        btn4 = types.InlineKeyboardButton('Мороженое', callback_data='ice_cream')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_message(callback.message.chat.id, 'Выберите десерт:', reply_markup=markup)
    if callback.data == "espresso":
        markup = types.InlineKeyboardMarkup()
        volume = 0
        btn1 = types.InlineKeyboardButton('40', callback_data='fourty')
        btn2 = types.InlineKeyboardButton('80', callback_data='eighty')
        markup.row(btn1, btn2)
        bot.send_message(callback.message.chat.id, 'Выберите объём(мл)', reply_markup=markup)
    if callback.data == "fourty":
        volume = 40
        print(volume)
        bot.send_message(callback.message.chat.id, 'Укажите количество порций (числом):')
    elif callback.data == "eighty":
        volume = 80
        print(volume)
        bot.send_message(callback.message.chat.id, 'Укажите количество порций (числом):')


bot.polling(none_stop=True)