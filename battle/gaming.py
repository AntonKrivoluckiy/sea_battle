import random

from buttons.buttons import buttons
from sumbols.sumbols import battle_sumbols, ships_sumbols


def gaming():
    rand_row = random.randint(0, 7)
    rand_column = random.randint(0, 7)
    print(rand_row, rand_column)
    if buttons[rand_row][rand_column] not in battle_sumbols:
        if buttons[rand_row][rand_column] not in ships_sumbols:
            buttons[rand_row][rand_column] = '*'
        if buttons[rand_row][rand_column] == '[ ]':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        buttons[rand_row][rand_column] = 'X'
                    elif rand_row + i >= 0 and rand_row + i < len(buttons) and rand_column + j >= 0 and rand_column + j < len(buttons[0]):
                        buttons[rand_row + i][rand_column + j] = '*'
            gaming()
        if buttons[rand_row][rand_column] in ships_sumbols[:2]:
            if (buttons[rand_row - 1][rand_column] in ships_sumbols[:2] or buttons[rand_row + 1][rand_column] in ships_sumbols[:2] or buttons[rand_row][rand_column - 1] in ships_sumbols[:2] or buttons[rand_row][rand_column + 1] in ships_sumbols[:2]) or (buttons[rand_row - 1][rand_column] == 'X' or buttons[rand_row + 1][rand_column] == 'X' or buttons[rand_row][rand_column - 1] == 'X' or buttons[rand_row][rand_column + 1] == 'X'):
                buttons[rand_row][rand_column] = 'X'
                rand_paw = random.choice(['1', '2'])
                if rand_paw == '1':
                    gaming()
                    if buttons[rand_row - 1][rand_column] in ships_sumbols[:2]:
                        buttons[rand_row - 1][rand_column] = 'X'
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
                    gaming()
                if buttons[rand_row - 1][rand_column] == 'X':
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
                if buttons[rand_row + 1][rand_column] == 'X':
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
                if buttons[rand_row][rand_column + 1] == 'X':
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
                if buttons[rand_row][rand_column + 1] == 'X':
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

        if buttons[rand_row][rand_column] in ships_sumbols[3:]:
            if (buttons[rand_row - 2][rand_column] in ships_sumbols[:3] or buttons[rand_row + 2][rand_column] in ships_sumbols[:3] or buttons[rand_row][rand_column - 2] in ships_sumbols[:3] or buttons[rand_row][rand_column + 2] in ships_sumbols[:3]) or (buttons[rand_row - 1][rand_column] in ships_sumbols[:3] or buttons[rand_row + 1][rand_column] in ships_sumbols[:3] or buttons[rand_row][rand_column - 1] in ships_sumbols[:3] or buttons[rand_row][rand_column + 1] in ships_sumbols[:3]) or (buttons[rand_row - 1][rand_column] == 'X' or buttons[rand_row + 1][rand_column] == 'X' or buttons[rand_row][rand_column - 1] == 'X' or buttons[rand_row][rand_column + 1] == 'X') or (buttons[rand_row - 2][rand_column] == 'X' or buttons[rand_row + 2][rand_column] == 'X' or buttons[rand_row][rand_column - 2] == 'X' or buttons[rand_row][rand_column + 2] == 'X'):
                buttons[rand_row][rand_column] = 'X'
                gaming()
                if buttons[rand_row - 1][rand_column] == 'X' and buttons[rand_row - 2][rand_column] == 'X':
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
                if buttons[rand_row + 1][rand_column] == 'X' and buttons[rand_row + 2][rand_column] == 'X':
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
                if buttons[rand_row - 1][rand_column] == 'X' and buttons[rand_row + 1][rand_column] == 'X':
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
                if buttons[rand_row][rand_column - 1] == 'X' and buttons[rand_row][rand_column - 2] == 'X':
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
                if buttons[rand_row][rand_column + 1] == 'X' and buttons[rand_row][rand_column + 2] == 'X':
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
                if buttons[rand_row][rand_column - 1] == 'X' and buttons[rand_row][rand_column + 1] == 'X':
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
        gaming()
