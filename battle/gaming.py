import random

from buttons.buttons import buttons
from init_bot import bot
from sumbols.sumbols import battle_sumbols, ships_sumbols


def gaming(id):
    rand_row = random.randint(0, 7)
    rand_column = random.randint(0, 7)
    cord_1 = rand_row + 1
    cord_2 = ''
    if rand_column == 0:
        cord_2 = 'A'
    if rand_column == 1:
        cord_2 = 'Б'
    if rand_column == 2:
        cord_2 = 'В'
    if rand_column == 3:
        cord_2 = 'Г'
    if rand_column == 4:
        cord_2 = 'Д'
    if rand_column == 5:
        cord_2 = 'Е'
    if rand_column == 6:
        cord_2 = 'Ж'
    if rand_column == 7:
        cord_2 = 'З'
    if buttons[rand_row][rand_column] not in battle_sumbols:
        if buttons[rand_row][rand_column] not in ships_sumbols:
            bot.send_message(id, f'Бот промахнулся, выстрелив на {cord_2}/{cord_1}')
            buttons[rand_row][rand_column] = '*'
        if buttons[rand_row][rand_column] == '[ ]':
            bot.send_message(id, f'Бот потопил ваш Боевой катер выстрелом на {cord_2}/{cord_1}')
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        buttons[rand_row][rand_column] = 'X'
                    elif rand_row + i >= 0 and rand_row + i < len(buttons) and rand_column + j >= 0 and rand_column + j < len(buttons[0]):
                        buttons[rand_row + i][rand_column + j] = '*'
            gaming(id)
        if buttons[rand_row][rand_column] in ships_sumbols[:2]:
            if (buttons[rand_row - 1][rand_column] in ships_sumbols[:2] or buttons[rand_row + 1][rand_column] in ships_sumbols[:2] or buttons[rand_row][rand_column - 1] in ships_sumbols[:2] or buttons[rand_row][rand_column + 1] in ships_sumbols[:2]) or (buttons[rand_row - 1][rand_column] == 'X' or buttons[rand_row + 1][rand_column] == 'X' or buttons[rand_row][rand_column - 1] == 'X' or buttons[rand_row][rand_column + 1] == 'X'):
                rand_paw = random.choice(['1', '1', '2'])
                if rand_paw == '1':
                    bot.send_message(id, f'Бот взорвал ваш Линкор, одна часть которого находится на координатах: {cord_2}/{cord_1}, после второго выстрела корабль был полностью уничтожен')
                    gaming(id)
                    if buttons[rand_row - 1][rand_column] in ships_sumbols[:2]:
                        buttons[rand_row - 1][rand_column] = 'X'
                        buttons[rand_row][rand_column] = 'X'
                        if rand_column - 1 > 0:
                            buttons[rand_row - 2][rand_column - 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row - 2][rand_column] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row - 2][rand_column + 1] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row - 1][rand_column - 1] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row - 1][rand_column + 1] = ' * '
                        if rand_column < len(buttons[0]):
                            buttons[rand_row][rand_column - 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row][rand_column + 1] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column - 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row + 1][rand_column] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column + 1] = ' * '
                    if buttons[rand_row + 1][rand_column] in ships_sumbols[:2]:
                        buttons[rand_row + 1][rand_column] = 'X'
                        buttons[rand_row][rand_column] = 'X'
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 2][rand_column + 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row + 2][rand_column] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row + 2][rand_column - 1] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column + 1] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row + 1][rand_column - 1] = ' * '
                        if rand_column < len(buttons[0]):
                            buttons[rand_row][rand_column + 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row][rand_column - 1] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row - 1][rand_column + 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row - 1][rand_column] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row - 1][rand_column - 1] = ' * '
                    if buttons[rand_row][rand_column - 1] in ships_sumbols[:2]:
                        buttons[rand_row][rand_column - 1] = 'X'
                        buttons[rand_row][rand_column] = 'X'
                        if rand_column - 2 > 0:
                            buttons[rand_row - 1][rand_column - 2] = ' * '
                        if rand_column - 2 < len(buttons[0]):
                            buttons[rand_row][rand_column - 2] = ' * '
                        if rand_column - 2 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column - 2] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row - 1][rand_column - 1] = ' * '
                        if rand_column - 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column - 1] = ' * '
                        if rand_column > 0:
                            buttons[rand_row - 1][rand_column] = ' * '
                        if rand_column < len(buttons[0]):
                            buttons[rand_row + 1][rand_column] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row - 1][rand_column + 1] = ' * '
                        if rand_column + 1 > 0:
                            buttons[rand_row][rand_column + 1] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column + 1] = ' * '
                    if buttons[rand_row][rand_column + 1] in ships_sumbols[:2]:
                        buttons[rand_row][rand_column + 1] = 'X'
                        buttons[rand_row][rand_column] = 'X'
                        if rand_column + 2 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column + 2] = ' * '
                        if rand_column + 2 > 0:
                            buttons[rand_row - 1][rand_column + 2] = ' * '
                        if rand_column + 1 < len(buttons[0]):
                            buttons[rand_row + 1][rand_column + 1] = ' * '
                        if rand_column + 1 > 0:
                            buttons[rand_row - 1][rand_column + 1] = ' * '
                        if rand_column < len(buttons[0]):
                            buttons[rand_row + 1][rand_column] = ' * '
                        if rand_column > 0:
                            buttons[rand_row - 1][rand_column] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row + 1][rand_column - 1] = ' * '
                        if rand_column - 1 < len(buttons[0]):
                            buttons[rand_row][rand_column - 1] = ' * '
                        if rand_column - 1 > 0:
                            buttons[rand_row - 1][rand_column - 1] = ' * '
                else:
                    buttons[rand_row][rand_column] = 'X'
                    bot.send_message(id, f'Бот попал, по вашему Линкору, что стоял на координатах: {cord_2}/{cord_1}, из-за плохой видимости он потерял горящие остатки')
                    gaming(id)
                if buttons[rand_row - 1][rand_column] in battle_sumbols[0]:
                    bot.send_message(id, f'Противник нашел и потопил остатки вашего Линкора, стоящего на координетах: {cord_2}/{cord_1}')
                    if rand_column - 1 > 0:
                        buttons[rand_row - 2][rand_column - 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row - 2][rand_column] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row - 2][rand_column + 1] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row - 1][rand_column - 1] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row - 1][rand_column + 1] = ' * '
                    if rand_column < len(buttons[0]):
                        buttons[rand_row][rand_column - 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row][rand_column + 1] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column - 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row + 1][rand_column] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 1] = ' * '
                if buttons[rand_row + 1][rand_column] in battle_sumbols[0]:
                    bot.send_message(id, f'Противник нашел и потопил остатки вашего Линкора, стоящего на координетах: {cord_2}/{cord_1}')
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 2][rand_column + 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row + 2][rand_column] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row + 2][rand_column - 1] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 1] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row + 1][rand_column - 1] = ' * '
                    if rand_column < len(buttons[0]):
                        buttons[rand_row][rand_column + 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row][rand_column - 1] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row - 1][rand_column + 1] = ' * '
                    if rand_column > 0:
                        buttons[rand_row - 1][rand_column] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row - 1][rand_column - 1] = ' * '
                if buttons[rand_row][rand_column + 1] in battle_sumbols[0]:
                    bot.send_message(id, f'Противник нашел и потопил остатки вашего Линкора, стоящего на координетах: {cord_2}/{cord_1}')
                    if rand_column + 2 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 2] = ' * '
                    if rand_column + 2 > 0:
                        buttons[rand_row - 1][rand_column + 2] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 1] = ' * '
                    if rand_column + 1 > 0:
                        buttons[rand_row - 1][rand_column + 1] = ' * '
                    if rand_column < len(buttons[0]):
                        buttons[rand_row + 1][rand_column] = ' * '
                    if rand_column > 0:
                        buttons[rand_row - 1][rand_column] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row + 1][rand_column - 1] = ' * '
                    if rand_column - 1 < len(buttons[0]):
                        buttons[rand_row][rand_column - 1] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row - 1][rand_column - 1] = ' * '
                if buttons[rand_row][rand_column + 1] in battle_sumbols[0]:
                    bot.send_message(id, f'Противник нашел и потопил остатки вашего Линкора, стоящего на координетах: {cord_2}/{cord_1}')
                    if rand_column + 2 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 2] = ' * '
                    if rand_column + 2 > 0:
                        buttons[rand_row - 1][rand_column + 2] = ' * '
                    if rand_column + 1 < len(buttons[0]):
                        buttons[rand_row + 1][rand_column + 1] = ' * '
                    if rand_column + 1 > 0:
                        buttons[rand_row - 1][rand_column + 1] = ' * '
                    if rand_column < len(buttons[0]):
                        buttons[rand_row + 1][rand_column] = ' * '
                    if rand_column > 0:
                        buttons[rand_row - 1][rand_column] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row + 1][rand_column - 1] = ' * '
                    if rand_column - 1 < len(buttons[0]):
                        buttons[rand_row][rand_column - 1] = ' * '
                    if rand_column - 1 > 0:
                        buttons[rand_row - 1][rand_column - 1] = ' * '

        elif buttons[rand_row][rand_column] in ships_sumbols[3:]:
            bot.send_message(id, f'Бот полностью потопил ваш Эсминец, который стоял на координатах {cord_2}/{cord_1}')
            if buttons[rand_row - 1][rand_column] in ships_sumbols[:3] and buttons[rand_row - 2][rand_column] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row - 1][rand_column] = 'X'
                buttons[rand_row - 2][rand_column] = 'X'
                buttons[rand_row - 3][rand_column - 1] = '*'
                buttons[rand_row - 3][rand_column] = '*'
                buttons[rand_row - 3][rand_column + 1] = '*'
                buttons[rand_row - 2][rand_column - 1] = '*'
                buttons[rand_row - 2][rand_column + 1] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row][rand_column - 1] = '*'
                buttons[rand_row][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
            if buttons[rand_row - 1][rand_column] in ships_sumbols[:3] and buttons[rand_row + 1][rand_column] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row - 1][rand_column] = 'X'
                buttons[rand_row + 1][rand_column] = 'X'
                buttons[rand_row - 2][rand_column - 1] = '*'
                buttons[rand_row - 2][rand_column] = '*'
                buttons[rand_row - 2][rand_column + 1] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row][rand_column + 1] = '*'
                buttons[rand_row][rand_column - 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
                buttons[rand_row + 2][rand_column - 1] = '*'
                buttons[rand_row + 2][rand_column] = '*'
                buttons[rand_row + 2][rand_column + 1] = '*'
            if buttons[rand_row + 1][rand_column] in ships_sumbols[:3] and buttons[rand_row + 2][rand_column] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row + 1][rand_column] = 'X'
                buttons[rand_row + 2][rand_column] = 'X'
                buttons[rand_row + 3][rand_column - 1] = '*'
                buttons[rand_row + 3][rand_column] = '*'
                buttons[rand_row + 3][rand_column + 1] = '*'
                buttons[rand_row + 2][rand_column - 1] = '*'
                buttons[rand_row + 2][rand_column + 2] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
                buttons[rand_row][rand_column + 1] = '*'
                buttons[rand_row][rand_column - 1] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row - 1][rand_column] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
            if buttons[rand_row][rand_column - 1] in ships_sumbols[:3] and buttons[rand_row][rand_column - 2] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row][rand_column - 1] = 'X'
                buttons[rand_row][rand_column - 2] = 'X'
                buttons[rand_row - 1][rand_column - 3] = '*'
                buttons[rand_row][rand_column - 3] = '*'
                buttons[rand_row + 1][rand_column - 3] = '*'
                buttons[rand_row - 1][rand_column - 2] = '*'
                buttons[rand_row + 1][rand_column - 2] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
                buttons[rand_row - 1][rand_column] = '*'
                buttons[rand_row + 1][rand_column] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
            if buttons[rand_row][rand_column + 1] in ships_sumbols[:3] and buttons[rand_row][rand_column + 2] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row][rand_column + 1] = 'X'
                buttons[rand_row][rand_column + 2] = 'X'
                buttons[rand_row - 1][rand_column + 3] = '*'
                buttons[rand_row][rand_column + 3] = '*'
                buttons[rand_row + 1][rand_column + 3] = '*'
                buttons[rand_row - 1][rand_column + 2] = '*'
                buttons[rand_row + 1][rand_column + 2] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
                buttons[rand_row - 1][rand_column] = '*'
                buttons[rand_row + 1][rand_column] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
                buttons[rand_row][rand_column - 1] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
            if buttons[rand_row][rand_column - 1] in ships_sumbols[:3] and buttons[rand_row][rand_column + 1] in ships_sumbols[:3]:
                buttons[rand_row][rand_column] = 'X'
                buttons[rand_row][rand_column - 1] = 'X'
                buttons[rand_row][rand_column + 1] = 'X'
                buttons[rand_row - 1][rand_column + 2] = '*'
                buttons[rand_row][rand_column + 2] = '*'
                buttons[rand_row + 1][rand_column + 2] = '*'
                buttons[rand_row - 1][rand_column + 1] = '*'
                buttons[rand_row + 1][rand_column + 1] = '*'
                buttons[rand_row - 1][rand_column] = '*'
                buttons[rand_row + 1][rand_column] = '*'
                buttons[rand_row - 1][rand_column - 1] = '*'
                buttons[rand_row + 1][rand_column - 1] = '*'
                buttons[rand_row - 1][rand_column - 2] = '*'
                buttons[rand_row][rand_column - 2] = '*'
                buttons[rand_row + 1][rand_column - 2] = '*'
    else:
        gaming(id)
