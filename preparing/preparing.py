import random

from buttons.buttons import send_buttons
from buttons.buttons_bot import buttons_bot
from init_bot import bot
from states.states import State_rast, rast


@bot.message_handler(commands=['game'])
def prepare_game(message):
    bot.send_message(message.chat.id, text='Перед началом самой игры необходимо раставить ваши корабли на поле. Из-за уменьшеного размера игрового поля, количество подконтрольных кораблей тоже уменьшилось, теперь в вашем распоряжении:\n    Один 3-х палубный корабль;\n    Два 2-х палубных корабля;\n    Три однопалубных корабля.')
    bot.send_message(message.chat.id, text='Для начала установите 3-х палубный корабль, для этого нужно нажать на 3 клетки, лежащие на одной линии и соприкосающиеся друг с другом  (програма расчитана на растановку с слева на право и с верху в низ, пожалуйста, во избежаний графичкских ошибок, начинайте растановку корабля с лева на право или с верху в низ!).')
    send_buttons(message.chat.id, 'user')

    rast.rast_bot = random.choice(['1', '2', '3', '4', '5'])

    def set_symbol(row, col, symbol):
        buttons_bot[row][col] = symbol

    def place_symbols(coords, symbols):
        for coord, symbol in zip(coords, symbols):
            set_symbol(*coord, symbol)
    if rast.rast_bot == '1':
        place_symbols([(0, 0), (7, 7), (7, 0), (3, 1), (4, 1), (4, 6), (5, 6), (6, 2), (6, 3), (6, 4)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast.rast_bot == '2':
        place_symbols([(1, 0), (2, 6), (7, 3), (4, 1), (5, 1), (4, 5), (5, 5), (1, 3), (2, 3), (3, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast.rast_bot == '3':
        place_symbols([(0, 2), (1, 6), (7, 3), (2, 2), (2, 3), (4, 4), (4, 5), (5, 1), (6, 1), (7, 1)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast.rast_bot == '4':
        place_symbols([(1, 1), (5, 1), (7, 2), (1, 6), (2, 6), (6, 4), (6, 5), (2, 3), (3, 3), (4, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    elif rast.rast_bot == '5':
        place_symbols([(1, 6), (4, 1), (4, 3), (4, 6), (5, 6), (6, 3), (6, 4), (2, 1), (2, 2), (2, 3)],
                      ['{}', '{}', '{}', '{', '}', '{', '}', '{', '=', '}'])
    State_rast.rast_3plbship = True
