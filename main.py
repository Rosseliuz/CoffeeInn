import telebot
from telebot import types
from count import handle_sugar
from syrups import list_of_syrup

bot = telebot.TeleBot('7885124101:AAHW2WovzEOIif18n2qA34DGgPVNmPc9Iag')
volume = 0
count_of_sugar = 0
type_of_cof = ''
coffee = ''
price = 0
final_price = 0
count = 0
order = ''
table_info = ''
temp_final_price = 0
marshmallows = False
text_of_syrup = ''
count_of_syrup = 0


@bot.message_handler(commands=['start'])
def main(message):
    photo = open('menu.png', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Меню', callback_data='menu'))
    markup.add(types.InlineKeyboardButton('Как добраться', callback_data='map'))
    markup.add(types.InlineKeyboardButton('Помощь', callback_data='help'))
    bot.send_photo(message.chat.id, photo, caption='Здравствуйте! Я бот-мессенджер "Coffee inn" и я помогу Вам сделать заказ!', reply_markup=markup)


def handle_count(message):
    global count
    count = message.text
    print(f'Количество позиции:' + count)


@bot.callback_query_handler(func=lambda callback: True)
def callback_msg(callback):
    global volume, count, type_of_cof, coffee, count_of_sugar, price, final_price, order, table_info, temp_final_price, marshmallows, text_of_syrup, count_of_syrup
    if callback.data == 'menu' or callback.data == 'back-end':
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
        if callback.data == 'classic':
            price = 0
            type_of_cof = 'На классическом молоке'
            print(type_of_cof)
        elif callback.data == 'without':
            price = 0
            price += 60
            type_of_cof = 'Без кофеина'
            print(type_of_cof)

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
        price = 0
        price += 60
        type_of_cof = 'На растительном молоке'
        print(type_of_cof)
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
        coffee = 'Эспрессо'
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('40', callback_data='fourty')
        btn2 = types.InlineKeyboardButton('80', callback_data='eighty')
        markup.row(btn1, btn2)
        bot.send_message(callback.message.chat.id, 'Выберите объём(мл)', reply_markup=markup)
    if callback.data == "fourty":
        volume = 40
        print(f'Желаемый объём:' + str(volume))
        bot.send_message(callback.message.chat.id, 'Укажите количество порций (числом):')
        bot.register_next_step_handler(callback.message, handle_count)
        bot.register_next_step_handler(callback.message, handle_sugar)
    elif callback.data == "eighty":
        volume = 80
        print(volume)
        bot.send_message(callback.message.chat.id, 'Укажите количество порций (числом):')
    if callback.data == 'sugar':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='one')
        btn2 = types.InlineKeyboardButton('2', callback_data='two')
        btn3 = types.InlineKeyboardButton('3', callback_data='three')
        markup.row(btn1, btn2, btn3)
        bot.send_message(callback.message.chat.id, 'Сколько Вы хотите добавить ложек сахара?:', reply_markup=markup)
    if callback.data == 'one' or callback.data == 'two' or callback.data == 'three' or callback.data == 'next':
        if callback.data == 'one':
            count_of_sugar = 1
            print(count_of_sugar)
        elif callback.data == 'two':
            count_of_sugar = 2
            print(count_of_sugar)
        elif callback.data == 'three':
            count_of_sugar = 3
            print(count_of_sugar)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Нет, продолжить', callback_data='next-clause'))
        markup.add(types.InlineKeyboardButton('Добавить маршмеллоу', callback_data='add_marshmallows'))
        markup.add(types.InlineKeyboardButton('Добавить сироп', callback_data='add_syrup'))
        bot.send_message(callback.message.chat.id, 'Хотите добавить маршмеллоу или сироп?:', reply_markup=markup)



    if callback.data == 'next-clause':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, добавить', callback_data='preorder'))
        markup.add(types.InlineKeyboardButton('Добавить маршмеллоу', callback_data='add_marshmallows'))
        markup.add(types.InlineKeyboardButton('Добавить сироп', callback_data='add_syrup'))
        markup.add(types.InlineKeyboardButton('Нет, отменить', callback_data='back-end'))
        if volume == 40:
            price = 130
            if type_of_cof == 'Без кофеина' or type_of_cof == 'На растительном молоке':
                final_price = (price * int(count)) + count_of_syrup + 60
            else:
                final_price = (price * int(count)) + count_of_syrup
        elif volume == 80:
            price = 160
            if type_of_cof == 'Без кофеина' or type_of_cof == 'На растительном молоке':
                final_price = price * int(count)
            else:
                final_price = price * int(count)
        if marshmallows:
            if count_of_sugar != 0:
                bot.send_message(callback.message.chat.id,
                                 'Вы уверены, что хотите добавить следующую позицию в заказ?:\n\n' + f'{type_of_cof} {coffee} {volume}' + f' мл Сахар x {count_of_sugar} Маршмеллоу {text_of_syrup}' + f'------ {count} ' + 'x ' + f'{price} = {final_price}',
                                 reply_markup=markup)
            else:
                bot.send_message(callback.message.chat.id,
                                 'Вы уверены, что хотите добавить следующую позицию в заказ?:\n\n' + f'{type_of_cof} {coffee} {volume}' + f' мл Маршмеллоу {text_of_syrup}' + f'------ {count} ' + 'x ' + f'{price} = {final_price}',
                                 reply_markup=markup)
        else:
            if count_of_sugar != 0:
                bot.send_message(callback.message.chat.id,
                                 'Вы уверены, что хотите добавить следующую позицию в заказ?:\n\n' + f'{type_of_cof} {coffee} {volume}' + f' мл Сахар x {count_of_sugar} {text_of_syrup}' + f'------ {count} ' + 'x ' + f'{price} = {final_price}',
                                 reply_markup=markup)
            else:
                bot.send_message(callback.message.chat.id,
                                 'Вы уверены, что хотите добавить следующую позицию в заказ?:\n\n' + f'{type_of_cof} {coffee} {volume}' + f' мл {text_of_syrup}' + f'------ {count} ' + 'x ' + f'{price} = {final_price}',
                                 reply_markup=markup)



    if callback.data == 'preorder':
        order += f'{type_of_cof} {coffee} {volume}' +' мл ' + f'------ {count} ' + 'x ' + f'{price} = {final_price}\n'
        temp_final_price = final_price
        if marshmallows:
            table_info += f'{type_of_cof} {coffee}{volume}x{count} Сахарx{count_of_sugar} Маршмеллоу {text_of_syrup}\n'
        else:
            table_info += f'{type_of_cof} {coffee}{volume}x{count} Сахарx{count_of_sugar} {text_of_syrup}\n'
        print(order)
        print(table_info)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Сформировать заказ', callback_data='order'))
        markup.add(types.InlineKeyboardButton('В начале меню', callback_data='menu'))
        bot.send_message(callback.message.chat.id, 'Позиция успешно добавлена!', reply_markup=markup)
        count_of_sugar = 0
        final_price = 0
        coffee = ''
        count = 0
        marshmallows = False
        text_of_syrup = ''
        count_of_syrup = 0

    # Добавление маршмеллоу
    if callback.data == 'add_marshmallows':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти к добавлению позиции в заказ', callback_data='next-clause'))
        if marshmallows:
            bot.send_message(callback.message.chat.id, 'Маршмеллоу уже были добавлены!', reply_markup=markup)
        else:
            marshmallows = True
            count_of_syrup += 25
            bot.send_message(callback.message.chat.id, 'Маршмеллоу успешно добавлены!', reply_markup=markup)

    # Добавление сиропов
    if callback.data == 'add_syrup':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Айриш крим', callback_data='irish_cream')
        btn2 = types.InlineKeyboardButton('Клиновый', callback_data='wedge')
        btn3 = types.InlineKeyboardButton('Голубой кюрасао', callback_data='blue_curacao')
        btn4 = types.InlineKeyboardButton('Облепиха', callback_data='sea_buckthorn')
        btn5 = types.InlineKeyboardButton('Бабл гам', callback_data='bubble_gum')
        btn6 = types.InlineKeyboardButton('Апельсин', callback_data='orange')
        btn7 = types.InlineKeyboardButton('Шоколад', callback_data='chocolate')
        btn8 = types.InlineKeyboardButton('Гранат', callback_data='pomegranate')
        btn9 = types.InlineKeyboardButton('Лаванда', callback_data='lavender')
        btn10 = types.InlineKeyboardButton('Персик', callback_data='peach')
        btn11 = types.InlineKeyboardButton('Киви', callback_data='kiwi')
        btn12 = types.InlineKeyboardButton('Имбирь', callback_data='ginger')
        btn13 = types.InlineKeyboardButton('Миндаль', callback_data='almond')
        btn14 = types.InlineKeyboardButton('Кокос', callback_data='coconut')
        btn15 = types.InlineKeyboardButton('Ваниль', callback_data='vanilla')
        btn16 = types.InlineKeyboardButton('Карамель', callback_data='caramel')
        btn17 = types.InlineKeyboardButton('Солёная карамель', callback_data='salted_caramel')
        btn18 = types.InlineKeyboardButton('Манго', callback_data='mango')
        btn19 = types.InlineKeyboardButton('Малина', callback_data='raspberry')
        btn20 = types.InlineKeyboardButton('Клубника', callback_data='strawberry')
        btn21 = types.InlineKeyboardButton('Огурец', callback_data='cucumber')
        btn22 = types.InlineKeyboardButton('Зелёный банан', callback_data='green_banana')
        btn23 = types.InlineKeyboardButton('Фисташки', callback_data='pistachios')
        btn24 = types.InlineKeyboardButton('Имбирный пряник', callback_data='gingerbread')
        btn25 = types.InlineKeyboardButton('Лесной орех', callback_data='hazelnut')
        btn26 = types.InlineKeyboardButton('Мята', callback_data='mint')
        btn27 = types.InlineKeyboardButton('Банан', callback_data='banana')
        btn28 = types.InlineKeyboardButton('Вишня', callback_data='cherry')
        btn29 = types.InlineKeyboardButton('Острый', callback_data='sharp')

        markup.row(btn1, btn2, btn28)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7, btn8, btn9)
        markup.row(btn10, btn11, btn12)
        markup.row(btn13, btn14, btn15)
        markup.row(btn16, btn28, btn18)
        markup.row(btn19, btn20, btn21)
        markup.row(btn29, btn23, btn24)
        markup.row(btn25, btn26, btn27)
        markup.row(btn3, btn17, btn22)

        bot.send_message(callback.message.chat.id, 'Выберите сироп:', reply_markup=markup)

    for i in list_of_syrup:
        markup = types.InlineKeyboardMarkup()
        if callback.data == list_of_syrup[i]:
            print(list_of_syrup[i])
            text_of_syrup += i
            count_of_syrup += 30
            print(final_price)
            markup.add(types.InlineKeyboardButton('Перейти к добавлению позиции в заказ', callback_data='next-clause'))
            bot.send_message(callback.message.chat.id, 'Сироп успешно добавлен!', reply_markup=markup)





bot.polling(none_stop=True)