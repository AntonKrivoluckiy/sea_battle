import telebot

from init_bot import bot


@bot.message_handler(commands=['start'])
def hello(message: telebot.types.Message):
    text = ('Привет, как можно понять из названия бота, весь его функционал - играть в "Морсой Бой".'
            '\nДля начала игры нужно использовать команду: /rules'
            '\nДля прочих функций используйте встроеную клавиатуру.'
            '\n!!!ВАЖНО!!! Игра не расчитана для игры через телефон, если вы используете его, пожалуйста перейдите на компьютер')
    bot.send_message(message.chat.id, text)
