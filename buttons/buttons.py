import telebot

from init_bot import bot

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
