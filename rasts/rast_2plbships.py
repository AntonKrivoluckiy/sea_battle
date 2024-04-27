from buttons.buttons import buttons, send_buttons
from init_bot import bot
from states.states import State_rast, not_zone
from sumbols.sumbols import ships_sumbols


@bot.callback_query_handler(func=lambda call: State_rast.rast_2plbship_1)
def rast_2plbship_1(call):
    row, column = map(int, call.data.rsplit('|', 1)[1].split())
    if buttons[row][column] not in ships_sumbols:
        if (str(buttons)).count(']') == 10 and (str(buttons)).count('[') == 11:
            if (buttons[row][column] != ' [ ') and (buttons[row][column] != '=') and (buttons[row][column] != ' ] '):
                if row < 6 and column < 6:
                    if buttons[row][column] not in not_zone.not_ships_zone:
                        if '[' in buttons[row + 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1] + buttons[row + 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1]
                        if '[' in buttons[row - 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column] + buttons[row + 1][column + 1]
                        if '[' in buttons[row][column + 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row + 1][column + 2] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1]
                        if '[' in buttons[row][column - 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column + 1] + buttons[row][column + 1] + buttons[row + 1][column + 1]
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                        send_buttons(call.message.chat.id, 'user')
                if row < 7 and column == 7:
                    if buttons[row][column] not in not_zone.not_ships_zone:
                        if '[' in buttons[row + 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 1][column - 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column]
                        if '[' in buttons[row - 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column]
                        if '[' in buttons[row][column - 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column]
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                        send_buttons(call.message.chat.id, 'user')
                if row == 7 and column < 7:
                    if buttons[row][column] not in not_zone.not_ships_zone:
                        if '[' in buttons[row - 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1]
                        if '[' in buttons[row][column + 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row - 1][column + 1] + buttons[row - 1][column] + buttons[row][column - 1]
                        if '[' in buttons[row][column - 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row - 1][column + 1] + buttons[row - 1][column] + buttons[row][column - 1]
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                        send_buttons(call.message.chat.id, 'user')
                if row == 7 and column == 7:
                    if buttons[row][column] not in not_zone.not_ships_zone:
                        if '[' in buttons[row - 1][column]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 1][column - 1] + buttons[row][column - 1]
                        if '[' in buttons[row][column - 1]:
                            buttons[row][column] = ']'
                            not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row - 1][column - 1] + buttons[row - 1][column]
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
            if row < 6 and column < 6:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    if '[' in buttons[row + 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 2][column + 1] + buttons[row + 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column] + buttons[row - 1][column + 1]
                    if '[' in buttons[row - 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column] + buttons[row + 1][column + 1]
                    if '[' in buttons[row][column + 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row + 1][column + 2] + buttons[row - 1][column + 1] + buttons[row + 1][column + 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1]
                    if '[' in buttons[row][column - 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column] + buttons[row + 1][column + 1] + buttons[row][column + 1] + buttons[row + 1][column + 1]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
            if row < 7 and column == 7:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    if '[' in buttons[row + 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row + 2][column - 1] + buttons[row + 2][column] + buttons[row + 1][column - 1] + buttons[row][column - 1] + buttons[row - 1][column - 1] + buttons[row - 1][column]
                    if '[' in buttons[row - 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 1][column - 1] + buttons[row][column - 1] + buttons[row + 1][column - 1] + buttons[row + 1][column]
                    if '[' in buttons[row][column - 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row + 1][column - 2] + buttons[row - 1][column - 1] + buttons[row + 1][column - 1] + buttons[row - 1][column] + buttons[row + 1][column]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
            if row == 7 and column < 7:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    if '[' in buttons[row - 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 2][column + 1] + buttons[row - 1][column - 1] + buttons[row][column + 1] + buttons[row][column - 1]
                    if '[' in buttons[row][column + 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row - 1][column + 1] + buttons[row - 1][column] + buttons[row][column - 1]
                    if '[' in buttons[row][column - 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column + 2] + buttons[row][column + 2] + buttons[row - 1][column + 1] + buttons[row - 1][column] + buttons[row][column - 1]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
            if row == 7 and column == 7:
                if buttons[row][column] not in not_zone.not_ships_zone:
                    if '[' in buttons[row - 1][column]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 2][column - 1] + buttons[row - 2][column] + buttons[row - 1][column - 1] + buttons[row][column - 1]
                    if '[' in buttons[row][column - 1]:
                        buttons[row][column] = ']'
                        not_zone.not_ships_zone += buttons[row - 1][column - 2] + buttons[row][column - 2] + buttons[row - 1][column - 1] + buttons[row - 1][column]
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 11:
        if (buttons[row][column] != '[') and (buttons[row][column] != '=') and (buttons[row][column] != ']'):
            if buttons[row][column] not in not_zone.not_ships_zone:
                buttons[row][column] = '['
                bot.delete_message(call.message.chat.id, call.message.message_id)
                send_buttons(call.message.chat.id, 'user')
    if (str(buttons)).count('[') == 12 and (str(buttons)).count(']') == 12:
        bot.send_message(call.message.chat.id, text='Отлично!!! Теперь вам осталось раставить три однопалубных корабля.')
        send_buttons(call.message.chat.id, 'user')
        State_rast.rast_2plbship_2 = False
        State_rast.rast_1plbship = True