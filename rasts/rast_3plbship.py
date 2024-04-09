from buttons.buttons import buttons, send_buttons
from init_bot import bot
from states.states import State_rast, not_zone


@bot.callback_query_handler(func=lambda call: State_rast.rast_3plbship)
def rast_3plbship(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    if '=' not in str(buttons) and ' [ ' in str(buttons):
        if row < 6 and column < 6:
            if " [ " in buttons[row - 1][column]:
                buttons[row + 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row + 1][column]:
                buttons[row - 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row][column - 1]:
                buttons[row][column + 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            if " [ " in buttons[row][column + 1]:
                buttons[row][column - 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
        if row == 6 and column < 6:
            if " [ " in buttons[row - 1][column]:
                buttons[row + 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1]
            if " [ " in buttons[row + 1][column]:
                buttons[row - 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1]
            if " [ " in buttons[row][column - 1]:
                buttons[row][column + 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            if " [ " in buttons[row][column + 1]:
                buttons[row][column - 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row + 1][column + 2] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
        if row < 6 and column == 6:
            if " [ " in buttons[row - 1][column]:
                buttons[row + 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row + 1][column]:
                buttons[row - 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row - 1][column + 1] + buttons[row][column - 1] + buttons[row][column + 1] + buttons[row + 1][column - 1] + buttons[row + 1][column + 1] + buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1]
            if " [ " in buttons[row][column - 1]:
                buttons[row][column + 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1]
            if " [ " in buttons[row][column + 1]:
                buttons[row][column - 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
        if row < 7 and column == 7:
            if " [ " in buttons[row - 1][column]:
                buttons[row + 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 2][column - 1] + buttons[row + 2][column]
            if " [ " in buttons[row + 1][column]:
                buttons[row - 1][column] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row - 2][column] + buttons[row - 2][column - 1] + buttons[row - 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 2][column - 1] + buttons[row + 2][column]
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
        if row == 7 and column < 7:
            if " [ " in buttons[row][column - 1]:
                buttons[row][column + 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1] + buttons[row - 1][column + 2] + buttons[row][column + 2]
            if " [ " in buttons[row][column + 1]:
                buttons[row][column - 1] = ' ] '
                buttons[row][column] = '='
                not_zone.not_ships_zone += buttons[row][column - 2] + buttons[row - 1][column - 2] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1] + buttons[row - 1][column + 2] + buttons[row][column + 2]
                bot.delete_message(call.message.chat.id, call.message.message_id)
            send_buttons(call.message.chat.id, 'user')
    if " [ " not in str(buttons):
        buttons[row][column] = ' [ '
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count(' [ ') == 1 and (str(buttons)).count('=') == 1 and (str(buttons)).count(' ] ') == 1:
        bot.send_message(call.message.chat.id, text='Отлично! Теперь расставьте два 2-х палубных корабля, для этого нужно нажать на 2 клетки, лежащие на одной линии и соприкасающиеся друг с другом. Программа расчитана на расстановку слева на право и сверху вниз, пожалуйста, начинайте расстановку корабля слева направо или сверху вниз, чтобы избежать графических ошибок!')
        send_buttons(call.message.chat.id, 'user')
        State_rast.rast_3plbship = False
        State_rast.rast_2plbship_1 = True