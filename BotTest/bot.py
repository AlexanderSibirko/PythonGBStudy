from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import CrossAndCircleModel
from PlayersHandler import *
# context.bot.send_message(update.effective_user.id,'Registered')


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'type /help to get possible commands')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext) -> None:
    help_message = '''Commands:
/help - list possible commands 
/hello - sends hello to you
/register - to register to Cross and Zeros game\n
'''
    if update.effective_user.id in players:
        help_message += '''/exit - unregister from Cross and Zeros game
/list - show players registered to Cross and Zeros game
/play - inform bot that you are ready to play
'''
    update.message.reply_text(help_message)




def registergame(update: Update, context: CallbackContext) -> None:
    add_player(update.effective_user.id, update.effective_user.name)
    update.message.reply_text(f'Registered \n Looking for opponents')
    # ToDo: check if there is anougth players to pair them if yes => ask_to_start_game(update, context)

def playgame(update: Update, context: CallbackContext) -> None:
    # ToDo: staring game for players
    # search for 2 players ready to play and start game for them 
    player1 = 1922797485 # PH code
    player2 = 1922797485 # PH code

    game_idx = CrossAndCircleModel.create_new_game(player1,player2)
    players_data[player1]['status'] = 1
    players_data[player2]['status'] = 1
    players_data[player1]['game_idx'] = game_idx
    players_data[player2]['game_idx'] = game_idx
    # создание кнопок игрового "поля"
    keyboard = [[InlineKeyboardButton(" ", callback_data='0'),InlineKeyboardButton(" ", callback_data='1'),InlineKeyboardButton(" ", callback_data='2')],
    [InlineKeyboardButton(" ", callback_data='3'),InlineKeyboardButton(" ", callback_data='4'),InlineKeyboardButton(" ", callback_data='5')],
    [InlineKeyboardButton(" ", callback_data='6'),InlineKeyboardButton(" ", callback_data='7'),InlineKeyboardButton(" ", callback_data='8')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    botanswer = update.message.reply_text('Please choose:', reply_markup=reply_markup)
    botanswer.chat_id 
    botanswer.message_id
    

    ### понять код
def button(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    """Parses the CallbackQuery and updates the message text."""
    this_chat_id = query.message.chat_id
    this_message = query.message.message_id
    
    query = update.callback_query
    context.bot.edit_message_text(chat_id = this_chat_id, message_id = this_message, text = 'gotcha')
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    # Получаем состояние игрового поля (через id юзера)
    game_idx = players_data[user_id]['game_idx']
    if CrossAndCircleModel.add_symbol(game_idx,user_id,int(query.data)):
        message_text = "Another_player_name turn" # ToDo get another player name from games_data
    else:
        message_text = "There is already X or O choice another square:"
    # создание кнопок игрового поля
    reply_markup = InlineKeyboardMarkup(create_response_table(game_idx))
    # query.edit_message_text(text=message_text, reply_markup=reply_markup)
    
def create_response_table(game_idx):
    table = CrossAndCircleModel.get_table(game_idx)
    keyboard = [[InlineKeyboardButton(str(table[0]), callback_data='0'),InlineKeyboardButton(str(table[1]), callback_data='1'),InlineKeyboardButton(str(table[2]), callback_data='2')],
    [InlineKeyboardButton(str(table[3]), callback_data='3'),InlineKeyboardButton(str(table[4]), callback_data='4'),InlineKeyboardButton(str(table[5]), callback_data='5')],
    [InlineKeyboardButton(str(table[6]), callback_data='6'),InlineKeyboardButton(str(table[7]), callback_data='7'),InlineKeyboardButton(str(table[8]), callback_data='8')]]
    return keyboard

def list_players(update: Update, context: CallbackContext) -> None:
    message = 'Registered players:\n'
    for player in players:
         message += players_data[player]['Name'] + '\n' 
    update.message.reply_text(message)

def exitgame(update: Update, context: CallbackContext) -> None:
    if remove_player(update.effective_user.id):
        update.message.reply_text(f'You have left registered to play mode')


updater = Updater('5263196202:AAFPaQDpDkQhC1jV6FdknUb0uSCaeULs51I')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('register', registergame))
updater.dispatcher.add_handler(CommandHandler('play', playgame))
updater.dispatcher.add_handler(CommandHandler('list', list_players))
updater.dispatcher.add_handler(CommandHandler('exit', exitgame))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
