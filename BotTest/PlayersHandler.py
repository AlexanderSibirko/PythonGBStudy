
# list = [telegram_id, telegram_id...]
players = []
# players_data = {'telegram_id': {'Name': string, games_id': {1,2,5,...}}
players_data = {}

def get_players():
    return players

def add_player_data(key, data, player_id):
    players_data[player_id][key] = data

def get_player_data(key, player_id):
    return players_data[player_id][key]

def add_player(user_id, user_name):
    players.append(user_id)
    add_player_data('Name', user_name, user_id)

def remove_player(user_id):
    if user_id in players:
        if players_data[user_id]['status'] == 0:
            players.remove(user_id)
            return True # player was removed
        else:
            # ToDo: if status = 1, inform opponent have left thd_player
            players.remove(user_id)
            return True # player was removed
    return False # player wasn't removed