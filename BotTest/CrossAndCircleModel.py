# [[telegram_id, telegram_id, game_data, active_player_idx],...] - 0 == 'x' player, 1 == 'o' player, _
# game_data = ["X","O","",...] were indexes
#  0 | 1 | 2
#  3 | 4 | 5
#  6 | 7 | 8
game_data = []
max_players = 2 
#  win conditions
#  0 == 1 == 2, 3 == 4 == 5, 6 == 7 == 8, 0 == 3 == 6, 1 == 4 == 7, 2 == 5 == 8, 0 == 4 == 8, 2 == 4 == 6

def create_new_game(user_one_id, user_two_id):
    # global game_data
    game_data.append([user_one_id, user_two_id, [' ' for idx in range(9)], 0])
    return len(game_data)-1

def add_symbol(game_idx, player_id, coord_idx):
    # проверка на возможность поля
    if game_data[game_idx][2][coord_idx] == ' ':
        # добавляем символ игрока
        if player_id == game_data[game_idx][0]:
            symbol = 'X'
        elif player_id == game_data[game_idx][1]:
            symbol = 'Y'
        game_data[game_idx][2][coord_idx] = symbol
        # меняем активного игрока
        if game_data[game_idx][3] < max_players-1:
            game_data[game_idx][3] += 1
        else:
            game_data[game_idx][3] = 0
        # возвращаем поле
        return True
    else:
        return False

def get_table(game_idx):
    return game_data[game_idx][2]
        
# def check_win(game_table):
#     if game_datas:
#     return False
