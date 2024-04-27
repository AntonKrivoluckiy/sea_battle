import telebot

from init_bot import bot

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