from buttons.buttons_bot import buttons_bot
from preparing.preparing import prepare_game
from states.states import rast


def attak(row_bot, column_bot):
    if buttons_bot[row_bot][column_bot] != '*':
        if rast.rast_bot == '1':
            if row_bot == 0 and column_bot == 0:
                buttons_bot[row_bot][column_bot] = 'X'
                buttons_bot[1][1] = '*'
                buttons_bot[0][1] = '*'
                buttons_bot[1][0] = '*'
            if row_bot == 7 and column_bot == 7:
                buttons_bot[row_bot][column_bot] = 'X'
                buttons_bot[6][7] = ' * '
                buttons_bot[6][6] = ' * '
                buttons_bot[7][6] = ' * '
            if row_bot == 7 and column_bot == 0:
                buttons_bot[row_bot][column_bot] = 'X'
                buttons_bot[6][0] = '*'
                buttons_bot[6][1] = '*'
                buttons_bot[7][1] = '*'
            if row_bot == 3 and column_bot == 1:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[4][1] == 'X':
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][1] = '*'
                    buttons_bot[5][2] = '*'
            if row_bot == 4 and column_bot == 1:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[3][1] == 'X':
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][1] = '*'
                    buttons_bot[5][2] = '*'
            if row_bot == 4 and column_bot == 6:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[5][6] == 'X':
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[4][7] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][7] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[6][7] = '*'
            if row_bot == 5 and column_bot == 6:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[4][6] == 'X':
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[4][7] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][7] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[6][7] = '*'
            if row_bot == 6 and column_bot == 2:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[6][3] == 'X' and buttons_bot[6][4] == 'X':
                    buttons_bot[5][1] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[7][1] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[7][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[7][5] = '*'
            if row_bot == 6 and column_bot == 3:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[6][2] == 'X' and buttons_bot[6][4] == 'X':
                    buttons_bot[5][1] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[7][1] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[7][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[7][5] = '*'
            if row_bot == 6 and column_bot == 4:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[6][3] == 'X' and buttons_bot[6][2] == 'X':
                    buttons_bot[5][1] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[7][1] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[7][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[7][5] = '*'
            if not (row_bot == 0 and column_bot == 0) and not (row_bot == 7 and column_bot == 7) and not (
                    row_bot == 7 and column_bot == 0) and not (row_bot == 3 and column_bot == 1) and not (
                    row_bot == 4 and column_bot == 1) and not (row_bot == 4 and column_bot == 6) and not (
                    row_bot == 5 and column_bot == 6) and not (row_bot == 6 and column_bot == 2) and not (
                    row_bot == 6 and column_bot == 3) and not (row_bot == 6 and column_bot == 4):
                buttons_bot[row_bot][column_bot] = '*'
        if rast.rast_bot == ('2'):
            if row_bot == 1 and column_bot == 0:
                buttons_bot[1][0] = 'X'
                buttons_bot[0][0] = '*'
                buttons_bot[0][1] = '*'
                buttons_bot[1][1] = '*'
                buttons_bot[2][1] = '*'
                buttons_bot[2][0] = '*'
            if row_bot == 2 and column_bot == 6:
                buttons_bot[2][6] = 'X'
                buttons_bot[1][5] = '*'
                buttons_bot[1][6] = '*'
                buttons_bot[1][7] = '*'
                buttons_bot[2][5] = '*'
                buttons_bot[2][7] = '*'
                buttons_bot[3][5] = '*'
                buttons_bot[3][6] = '*'
                buttons_bot[3][7] = '*'
            if row_bot == 7 and column_bot == 3:
                buttons_bot[7][3] = 'X'
                buttons_bot[7][2] = '*'
                buttons_bot[6][2] = '*'
                buttons_bot[6][3] = '*'
                buttons_bot[6][4] = '*'
                buttons_bot[7][4] = '*'
            if row_bot == 4 and column_bot == 1:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[5][1] == 'X':
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[6][2] = '*'
            if row_bot == 5 and column_bot == 1:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[4][1] == 'X':
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[6][1] = '*'
                    buttons_bot[6][2] = '*'
            if row_bot == 4 and column_bot == 5:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[5][5] == 'X':
                    buttons_bot[3][4] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[4][6] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][6] = '*'
                    buttons_bot[6][4] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
            if row_bot == 5 and column_bot == 5:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[4][5] == 'X':
                    buttons_bot[3][4] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[4][6] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][6] = '*'
                    buttons_bot[6][4] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
            if row_bot == 1 and column_bot == 3:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[2][3] == 'X' and buttons_bot[3][3] == 'X':
                    buttons_bot[0][2] = '*'
                    buttons_bot[0][3] = '*'
                    buttons_bot[0][4] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][3] = '*'
                    buttons_bot[4][4] = '*'
            if row_bot == 2 and column_bot == 3:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[1][3] == 'X' and buttons_bot[3][3] == 'X':
                    buttons_bot[0][2] = '*'
                    buttons_bot[0][3] = '*'
                    buttons_bot[0][4] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][3] = '*'
                    buttons_bot[4][4] = '*'
            if row_bot == 3 and column_bot == 3:
                buttons_bot[row_bot][column_bot] = 'X'
                if buttons_bot[2][3] == 'X' and buttons_bot[1][3] == 'X':
                    buttons_bot[0][2] = '*'
                    buttons_bot[0][3] = '*'
                    buttons_bot[0][4] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][3] = '*'
                    buttons_bot[4][4] = '*'
            if not (row_bot == 1 and column_bot == 0) and not (row_bot == 2 and column_bot == 6) and not (
                    row_bot == 7 and column_bot == 3) and not (row_bot == 4 and column_bot == 1) and not (
                    row_bot == 5 and column_bot == 1) and not (row_bot == 4 and column_bot == 5) and not (
                    row_bot == 5 and column_bot == 5) and not (row_bot == 1 and column_bot == 3) and not (
                    row_bot == 2 and column_bot == 3) and not (row_bot == 3 and column_bot == 3):
                buttons_bot[row_bot][column_bot] = '*'
        if rast.rast_bot == '3':
            if row_bot == 2 and column_bot == 0:
                buttons_bot[2][0] = 'X'
                buttons_bot[1][0] = '*'
                buttons_bot[1][1] = '*'
                buttons_bot[2][1] = '*'
                buttons_bot[3][0] = '*'
                buttons_bot[3][1] = '*'
            if row_bot == 1 and column_bot == 6:
                buttons_bot[1][6] = 'X'
                buttons_bot[0][5] = '*'
                buttons_bot[0][6] = '*'
                buttons_bot[0][7] = '*'
                buttons_bot[1][5] = '*'
                buttons_bot[1][7] = '*'
                buttons_bot[2][5] = '*'
                buttons_bot[2][6] = '*'
                buttons_bot[2][7] = '*'
            if row_bot == 3 and column_bot == 7:
                buttons_bot[3][7] = 'X'
                buttons_bot[2][7] = '*'
                buttons_bot[2][6] = '*'
                buttons_bot[3][6] = '*'
                buttons_bot[4][6] = '*'
                buttons_bot[4][7] = '*'
            if row_bot == 2 and column_bot == 2:
                buttons_bot[2][2] = 'X'
                if buttons_bot[3][2] == 'X':
                    buttons_bot[1][1] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][3] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][3] = '*'
            if row_bot == 3 and column_bot == 2:
                buttons_bot[3][2] = 'X'
                if buttons_bot[2][2] == 'X':
                    buttons_bot[1][1] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[2][1] = '*'
                    buttons_bot[2][3] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][3] = '*'
            if row_bot == 4 and column_bot == 4:
                buttons_bot[4][4] = 'X'
                if buttons_bot[5][4] == 'X':
                    buttons_bot[3][3] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[4][3] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[6][4] = '*'
                    buttons_bot[6][5] = '*'
            if row_bot == 5 and column_bot == 4:
                buttons_bot[5][4] = 'X'
                if buttons_bot[4][4] == 'X':
                    buttons_bot[3][3] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[4][3] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[6][4] = '*'
                    buttons_bot[6][5] = '*'
            if row_bot == 5 and column_bot == 1:
                buttons_bot[5][1] = 'X'
                if buttons_bot[6][1] == 'X' and buttons_bot[7][1] == 'X':
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[7][0] = '*'
                    buttons_bot[7][2] = '*'
            if row_bot == 6 and column_bot == 1:
                buttons_bot[6][1] = 'X'
                if buttons_bot[5][1] == 'X' and buttons_bot[7][1] == 'X':
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[7][0] = '*'
                    buttons_bot[7][2] = '*'
            if row_bot == 7 and column_bot == 1:
                buttons_bot[7][1] = 'X'
                if buttons_bot[5][1] == 'X' and buttons_bot[6][1] == 'X':
                    buttons_bot[4][0] = '*'
                    buttons_bot[4][1] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[5][0] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[6][0] = '*'
                    buttons_bot[6][2] = '*'
                    buttons_bot[7][0] = '*'
                    buttons_bot[7][2] = '*'
            if not (row_bot == 2 and column_bot == 0) and not (row_bot == 1 and column_bot == 6) and not (
                    row_bot == 3 and column_bot == 7) and not (row_bot == 2 and column_bot == 2) and not (
                    row_bot == 3 and column_bot == 2) and not (row_bot == 4 and column_bot == 4) and not (
                    row_bot == 5 and column_bot == 4) and not (row_bot == 5 and column_bot == 1) and not (
                    row_bot == 6 and column_bot == 1) and not (row_bot == 7 and column_bot == 1):
                buttons_bot[row_bot][column_bot] = '*'
        if rast.rast_bot == '4':
            if row_bot == 1 and column_bot == 1:
                buttons_bot[1][1] = 'X'
                buttons_bot[0][0] = '*'
                buttons_bot[0][1] = '*'
                buttons_bot[0][2] = '*'
                buttons_bot[1][0] = '*'
                buttons_bot[1][2] = '*'
                buttons_bot[2][0] = '*'
                buttons_bot[2][1] = '*'
                buttons_bot[2][2] = '*'
            if row_bot == 5 and column_bot == 1:
                buttons_bot[5][1] = 'X'
                buttons_bot[4][0] = '*'
                buttons_bot[4][1] = '*'
                buttons_bot[4][2] = '*'
                buttons_bot[5][0] = '*'
                buttons_bot[5][2] = '*'
                buttons_bot[6][0] = '*'
                buttons_bot[6][1] = '*'
                buttons_bot[6][2] = '*'
            if row_bot == 7 and column_bot == 2:
                buttons_bot[7][2] = 'X'
                buttons_bot[7][1] = '*'
                buttons_bot[6][1] = '*'
                buttons_bot[6][2] = '*'
                buttons_bot[6][3] = '*'
                buttons_bot[7][3] = '*'
            if row_bot == 6 and column_bot == 4:
                buttons_bot[6][4] = 'X'
                if buttons_bot[6][5] == 'X':
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][6] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[7][5] = '*'
                    buttons_bot[7][6] = '*'
            if row_bot == 6 and column_bot == 5:
                buttons_bot[6][5] = 'X'
                if buttons_bot[6][4] == 'X':
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][6] = '*'
                    buttons_bot[6][3] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[7][5] = '*'
                    buttons_bot[7][6] = '*'
            if row_bot == 1 and column_bot == 6:
                buttons_bot[1][6] = 'X'
                if buttons_bot[2][6] == 'X':
                    buttons_bot[0][5] = '*'
                    buttons_bot[0][6] = '*'
                    buttons_bot[0][7] = '*'
                    buttons_bot[1][5] = '*'
                    buttons_bot[1][7] = '*'
                    buttons_bot[2][5] = '*'
                    buttons_bot[2][7] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
            if row_bot == 2 and column_bot == 6:
                buttons_bot[2][6] = 'X'
                if buttons_bot[1][6] == 'X':
                    buttons_bot[0][5] = '*'
                    buttons_bot[0][6] = '*'
                    buttons_bot[0][7] = '*'
                    buttons_bot[1][5] = '*'
                    buttons_bot[1][7] = '*'
                    buttons_bot[2][5] = '*'
                    buttons_bot[2][7] = '*'
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
            if row_bot == 2 and column_bot == 3:
                buttons_bot[2][3] = 'X'
                if buttons_bot[3][3] == 'X' and buttons_bot[4][3] == 'X':
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
            if row_bot == 3 and column_bot == 3:
                buttons_bot[3][3] = 'X'
                if buttons_bot[2][3] == 'X' and buttons_bot[4][3] == 'X':
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
            if row_bot == 4 and column_bot == 3:
                buttons_bot[4][3] = 'X'
                if buttons_bot[3][3] == 'X' and buttons_bot[2][3] == 'X':
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][2] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][4] = '*'
                    buttons_bot[4][2] = '*'
                    buttons_bot[4][4] = '*'
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
            if not (row_bot == 1 and column_bot == 1) and not (row_bot == 5 and column_bot == 1) and not (
                    row_bot == 7 and column_bot == 2) and not (row_bot == 6 and column_bot == 4) and not (
                    row_bot == 6 and column_bot == 5) and not (row_bot == 1 and column_bot == 6) and not (
                    row_bot == 2 and column_bot == 6) and not (row_bot == 2 and column_bot == 3) and not (
                    row_bot == 3 and column_bot == 3) and not (row_bot == 4 and column_bot == 3):
                buttons_bot[row_bot][column_bot] = '*'
        if rast.rast_bot == '5':
            if row_bot == 1 and column_bot == 6:
                buttons_bot[1][6] = 'X'
                buttons_bot[0][5] = '*'
                buttons_bot[0][6] = '*'
                buttons_bot[0][7] = '*'
                buttons_bot[1][5] = '*'
                buttons_bot[1][7] = '*'
                buttons_bot[2][5] = '*'
                buttons_bot[2][6] = '*'
                buttons_bot[2][7] = '*'
            if row_bot == 4 and column_bot == 1:
                buttons_bot[4][1] = 'X'
                buttons_bot[3][0] = '*'
                buttons_bot[3][1] = '*'
                buttons_bot[3][2] = '*'
                buttons_bot[4][0] = '*'
                buttons_bot[4][2] = '*'
                buttons_bot[5][0] = '*'
                buttons_bot[5][1] = '*'
                buttons_bot[5][2] = '*'
            if row_bot == 4 and column_bot == 3:
                buttons_bot[4][3] = 'X'
                buttons_bot[3][2] = '*'
                buttons_bot[3][3] = '*'
                buttons_bot[4][2] = '*'
                buttons_bot[4][4] = '*'
                buttons_bot[5][2] = '*'
                buttons_bot[5][3] = '*'
                buttons_bot[5][4] = '*'
            if row_bot == 4 and column_bot == 6:
                buttons_bot[4][6] = 'X'
                if buttons_bot[5][6] == 'X':
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[4][7] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][7] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[6][7] = '*'
            if row_bot == 5 and column_bot == 6:
                buttons_bot[5][6] = 'X'
                if buttons_bot[4][6] == 'X':
                    buttons_bot[3][5] = '*'
                    buttons_bot[3][6] = '*'
                    buttons_bot[3][7] = '*'
                    buttons_bot[4][5] = '*'
                    buttons_bot[4][7] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[5][7] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[6][6] = '*'
                    buttons_bot[6][7] = '*'
            if row_bot == 6 and column_bot == 3:
                buttons_bot[6][3] = 'X'
                if buttons_bot[6][4] == 'X':
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][2] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[7][2] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[7][5] = '*'
            if row_bot == 6 and column_bot == 4:
                buttons_bot[6][4] = 'X'
                if buttons_bot[6][3] == 'X':
                    buttons_bot[5][2] = '*'
                    buttons_bot[5][3] = '*'
                    buttons_bot[5][4] = '*'
                    buttons_bot[5][5] = '*'
                    buttons_bot[6][2] = '*'
                    buttons_bot[6][5] = '*'
                    buttons_bot[7][2] = '*'
                    buttons_bot[7][3] = '*'
                    buttons_bot[7][4] = '*'
                    buttons_bot[7][5] = '*'
            if row_bot == 2 and column_bot == 1:
                buttons_bot[2][1] = 'X'
                if buttons_bot[2][2] == 'X' and buttons_bot[2][3] == 'X':
                    buttons_bot[1][0] = '*'
                    buttons_bot[1][1] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[3][4] = '*'
            if row_bot == 2 and column_bot == 2:
                buttons_bot[2][2] = 'X'
                if buttons_bot[2][1] == 'X' and buttons_bot[2][3] == 'X':
                    buttons_bot[1][0] = '*'
                    buttons_bot[1][1] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[3][4] = '*'
            if row_bot == 2 and column_bot == 3:
                buttons_bot[2][3] = 'X'
                if buttons_bot[2][2] == 'X' and buttons_bot[2][1] == 'X':
                    buttons_bot[1][0] = '*'
                    buttons_bot[1][1] = '*'
                    buttons_bot[1][2] = '*'
                    buttons_bot[1][3] = '*'
                    buttons_bot[1][4] = '*'
                    buttons_bot[2][0] = '*'
                    buttons_bot[2][4] = '*'
                    buttons_bot[3][0] = '*'
                    buttons_bot[3][1] = '*'
                    buttons_bot[3][2] = '*'
                    buttons_bot[3][3] = '*'
                    buttons_bot[3][4] = '*'
            if not (row_bot == 1 and column_bot == 6) and not (row_bot == 4 and column_bot == 1) and not (
                    row_bot == 4 and column_bot == 3) and not (row_bot == 4 and column_bot == 6) and not (
                    row_bot == 5 and column_bot == 6) and not (row_bot == 6 and column_bot == 3) and not (
                    row_bot == 6 and column_bot == 4) and not (row_bot == 2 and column_bot == 1) and not (
                    row_bot == 2 and column_bot == 2) and not (row_bot == 2 and column_bot == 3):
                buttons_bot[row_bot][column_bot] = '*'
