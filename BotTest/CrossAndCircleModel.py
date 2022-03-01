import random

# games = (game_id, game_id...) - список указателей на игры, просто инкрементарный без сброса значений (на данный момент кол-во сессий не удёт в безлимит), в реальности желателен совсем уникальный ключ который очень долго не повтроится (тогда можно хранить логи за все время жизни)
# games_data = {'game_id': 
#                       {'player_1_message_link':(chat_id, message_id),             # - первый линк играет за крестики (шафлим после старта игры)
#                        'player_2_message_link':(chat_id, message_id),             # - второй линк играет за нолики   (шафлим после старта игры)
#                        'game_table': ['','','','','','','','',''], 
#                        'current_player': 1..2}}

# game_table = 0 | 1 | 2
#              3 | 4 | 5
#              6 | 7 | 8

games = set()
games_data = {}
pending_game_id = 0 # == False

# GAMEPLAY 

# return False or winning symbol
def check_win(game_table): 
    #  rows: 0 == 1 == 2, 3 == 4 == 5, 6 == 7 == 8, 
    #  columns: 0 == 3 == 6, 1 == 4 == 7, 2 == 5 == 8
    #  diagonals: 0 == 4 == 8, 2 == 4 == 6
    check_lines = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])
    for line in check_lines:
        first_cell = game_table[line[0]]
        second_cell = game_table[line[1]]
        third_cell = game_table[line[2]]
        if check_non_empty_similar_three(first_cell,second_cell,third_cell):
            return first_cell
    return False

def check_non_empty_similar_three(one,two,three):
    if one == two == three != ' ':
        return True
    return False

def add_symbol(game_idx, player_id, coord_idx):
    # проверка на возможность поля
    if games_data[game_idx][2][coord_idx] == ' ':
        # добавляем символ игрока
        if player_id == games_data[game_idx][0]:
            symbol = 'X'
        elif player_id == games_data[game_idx][1]:
            symbol = 'Y'
        games_data[game_idx][2][coord_idx] = symbol
        # меняем активного игрока
        if games_data[game_idx][3] < max_players-1:
            games_data[game_idx][3] += 1
        else:
            games_data[game_idx][3] = 0
        # возвращаем поле
        return True
    else:
        return False


# WORKING WITH GAME DATA
# get pending game id if exists. If not create new game. For game with bot always create new game
def add_game_data(key, data, game_id):
    games_data[game_id][key] = data

def get_game_data(key, game_id):
    return games_data[game_id][key]

def get_game_id(bot_game = False):
    if pending_game_id and not bot_game:
        id = pending_game_id
        pending_game_id = 0
        is_new_game = False
    else:
        id = max(games)+1 if len(games) else 0
        games.add(id)
        create_new_game(id)
        pending_game_id = id
        is_new_game = True
    return id, is_new_game

def create_new_game(game_id):
    games_data[game_id] = {}
    add_game_data('game_table', [' ' for e in range(9)], game_id)

def add_player_to_game(player_number, chat_id, message_id, game_id):
    add_game_data(f'player_{player_number}_message_link', (chat_id, message_id), game_id)

def add_bot_to_game(game_id):
    player_number = 2; bot_chat_id = 0; bot_message_id = 0
    add_game_data(f'player_{player_number}_message_link', (bot_chat_id, bot_message_id), game_id)

def join_game(chat_id, message_id, bot_game = False):
    if bot_game:
        game_id, is_new_game = get_game_id(bot_game = True)
        player_number = 1
        add_player_to_game(player_number,chat_id,message_id,game_id)
        add_bot_to_game(game_id)
    else:
        game_id, is_new_game = get_game_id()
        player_number = 1 if is_new_game else 2
        add_player_to_game(player_number,chat_id,message_id,game_id)
    # returning to write in playerhandler
    return game_id

def start_game(game_id):
    # randomizing 'X' and 'O' player
    if random.random() > 0.5:
        games_data[game_id]['player_1_message_link'], games_data[game_id]['player_2_message_link'] = games_data[game_id]['player_2_message_link'], games_data[game_id]['player_1_message_link']
    add_game_data('current_player', 1, game_id)    

def get_message_link_by_symbol(symbol, game_id):
    if symbol == 'X':
        return get_game_data('player_1_message_link', game_id)
    elif symbol == 'O':
        return get_game_data('player_2_message_link', game_id)
    pass

def get_table(game_id):
    return get_game_data('game_table', game_id)

# $$$NYI$$$ BOT CODES
# for_bot_corners = (0,2,6,8)
# for_bot_center = (4)
# for_bot_mids = (1,3,5,7)
