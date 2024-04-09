from buttons.buttons import buttons, send_buttons
from buttons.buttons_bot import bot_send_buttons
from init_bot import bot
from states.states import State_rast, not_zone, State_game


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
