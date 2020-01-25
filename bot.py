from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

#bot = telegram.Bot(token='1044556705:AAFMzUzmbYW7GJiYKlVL8icLEU-mSa64V0Q')
#print (bot.get_me())

updater = Updater(token='1044556705:AAFMzUzmbYW7GJiYKlVL8icLEU-mSa64V0Q', use_context=True)
dispatcher = updater.dispatcher
msg = "These are the 2 commands available: \n /setdate ddmm: to set the date \n /horoscope: to get your horoscope"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to horoscope bot! \n\n"+msg)

def error(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the right command \n\n" +msg)

def setdate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)




start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

error_handler = MessageHandler(Filters.text, error)
dispatcher.add_handler(error_handler)

setdate_handler = CommandHandler('setdate', setdate)
dispatcher.add_handler(setdate_handler)
updater.start_polling()
