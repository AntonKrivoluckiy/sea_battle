from battle.attak import attak
from battle.gaming import gaming
from buttons.buttons import buttons, send_buttons
from buttons.buttons_bot import buttons_bot, bot_send_buttons
from init_bot import bot
from states.states import State_game

@bot.callback_query_handler(func=lambda call: State_game.game)
def game(call):
    row_bot, column_bot = map(int, call.data.split())
    if call.data.startswith('user'):
        pass
    else:
        attak(row_bot, column_bot)
        gaming(id=call.message.chat.id)

        if (str(buttons)).count('X') == 10:
            bot.send_message(call.message.chat.id, 'Игра окончена. Вы проиграли, это была хорошая игра, а вы достойнам противником! Не растраивайтесь и поробуйте еще раз, в следующий раз у вас точно получится! Чтобы сыграть еще раз, нажмите /restart')
        if (str(buttons_bot)).count('X') == 10:
            bot.send_message(call.message.chat.id, 'Игра окончена. Вы победили, так держать! Чтобы сыграть еще раз, нажмите /restart')

        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            send_buttons(call.message.chat.id, 'user')
            bot_send_buttons(call.message.chat.id)
