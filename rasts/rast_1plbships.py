import telebot

from buttons.buttons import buttons, send_buttons
from init_bot import bot
from states.states import State_rast, not_zone, State_game, preparing_state


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
            last_question = telebot.util.quick_markup(
                {
                    "Нет": {'callback_data': 'No'},
                    "Да": {'callback_data': 'Yes'}
                }
            )
            bot.send_message(call.message.chat.id, 'Отлично, проверьте еще раз расстановку своих кораблей, она вас устраивает?', reply_markup=last_question)
            State_rast.rast_1plbship = False
            preparing_state.last_question = True


