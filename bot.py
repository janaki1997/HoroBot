from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

#bot = telegram.Bot(token='1044556705:AAFMzUzmbYW7GJiYKlVL8icLEU-mSa64V0Q')
#print (bot.get_me())

updater = Updater(token='1044556705:AAFMzUzmbYW7GJiYKlVL8icLEU-mSa64V0Q', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="HI I am Harini! Call me maybe")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
