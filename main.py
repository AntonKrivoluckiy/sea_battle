import random

import telebot

from Token import TOKEN

bot = telebot.TeleBot(TOKEN)


class State_rast:
    rast_3plbship = False
    rast_2plbship_1 = False
    rast_2plbship_2 = False
    rast_1plbship = False

class State_game:
    game = False


@bot.message_handler(commands=['start'])
def hello(message: telebot.types.Message):
    text = ('Привет, как можно понять из названия бота, весь его функционал - играть в "Морсой Бой".'
            '\nДля начала игры нужно использовать команду: /rules'
            '\nДля прочих функций используйте встроеную клавиатуру.'
            '\n!!!ВАЖНО!!! Игра не расчитана для игры через телефон, если вы используете его, пожалуйста перейдите на компьютер')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['rules'])
def rules_game(message: telebot.types.Message):
    text = ("Отлично, но для начала раунда необходимо ознакомится с некоторыми правилами:"
            "\n     1. Думаю с правилами самой игры вы ознакомлены, в противном случае обратитесь к интернету."
            "\n     2. Единственное отличие данной игры от оригинала - с целью оптимизации игры и созлания оптимальных условий для партии, игровое поле уменьшино на 2 клетки, теперь его размер не 10 на 10 клеток, а 8 на 8."
            "\n     3. Кнопки на вашем игровом поле являются лишь наглядным представленим вашего поевого поля, ни одна кнопка на нем работать НЕ будет, кроме расстановки кораблей на игровом поле в начале игры."
            "\n     Некоторые клетки на поле, после взаимодействия с ними, будут иметь специальные символы:"
            '\n             1. "{}" - таким символом будут обозначаться однопалубные корабли на игровом поле;'
            '\n             2. "{ }" - таким символом будут обозначаться 2-х палубные корабли на игровом поле;'
            '\n             2. "{ = }" - таким символом будут обозначаться 3-х палубные корабли на игровом поле;'
            '\n             4. "X" - этот символ обозначает, что ваш или корабль противника унечтожен, "х" - данный символ означает, что в корабль попали, но еще не потопили его;'
            '\n             5. "*" - этим символом будут обозначаться промохи по акватории противника.'
            '\n'
            '\nДля начала игры используйте команду: /game'
            '\nДля прочих функций используйте встроеную клавиатуру.')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['game'])
def prepare_game(message):
    bot.send_message(message.chat.id, text='Перед началом самой игры необходимо раставить ваши корабли на поле. Из-за уменьшеного размера игрового поля, количество подконтрольных кораблей тоже уменьшилось, теперь в вашем распоряжении:\n    Один 3-х палубный корабль;\n    Два 2-х палубных корабля;\n    Три однопалубных корабля.')
    bot.send_message(message.chat.id, text='Для начала установите 3-х палубный корабль, для этого нужно нажать на 3 клетки, лежащие на одной линии и соприкосающиеся друг с другом  (програма расчитана на растановку с слева на право и с верху в низ, пожалуйста, во избежаний графичкских ошибок, начинайте растановку корабля с лева на право или с верху в низ!).')
    send_buttons(message.chat.id)

    rast_bot = random.choice(['1', '2', '3', '4', '5'])

    def set_symbol(row, col, symbol):
        buttons_bot[row][col] = symbol

    def place_symbols(coords, symbols):
        for coord, symbol in zip(coords, symbols):
            set_symbol(*coord, symbol)
    if rast_bot == '1':
        place_symbols([(0, 0), (7, 7), (7, 0), (3, 1), (4, 1), (4, 6), (5, 6), (6, 2), (6, 3), (6, 4)],
                      ['{', '}', '{', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '2':
        place_symbols([(1, 0), (2, 6), (7, 3), (4, 1), (5, 1), (4, 5), (5, 5), (1, 3), (2, 3), (3, 3)],
                      ['{', '}', '{', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '3':
        place_symbols([(0, 2), (1, 6), (7, 3), (2, 2), (2, 3), (4, 4), (4, 5), (5, 1), (6, 1), (7, 1)],
                      ['{', '}', '{', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '4':
        place_symbols([(1, 1), (5, 1), (7, 2), (1, 6), (2, 6), (6, 4), (6, 5), (2, 3), (3, 3), (4, 3)],
                      ['{', '}', '{', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '5':
        place_symbols([(1, 6), (4, 1), (4, 3), (4, 6), (5, 6), (6, 3), (6, 4), (2, 1), (2, 2), (2, 3)],
                      ['{', '}', '{', '{', '}', '{', '}', '{', '=', '}'])
    State_rast.rast_3plbship = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_3plbship)
def rast_3plbship(call):
    row, column = map(int, call.data.split())
    global not_ships_zone
    not_ships_zone = ''
    if " } " not in str(buttons) and '=' in str(buttons):
        if ("=" in buttons[row + 1][column] or "=" in buttons[row - 1][column] or "=" in buttons[row][column + 1] or "=" in buttons[row][column - 1]) and (" { " in buttons[row + 2][column] or " { " in buttons[row - 2][column] or " { " in buttons[row][column + 2] or " { " in buttons[row][column - 2]):
            buttons[row][column] = " } "
            not_ships_zone += buttons[row + 1][column] + buttons[row - 1][column] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id)
    if "=" not in str(buttons):
        if " { " in buttons[row + 1][column] or " { " in buttons[row - 1][column] or " { " in buttons[row][column + 1] or " { " in buttons[row][column - 1]:
            buttons[row][column] = "="
            not_ships_zone += buttons[row + 1][column] + buttons[row - 1][column] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id)
    if " { " not in str(buttons):
        buttons[row][column] = " { "
        not_ships_zone += buttons[row + 1][column] + buttons[row - 1][column] + buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_buttons(call.message.chat.id)
    if (str(buttons)).count(' { ') == 1 and (str(buttons)).count('=') == 1 and (str(buttons)).count(' } ') == 1:
        bot.send_message(call.message.chat.id, text='Отлично! Теперь расставьте два 2-х палубных корабля, для этого нужно нажать на 2 клетки, лежащие на одной линии и соприкасающиеся друг с другом. Программа расчитана на расстановку слева на право и сверху вниз, пожалуйста, начинайте расстановку корабля слева направо или сверху вниз, чтобы избежать графических ошибок!')
        send_buttons(call.message.chat.id)
        State_rast.rast_3plbship = False
        State_rast.rast_2plbship_1 = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_2plbship_1)
def rast_2plbship_1(call):
    row, column = map(int, call.data.split())
    global not_ships_zone
    if (str(buttons)).count('}') == 1:
        if (buttons[row][column] != ' { ') and (buttons[row][column] != '=') and (buttons[row][column] != ' } '):
            if '{' in buttons[row + 1][column] or '{' in buttons[row - 1][column] or '{' in buttons[row][column + 1] or '{' in buttons[row][column - 1]:
                if buttons[row][column] not in not_ships_zone:
                    buttons[row][column] = '}'
                    not_ships_zone += buttons[row + 1][column] + buttons[row - 1][column] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id)
    if (str(buttons)).count('{') == 1:
        if (buttons[row][column] != '{') and (buttons[row][column] != '=') and (buttons[row][column] != '}'):
            if buttons[row][column] not in not_ships_zone:
                buttons[row][column] = '{'
                not_ships_zone += buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
                bot.delete_message(call.message.chat.id, call.message.message_id)
                send_buttons(call.message.chat.id)
    if (str(buttons)).count('{') == 2 and (str(buttons)).count('}') == 2:
        State_rast.rast_2plbship_1 = False
        State_rast.rast_2plbship_2 = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_2plbship_2)
def rast_2plbship_2(call):
    row, column = map(int, call.data.split())
    global not_ships_zone
    if (str(buttons)).count('}') == 2:
        if (buttons[row][column] != ' { ') and (buttons[row][column] != '=') and (buttons[row][column] != ' } '):
            if '{' in buttons[row + 1][column] or '{' in buttons[row - 1][column] or '{' in buttons[row][column + 1] or '{' in buttons[row][column - 1]:
                if buttons[row][column] not in not_ships_zone:
                    buttons[row][column] = '}'
                    not_ships_zone += buttons[row + 1][column] + buttons[row - 1][column] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id)
    if (str(buttons)).count('{') == 2:
        if (buttons[row][column] != ' { ') and (buttons[row][column] != '=') and (buttons[row][column] != ' } '):
            if buttons[row][column] not in not_ships_zone:
                buttons[row][column] = '{'
                not_ships_zone += buttons[row + 1][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row + 1][column - 1]
                bot.delete_message(call.message.chat.id, call.message.message_id)
                send_buttons(call.message.chat.id)
    if (str(buttons)).count('{') == 3 and (str(buttons)).count('}') == 3:
        bot.send_message(call.message.chat.id, text='Отлично!!! Теперь вам осталось раставить три однопалубных корабля.')
        send_buttons(call.message.chat.id)
        State_rast.rast_2plbship_2 = False
        State_rast.rast_1plbship = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_1plbship)
def rast_1plbship(call):
    row, column = map(int, call.data.split())
    global not_ships_zone
    def is_valid_position(row, column):
        return 0 <= row < len(buttons) and 0 <= column < len(buttons[0])

    if (str(buttons)).count('{}') != 3:
        if is_valid_position(row, column) and buttons[row][column] not in not_ships_zone:
            buttons[row][column] = '{}'
            for r in range(max(0, row - 1), min(len(buttons), row + 2)):
                for c in range(max(0, column - 1), min(len(buttons[0]), column + 2)):
                    not_ships_zone += buttons[r][c]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id)
    if (str(buttons)).count('{}') == 3:
        bot.send_message(call.message.chat.id, text='Отлично, теперь ваш боевой флот полсностью расставлен и готов к бою!!!')
        bot.send_message(call.message.chat.id, 'Теперь, когда вы и ваш противник готовы к бою, вы можете атаковать его флот, нажимая на его игровое поле, если вы попадете в корабль противника, то на клетке появится крест (" X "), что означает попадание или убийство корабля противника, в противном случае будет символ промаха(" * ").'
                                           '\nУдачи в бою, возвращайтесь с победой!!!')
        send_buttons(call.message.chat.id)
        bot_send_buttons(call.message.chat.id)
        State_rast.rast_1plbship = False
        State_game.game = True


@bot.callback_query_handler(func=lambda call: State_game.game and buttons_bot)
def game(call):
    pass


rows = list(range(1, 9))
columns = list('АБВГДЕЖЗ')

buttons = [[f'{columns[column]}/{rows[row]}' for column in range(8)] for row in range(8)]

def send_buttons(chat_id):
    markup = telebot.types.InlineKeyboardMarkup()
    row_buttons = []
    for row in range(8):
        for column in range(8):
            button = telebot.types.InlineKeyboardButton(text=f'{buttons[row][column]}', callback_data=f'{row} {column}')
            row_buttons.append(button)
            if len(row_buttons) == 8:
                markup.row(*row_buttons)
                row_buttons = []
    if row_buttons:
        markup.row(*row_buttons)
    bot.send_message(chat_id, text='[                            Ваше игровое поле                             ]', reply_markup=markup)

rows_bot = list(range(1, 9))
columns_bot = list('АБВГДЕЖЗ')

buttons_bot = [[f'{columns_bot[column_bot]}/{rows_bot[row_bot]}' for column_bot in range(8)] for row_bot in range(8)]

def get_display_value(symbol, row, col):
    if symbol in ['{', '=', '}', '{}']:
        return f'{chr(1040 + col)}/{row + 1}'
    return symbol

def bot_send_buttons(chat_id):
    global buttons_bot
    markup_bot = telebot.types.InlineKeyboardMarkup()
    row_buttons_bot = []
    for row_bot in range(8):
        for column_bot in range(8):
            symbol = buttons_bot[row_bot][column_bot]
            display_value = get_display_value(symbol, row_bot, column_bot)
            button_bot = telebot.types.InlineKeyboardButton(text=f'{display_value}', callback_data=f'{row_bot} {column_bot}')
            row_buttons_bot.append(button_bot)
            if len(row_buttons_bot) == 8:
                markup_bot.row(*row_buttons_bot)
                row_buttons_bot = []
    if row_buttons_bot:
        markup_bot.row(*row_buttons_bot)
    bot.send_message(chat_id, text='[                           Игровое поле противника                         ]', reply_markup=markup_bot)
    print(str(buttons_bot))

print('Bot Start')
bot.infinity_polling()
