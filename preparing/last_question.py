from battle.restart import restart
from buttons.buttons import send_buttons
from buttons.buttons_bot import bot_send_buttons
from init_bot import bot
from states.states import preparing_state, State_game


@bot.callback_query_handler(func=lambda call: preparing_state.last_question)
def last_question(call):
    if call.data == 'No':
        preparing_state.last_question = False
        restart(call.message)
    if call.data == 'Yes':
        preparing_state.last_question = False
        send_buttons(call.message.chat.id, 'user')
        bot_send_buttons(call.message.chat.id)
        State_game.game = True
