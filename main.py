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

class not_zone:
    not_ships_zone = ''


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
            '\n             4. "X" - этот символ обозначает, что вы или ваш противник попали в корабль противника;'
            '\n             5. "*" - этим символом будут обозначаться промохи по акватории противника.'
            '\n'
            '\nДля начала игры используйте команду: /game'
            '\nДля прочих функций используйте встроеную клавиатуру.')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['game'])
def prepare_game(message):
    bot.send_message(message.chat.id, text='Перед началом самой игры необходимо раставить ваши корабли на поле. Из-за уменьшеного размера игрового поля, количество подконтрольных кораблей тоже уменьшилось, теперь в вашем распоряжении:\n    Один 3-х палубный корабль;\n    Два 2-х палубных корабля;\n    Три однопалубных корабля.')
    bot.send_message(message.chat.id, text='Для начала установите 3-х палубный корабль, для этого нужно нажать на 3 клетки, лежащие на одной линии и соприкосающиеся друг с другом  (програма расчитана на растановку с слева на право и с верху в низ, пожалуйста, во избежаний графичкских ошибок, начинайте растановку корабля с лева на право или с верху в низ!).')
    send_buttons(message.chat.id, 'user')

    global rast_bot
    rast_bot = random.choice(['1', '2', '3', '4', '5'])

    def set_symbol(row, col, symbol):
        buttons_bot[row][col] = symbol

    def place_symbols(coords, symbols):
        for coord, symbol in zip(coords, symbols):
            set_symbol(*coord, symbol)
    if rast_bot == '1':
        place_symbols([(0, 0), (7, 7), (7, 0), (3, 1), (4, 1), (4, 6), (5, 6), (6, 2), (6, 3), (6, 4)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '2':
        place_symbols([(1, 0), (2, 6), (7, 3), (4, 1), (5, 1), (4, 5), (5, 5), (1, 3), (2, 3), (3, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '3':
        place_symbols([(0, 2), (1, 6), (7, 3), (2, 2), (2, 3), (4, 4), (4, 5), (5, 1), (6, 1), (7, 1)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '4':
        place_symbols([(1, 1), (5, 1), (7, 2), (1, 6), (2, 6), (6, 4), (6, 5), (2, 3), (3, 3), (4, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast_bot == '5':
        place_symbols([(1, 6), (4, 1), (4, 3), (4, 6), (5, 6), (6, 3), (6, 4), (2, 1), (2, 2), (2, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    State_rast.rast_3plbship = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_3plbship)
def rast_3plbship(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    if " ] " not in str(buttons) and '=' in str(buttons):
        if ("=" in buttons[row + 1][column] or "=" in buttons[row - 1][column] or "=" in buttons[row][column + 1] or "=" in buttons[row][column - 1]) and (" [ " in buttons[row + 2][column] or " [ " in buttons[row - 2][column] or " [ " in buttons[row][column + 2] or " [ " in buttons[row][column - 2]):
            buttons[row][column] = " ] "
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
    if "=" not in str(buttons):
        if " [ " in buttons[row + 1][column] or " [ " in buttons[row - 1][column] or " [ " in buttons[row][column + 1] or " [ " in buttons[row][column - 1]:
            if " [ " in buttons[row - 1][column]:
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row + 1][column]:
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row][column - 1]:
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            if " [ " in buttons[row][column + 1]:
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            buttons[row][column] = "="
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
    if " [ " not in str(buttons):
        buttons[row][column] = " [ "
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count(' [ ') == 1 and (str(buttons)).count('=') == 1 and (str(buttons)).count(' ] ') == 1:
        bot.send_message(call.message.chat.id, text='Отлично! Теперь расставьте два 2-х палубных корабля, для этого нужно нажать на 2 клетки, лежащие на одной линии и соприкасающиеся друг с другом. Программа расчитана на расстановку слева на право и сверху вниз, пожалуйста, начинайте расстановку корабля слева направо или сверху вниз, чтобы избежать графических ошибок!')
        send_buttons(call.message.chat.id, 'user')
        State_rast.rast_3plbship = False
        State_rast.rast_2plbship_1 = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_2plbship_1)
def rast_2plbship_1(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    if (str(buttons)).count(']') == 10:
        if (buttons[row][column] != ' [ ') and (buttons[row][column] != '=') and (buttons[row][column] != ' ] '):
            if '[' in buttons[row + 1][column] or '[' in buttons[row - 1][column] or '[' in buttons[row][column + 1] or '[' in buttons[row][column - 1]:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    buttons[row][column] = ']'
                    if '[' in buttons[row + 1][column]:
                        not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1] + buttons[row + 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1]
                    if '[' in buttons[row - 1][column]:
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column] + buttons[row + 1][column + 1]
                    if '[' in buttons[row][column + 1]:
                        not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row + 1][column + 2] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column - 1] + buttons[row][column - 1]+ buttons[row + 1][column - 1]
                    if '[' in buttons[row][column - 1]:
                        not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column + 1] + buttons[row][column + 1]+ buttons[row + 1][column + 1]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 10:
        if (buttons[row][column] != '[') and (buttons[row][column] != '=') and (buttons[row][column] != ']'):
            if buttons[row][column] not in not_zone.not_ships_zone:
                buttons[row][column] = '['
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.delete_message(call.message.chat.id, call.message.message_id - 2)
                send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 11 and (str(buttons)).count(']') == 11:
        State_rast.rast_2plbship_1 = False
        State_rast.rast_2plbship_2 = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_2plbship_2)
def rast_2plbship_2(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    if (str(buttons)).count(']') == 11:
        if (buttons[row][column] != ' [ ') and (buttons[row][column] != '=') and (buttons[row][column] != ' ] '):
            if '[' in buttons[row + 1][column] or '[' in buttons[row - 1][column] or '[' in buttons[row][column + 1] or '[' in buttons[row][column - 1]:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    if '[' in buttons[row + 1][column]:
                        not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1] + buttons[row + 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1]
                    if '[' in buttons[row - 1][column]:
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column] + buttons[row + 1][column + 1]
                    if '[' in buttons[row][column + 1]:
                        not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row + 1][column + 2] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1]
                    if '[' in buttons[row][column - 1]:
                        not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column + 1] + buttons[row][column + 1] + buttons[row + 1][column + 1]
                    buttons[row][column] = ']'
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 11:
        if (buttons[row][column] != ' [ ') and (buttons[row][column] != '=') and (buttons[row][column] != ' ] '):
            if buttons[row][column] not in not_zone.not_ships_zone:
                buttons[row][column] = '['
                bot.delete_message(call.message.chat.id, call.message.message_id)
                send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 12 and (str(buttons)).count(']') == 12:
        bot.send_message(call.message.chat.id, text='Отлично!!! Теперь вам осталось раставить три однопалубных корабля.')
        send_buttons(call.message.chat.id, 'user')
        State_rast.rast_2plbship_2 = False
        State_rast.rast_1plbship = True

@bot.callback_query_handler(func=lambda call: State_rast.rast_1plbship)
def rast_1plbship(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    def is_valid_position(row, column):
        return 0 <= row < len(buttons) and 0 <= column < len(buttons[0])

    if (str(buttons)).count('[ ]') != 3:
        if (str(buttons)).count('[ ]') == 0:
            if is_valid_position(row, column) and buttons[row][column] not in not_zone.not_ships_zone:
                buttons[row][column] = '[ ]'
                for r in range(max(0, row - 1), min(len(buttons), row + 2)):
                    for c in range(max(0, column - 1), min(len(buttons[0]), column + 2)):
                        not_zone.not_ships_zone += buttons[r][c]
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.delete_message(call.message.chat.id, call.message.message_id - 2)
                send_buttons(call.message.chat.id, 'user')
        else:
            if is_valid_position(row, column) and buttons[row][column] not in not_zone.not_ships_zone:
                buttons[row][column] = '[ ]'
                for r in range(max(0, row - 1), min(len(buttons), row + 2)):
                    for c in range(max(0, column - 1), min(len(buttons[0]), column + 2)):
                        not_zone.not_ships_zone += buttons[r][c]
                bot.delete_message(call.message.chat.id, call.message.message_id)
                send_buttons(call.message.chat.id, 'user')
        if (str(buttons)).count('[ ]') == 3:
            bot.send_message(call.message.chat.id, text='Отлично, теперь ваш боевой флот полсностью расставлен и готов к бою!!!')
            bot.send_message(call.message.chat.id, 'Теперь, когда вы и ваш противник готовы к бою, вы можете атаковать его флот, нажимая на его игровое поле, если вы попадете в корабль противника, то на клетке появится крест (" X "), что означает попадание или убийство корабля противника, в противном случае будет символ промаха(" * ").'
                                                '\nПервый ход за вами.'
                                                '\nУдачи в бою, возвращайтесь с победой!!!')
            send_buttons(call.message.chat.id, 'user')
            bot_send_buttons(call.message.chat.id)
            State_rast.rast_1plbship = False
            State_game.game = True

@bot.callback_query_handler(func=lambda call: State_game.game)
def game(call):
    row_bot, column_bot = map(int, call.data.split())
    if call.data.startswith('user'):
        pass
    else:
        global rast_bot
        if buttons_bot[row_bot][column_bot] != '*':
            if rast_bot == '1':
                if row_bot == 0 and column_bot == 0:
                    buttons_bot[row_bot][column_bot] = 'X'
                    buttons_bot[1][1] = '*'
                    buttons_bot[0][1] = '*'
                    buttons_bot[1][0] = '*'
                if row_bot == 7 and column_bot == 7:
                    buttons_bot[row_bot][column_bot] = 'X'
                    buttons_bot[6][7] = ' * '
                    buttons_bot[6][6] = ' * '
                    buttons_bot[7][6] = ' * '
                if row_bot == 7 and column_bot == 0:
                    buttons_bot[row_bot][column_bot] = 'X'
                    buttons_bot[6][0] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[7][1] = '*'
                if row_bot == 3 and column_bot == 1:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[4][1] == 'X':
                        buttons_bot[2][0] = '*'
                        buttons_bot[2][1] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][1] = '*'
                        buttons_bot[5][2] = '*'
                if row_bot == 4 and column_bot == 1:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[3][1] == 'X':
                        buttons_bot[2][0] = '*'
                        buttons_bot[2][1] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][1] = '*'
                        buttons_bot[5][2] = '*'
                if row_bot == 4 and column_bot == 6:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[5][6] == 'X':
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[4][7] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][7] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[6][7] = '*'
                if row_bot == 5 and column_bot == 6:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[4][6] == 'X':
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[4][7] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][7] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[6][7] = '*'
                if row_bot == 6 and column_bot == 2:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[6][3] == 'X' and buttons_bot[6][4] == 'X':
                        buttons_bot[5][1] = '*'
                        buttons_bot[6][1] = '*'
                        buttons_bot[7][1] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[7][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[7][5] = '*'
                if row_bot == 6 and column_bot == 3:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[6][2] == 'X' and buttons_bot[6][4] == 'X':
                        buttons_bot[5][1] = '*'
                        buttons_bot[6][1] = '*'
                        buttons_bot[7][1] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[7][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[7][5] = '*'
                if row_bot == 6 and column_bot == 4:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[6][3] == 'X' and buttons_bot[6][2] == 'X':
                        buttons_bot[5][1] = '*'
                        buttons_bot[6][1] = '*'
                        buttons_bot[7][1] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[7][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[7][5] = '*'
                if not(row_bot == 0 and column_bot == 0) and not(row_bot == 7 and column_bot == 7) and not(row_bot == 7 and column_bot == 0) and not(row_bot == 3 and column_bot == 1) and not(row_bot == 4 and column_bot == 1) and not(row_bot == 4 and column_bot == 6) and not(row_bot == 5 and column_bot == 6) and not(row_bot == 6 and column_bot == 2) and not(row_bot == 6 and column_bot == 3) and not(row_bot == 6 and column_bot == 4):
                    buttons_bot[row_bot][column_bot] = '*'
            if rast_bot == ('2'):
                if row_bot == 1 and column_bot == 0:
                    buttons_bot[1][0] = 'X'
                    buttons_bot[0][0] = '*'
                    buttons_bot[0][1] = '*'
                    buttons_bot[1][1] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][0] = '*'
                if row_bot == 2 and column_bot == 6:
                    buttons_bot[2][6] = 'X'
                    buttons_bot[1][5] = '*'
                    buttons_bot[1][6] = '*'
                    buttons_bot[1][7] = '*'
                    buttons_bot[2][5] = '*'
                    buttons_bot[2][7] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
                if row_bot == 7 and column_bot == 3:
                    buttons_bot[7][3] = 'X'
                    buttons_bot[7][2] = '*'
                    buttons_bot[6][2] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[6][4] = '*'
                    buttons_bot[7][4] = '*'
                if row_bot == 4 and column_bot == 1:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[5][1] == 'X':
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[6][0] = '*'
                        buttons_bot[6][1] = '*'
                        buttons_bot[6][2] = '*'
                if row_bot == 5 and column_bot == 1:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[4][1] == 'X':
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[6][0] = '*'
                        buttons_bot[6][1] = '*'
                        buttons_bot[6][2] = '*'
                if row_bot == 4 and column_bot == 5:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[5][5] == 'X':
                        buttons_bot[3][4] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[4][4] = '*'
                        buttons_bot[4][6] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][6] = '*'
                        buttons_bot[6][4] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                if row_bot == 5 and column_bot == 5:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[4][5] == 'X':
                        buttons_bot[3][4] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[4][4] = '*'
                        buttons_bot[4][6] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][6] = '*'
                        buttons_bot[6][4] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                if row_bot == 1 and column_bot == 3:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[2][3] == 'X' and buttons_bot[3][3] == 'X':
                        buttons_bot[0][2] = '*'
                        buttons_bot[0][3] = '*'
                        buttons_bot[0][4] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][3] = '*'
                        buttons_bot[4][4] = '*'
                if row_bot == 2 and column_bot == 3:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[1][3] == 'X' and buttons_bot[3][3] == 'X':
                        buttons_bot[0][2] = '*'
                        buttons_bot[0][3] = '*'
                        buttons_bot[0][4] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][3] = '*'
                        buttons_bot[4][4] = '*'
                if row_bot == 3 and column_bot == 3:
                    buttons_bot[row_bot][column_bot] = 'X'
                    if buttons_bot[2][3] == 'X' and buttons_bot[1][3] == 'X':
                        buttons_bot[0][2] = '*'
                        buttons_bot[0][3] = '*'
                        buttons_bot[0][4] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][3] = '*'
                        buttons_bot[4][4] = '*'
                if not(row_bot == 1 and column_bot == 0) and not(row_bot == 2 and column_bot == 6) and not(row_bot == 7 and column_bot == 3) and not(row_bot == 4 and column_bot == 1) and not(row_bot == 5 and column_bot == 1) and not(row_bot == 4 and column_bot == 5) and not(row_bot == 5 and column_bot == 5) and not(row_bot == 1 and column_bot == 3) and not(row_bot == 2 and column_bot == 3) and not(row_bot == 3 and column_bot == 3):
                    buttons_bot[row_bot][column_bot] = '*'
            if rast_bot == '3':
                if row_bot == 2 and column_bot == 0:
                    buttons_bot[2][0] = 'X'
                    buttons_bot[1][0] = '*'
                    buttons_bot[1][1] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                if row_bot == 1 and column_bot == 6:
                    buttons_bot[1][6] = 'X'
                    buttons_bot[0][5] = '*'
                    buttons_bot[0][6] = '*'
                    buttons_bot[0][7] = '*'
                    buttons_bot[1][5] = '*'
                    buttons_bot[1][7] = '*'
                    buttons_bot[2][5] = '*'
                    buttons_bot[2][6] = '*'
                    buttons_bot[2][7] = '*'
                if row_bot == 3 and column_bot == 7:
                    buttons_bot[3][7] = 'X'
                    buttons_bot[2][7] = '*'
                    buttons_bot[2][6] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[4][6] = '*'
                    buttons_bot[4][7] = '*'
                if row_bot == 2 and column_bot == 2:
                    buttons_bot[2][2] = 'X'
                    if buttons_bot[3][2] == 'X':
                        buttons_bot[1][1] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[2][1] = '*'
                        buttons_bot[2][3] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][3] = '*'
                        buttons_bot[4][1] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][3] = '*'
                if row_bot == 3 and column_bot == 2:
                    buttons_bot[3][2] = 'X'
                    if buttons_bot[2][2] == 'X':
                        buttons_bot[1][1] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[2][1] = '*'
                        buttons_bot[2][3] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][3] = '*'
                        buttons_bot[4][1] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][3] = '*'
                if row_bot == 4 and column_bot == 4:
                    buttons_bot[4][4] = 'X'
                    if buttons_bot[5][4] == 'X':
                        buttons_bot[3][3] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[4][3] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][3] = '*'
                        buttons_bot[6][4] = '*'
                        buttons_bot[6][5] = '*'
                if row_bot == 5 and column_bot == 4:
                    buttons_bot[5][4] = 'X'
                    if buttons_bot[4][4] == 'X':
                        buttons_bot[3][3] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[4][3] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][3] = '*'
                        buttons_bot[6][4] = '*'
                        buttons_bot[6][5] = '*'
                if row_bot == 5 and column_bot == 1:
                    buttons_bot[5][1] = 'X'
                    if buttons_bot[6][1] == 'X' and buttons_bot[7][1] == 'X':
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][1] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[6][0] = '*'
                        buttons_bot[7][0] = '*'
                        buttons_bot[7][2] = '*'
                if row_bot == 6 and column_bot == 1:
                    buttons_bot[6][1] = 'X'
                    if buttons_bot[5][1] == 'X' and buttons_bot[7][1] == 'X':
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][1] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[6][0] = '*'
                        buttons_bot[7][0] = '*'
                        buttons_bot[7][2] = '*'
                if row_bot == 7 and column_bot == 1:
                    buttons_bot[7][1] = 'X'
                    if buttons_bot[5][1] == 'X' and buttons_bot[6][1] == 'X':
                        buttons_bot[4][0] = '*'
                        buttons_bot[4][1] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[5][0] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[6][0] = '*'
                        buttons_bot[6][2] = '*'
                        buttons_bot[7][0] = '*'
                        buttons_bot[7][2] = '*'
                if not(row_bot == 2 and column_bot == 0) and not(row_bot == 1 and column_bot == 6) and not(row_bot == 3 and column_bot == 7) and not(row_bot == 2 and column_bot == 2) and not(row_bot == 3 and column_bot == 2) and not(row_bot == 4 and column_bot == 4) and not(row_bot == 5 and column_bot == 4) and not(row_bot == 5 and column_bot == 1) and not(row_bot == 6 and column_bot == 1) and not(row_bot == 7 and column_bot == 1):
                    buttons_bot[row_bot][column_bot] = '*'
            if rast_bot == '4':
                if row_bot == 1 and column_bot == 1:
                    buttons_bot[1][1] = 'X'
                    buttons_bot[0][0] = '*'
                    buttons_bot[0][1] = '*'
                    buttons_bot[0][2] = '*'
                    buttons_bot[1][0] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][2] = '*'
                if row_bot == 5 and column_bot == 1:
                    buttons_bot[5][1] = 'X'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[6][2] = '*'
                if row_bot == 7 and column_bot == 2:
                    buttons_bot[7][2] = 'X'
                    buttons_bot[7][1] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[6][2] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[7][3] = '*'
                if row_bot == 6 and column_bot == 4:
                    buttons_bot[6][4] = 'X'
                    if buttons_bot[6][5] == 'X':
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][6] = '*'
                        buttons_bot[6][3] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[7][5] = '*'
                        buttons_bot[7][6] = '*'
                if row_bot == 6 and column_bot == 5:
                    buttons_bot[6][5] = 'X'
                    if buttons_bot[6][4] == 'X':
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][6] = '*'
                        buttons_bot[6][3] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[7][5] = '*'
                        buttons_bot[7][6] = '*'
                if row_bot == 1 and column_bot == 6:
                    buttons_bot[1][6] = 'X'
                    if buttons_bot[2][6] == 'X':
                        buttons_bot[0][5] = '*'
                        buttons_bot[0][6] = '*'
                        buttons_bot[0][7] = '*'
                        buttons_bot[1][5] = '*'
                        buttons_bot[1][7] = '*'
                        buttons_bot[2][5] = '*'
                        buttons_bot[2][7] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                if row_bot == 2 and column_bot == 6:
                    buttons_bot[2][6] = 'X'
                    if buttons_bot[1][6] == 'X':
                        buttons_bot[0][5] = '*'
                        buttons_bot[0][6] = '*'
                        buttons_bot[0][7] = '*'
                        buttons_bot[1][5] = '*'
                        buttons_bot[1][7] = '*'
                        buttons_bot[2][5] = '*'
                        buttons_bot[2][7] = '*'
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                if row_bot == 2 and column_bot == 3:
                    buttons_bot[2][3] = 'X'
                    if buttons_bot[3][3] == 'X' and buttons_bot[4][3] == 'X':
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][4] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                if row_bot == 3 and column_bot == 3:
                    buttons_bot[3][3] = 'X'
                    if buttons_bot[2][3] == 'X' and buttons_bot[4][3] == 'X':
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][4] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                if row_bot == 4 and column_bot == 3:
                    buttons_bot[4][3] = 'X'
                    if buttons_bot[3][3] == 'X' and buttons_bot[2][3] == 'X':
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][2] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][4] = '*'
                        buttons_bot[4][2] = '*'
                        buttons_bot[4][4] = '*'
                        buttons_bot[5][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                if not(row_bot == 1 and column_bot == 1) and not(row_bot == 5 and column_bot == 1) and not(row_bot == 7 and column_bot == 2) and not(row_bot == 6 and column_bot == 4) and not(row_bot == 6 and column_bot == 5) and not(row_bot == 1 and column_bot == 6) and not(row_bot == 2 and column_bot == 6) and not(row_bot == 2 and column_bot == 3) and not(row_bot == 3 and column_bot == 3) and not(row_bot == 4 and column_bot == 3):
                    buttons_bot[row_bot][column_bot] = '*'
            if rast_bot == '5':
                if row_bot == 1 and column_bot == 6:
                    buttons_bot[1][6] = 'X'
                    buttons_bot[0][5] = '*'
                    buttons_bot[0][6] = '*'
                    buttons_bot[0][7] = '*'
                    buttons_bot[1][5] = '*'
                    buttons_bot[1][7] = '*'
                    buttons_bot[2][5] = '*'
                    buttons_bot[2][6] = '*'
                    buttons_bot[2][7] = '*'
                if row_bot == 4 and column_bot == 1:
                    buttons_bot[4][1] = 'X'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][1] = '*'
                    buttons_bot[5][2] = '*'
                if row_bot == 4 and column_bot == 3:
                    buttons_bot[4][3] = 'X'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
                if row_bot == 4 and column_bot == 6:
                    buttons_bot[4][6] = 'X'
                    if buttons_bot[5][6] == 'X':
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[4][7] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][7] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[6][7] = '*'
                if row_bot == 5 and column_bot == 6:
                    buttons_bot[5][6] = 'X'
                    if buttons_bot[4][6] == 'X':
                        buttons_bot[3][5] = '*'
                        buttons_bot[3][6] = '*'
                        buttons_bot[3][7] = '*'
                        buttons_bot[4][5] = '*'
                        buttons_bot[4][7] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[5][7] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[6][6] = '*'
                        buttons_bot[6][7] = '*'
                if row_bot == 6 and column_bot == 3:
                    buttons_bot[6][3] = 'X'
                    if buttons_bot[6][4] == 'X':
                        buttons_bot[5][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][2] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[7][2] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[7][5] = '*'
                if row_bot == 6 and column_bot == 4:
                    buttons_bot[6][4] = 'X'
                    if buttons_bot[6][3] == 'X':
                        buttons_bot[5][2] = '*'
                        buttons_bot[5][3] = '*'
                        buttons_bot[5][4] = '*'
                        buttons_bot[5][5] = '*'
                        buttons_bot[6][2] = '*'
                        buttons_bot[6][5] = '*'
                        buttons_bot[7][2] = '*'
                        buttons_bot[7][3] = '*'
                        buttons_bot[7][4] = '*'
                        buttons_bot[7][5] = '*'
                if row_bot == 2 and column_bot == 1:
                    buttons_bot[2][1] = 'X'
                    if buttons_bot[2][2] == 'X' and buttons_bot[2][3] == 'X':
                        buttons_bot[1][0] = '*'
                        buttons_bot[1][1] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][0] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][3] = '*'
                        buttons_bot[3][4] = '*'
                if row_bot == 2 and column_bot == 2:
                    buttons_bot[2][2] = 'X'
                    if buttons_bot[2][1] == 'X' and buttons_bot[2][3] == 'X':
                        buttons_bot[1][0] = '*'
                        buttons_bot[1][1] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][0] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][3] = '*'
                        buttons_bot[3][4] = '*'
                if row_bot == 2 and column_bot == 3:
                    buttons_bot[2][3] = 'X'
                    if buttons_bot[2][2] == 'X' and buttons_bot[2][1] == 'X':
                        buttons_bot[1][0] = '*'
                        buttons_bot[1][1] = '*'
                        buttons_bot[1][2] = '*'
                        buttons_bot[1][3] = '*'
                        buttons_bot[1][4] = '*'
                        buttons_bot[2][0] = '*'
                        buttons_bot[2][4] = '*'
                        buttons_bot[3][0] = '*'
                        buttons_bot[3][1] = '*'
                        buttons_bot[3][2] = '*'
                        buttons_bot[3][3] = '*'
                        buttons_bot[3][4] = '*'
                if not(row_bot == 1 and column_bot == 6) and not(row_bot == 4 and column_bot == 1) and not(row_bot == 4 and column_bot == 3) and not(row_bot == 4 and column_bot == 6) and not(row_bot == 5 and column_bot == 6) and not(row_bot == 6 and column_bot == 3) and not(row_bot == 6 and column_bot == 4) and not(row_bot == 2 and column_bot == 1) and not(row_bot == 2 and column_bot == 2) and not(row_bot == 2 and column_bot == 3):
                    buttons_bot[row_bot][column_bot] = '*'
            gaming()
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            send_buttons(call.message.chat.id, 'user')
            bot_send_buttons(call.message.chat.id)


ships_sumbols = ['[', ']', '[ ]', ' [ ', ' ] ', '=']
battle_sumbols = ['X', '*']

def gaming():
    rand_row = random.randint(0, 7)
    rand_column = random.randint(0, 7)
    print(rand_row, rand_column)
    if buttons[rand_row][rand_column] not in battle_sumbols:
        if buttons[rand_row][rand_column] not in ships_sumbols:
            buttons[rand_row][rand_column] = '*'
        if buttons[rand_row][rand_column] == '[ ]':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        buttons[rand_row][rand_column] = 'X'
                    elif rand_row + i >= 0 and rand_row + i < len(buttons) and rand_column + j >= 0 and rand_column + j < len(buttons[0]):
                        buttons[rand_row + i][rand_column + j] = '*'
        # if buttons[rand_row][rand_column] in ships_sumbols[:2]:
        #     if buttons[rand_row - 1][rand_column] in ships_sumbols[:2] or buttons[rand_row + 1][rand_column] in ships_sumbols[:2] or buttons[rand_row][rand_column - 1] in ships_sumbols[:2] or buttons[rand_row][rand_column + 1] in ships_sumbols[:2]:
        #         buttons[rand_row][rand_column] = 'X'
        #         if buttons[rand_row - 1][rand_column] == 'X':
        #             buttons[rand_row - 2][rand_column - 1] = '*'
        #             buttons[rand_row - 2][rand_column] = '*'
        #             buttons[rand_row - 2][rand_column + 1] = '*'
        #             buttons[rand_row - 1][rand_column - 1] = '*'
        #             buttons[rand_row - 1][rand_column + 1] = '*'
        #             buttons[rand_row][rand_column - 1] = '*'
        #             buttons[rand_row][rand_column + 1] = '*'
        #             buttons[rand_row + 1][rand_column - 1] = '*'
        #             buttons[rand_row + 1][rand_column] = '*'
        #             buttons[rand_row + 1][rand_column + 1] = '*'
        #         if buttons[rand_row + 1][rand_column] == 'X':
        #             buttons[rand_row + 2][rand_column + 1] = '*'
        #             buttons[rand_row + 2][rand_column] = '*'
        #             buttons[rand_row + 2][rand_column - 1] = '*'
        #             buttons[rand_row + 1][rand_column + 1] = '*'
        #             buttons[rand_row + 1][rand_column - 1] = '*'
        #             buttons[rand_row][rand_column + 1] = '*'
        #             buttons[rand_row][rand_column - 1] = '*'
        #             buttons[rand_row - 1][rand_column + 1] = '*'
        #             buttons[rand_row - 1][rand_column] = '*'
        #             buttons[rand_row - 1][rand_column - 1] = '*'
        #         if buttons[rand_row][rand_column - 1] == 'X':
        #             buttons[rand_row - 1][rand_column - 2] = '*'
        #             buttons[rand_row][rand_column - 2] = '*'
        #             buttons[rand_row + 1][rand_column - 2] = '*'
        #             buttons[rand_row - 1][rand_column - 1] = '*'
        #             buttons[rand_row + 1][rand_column - 1] = '*'
        #             buttons[rand_row - 1][rand_column] = '*'
        #             buttons[rand_row + 1][rand_column] = '*'
        #             buttons[rand_row - 1][rand_column + 1] = '*'
        #             buttons[rand_row][rand_column + 1] = '*'
        #             buttons[rand_row + 1][rand_column + 1] = '*'
        #         if buttons[rand_row][rand_column + 1] == 'X':
        #             buttons[rand_row + 1][rand_column + 2] = '*'
        #             buttons[rand_row][rand_column + 2] = '*'
        #             buttons[rand_row - 1][rand_column + 2] = '*'
        #             buttons[rand_row + 1][rand_column + 1] = '*'
        #             buttons[rand_row - 1][rand_column + 1] = '*'
        #             buttons[rand_row + 1][rand_column] = '*'
        #             buttons[rand_row - 1][rand_column] = '*'
        #             buttons[rand_row + 1][rand_column - 1] = '*'
        #             buttons[rand_row][rand_column - 1] = '*'
        #             buttons[rand_row - 1][rand_column - 1] = '*'

    else:
        gaming()


rows = list(range(1, 9))
columns = list('АБВГДЕЖЗ')

buttons = [[f'{columns[column]}/{rows[row]}' for column in range(8)] for row in range(8)]

def send_buttons(chat_id, x):
    markup = telebot.types.InlineKeyboardMarkup()
    row_buttons = []
    for row in range(8):
        for column in range(8):
            button = telebot.types.InlineKeyboardButton(text=f'{buttons[row][column]}', callback_data=f'{x}|{row} {column}')
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
