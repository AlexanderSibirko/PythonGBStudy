
# list = [telegram_id, telegram_id...]
players = []
# players_data = {'telegram_id': {'Name': string, 'status': integer, 'game_idx': integer}
players_data = ({})

def add_player(user_id, user_name):
    players.append(user_id)
    players_data[user_id] = {'Name': user_name, 'status': 0}

def remove_player(user_id):
    if user_id in players:
        if players_data[user_id]['status'] == 0:
            players.remove(user_id)
            return True # player was removed
        else:
            # ToDo: if status = 1, inform opponent have left the game
            players.remove(user_id)
            return True # player was removed
    return False # player wasn't removed