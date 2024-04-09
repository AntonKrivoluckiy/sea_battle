from buttons.buttons import buttons
from buttons.buttons_bot import buttons_bot
from init_bot import bot
from preparing.preparing import prepare_game
from states.states import not_zone


@bot.message_handler(commands=['restart'])
def restart(message):
    for i in range(8):
        for y in range(8):
            buttons[i][y] = f'{chr(1040 + y)}/{i + 1}'
            buttons_bot[i][y] = f'{chr(1040 + y)}/{i + 1}'

    not_zone.not_ships_zone = ''

    bot.send_message(message.chat.id, 'игра перезапущенна')

    prepare_game(message)
