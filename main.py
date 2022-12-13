
from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5820790481:AAGo1-TRggGLhs6qzrvHlZ0l9X1uYgqkOdM',use_context = True )

def start(updater,context):
 updater.message.reply_text("Hi I'm Telegram Bot and English to Amharic Translator. Type any word, phrase or sentense, I will translate to Amharic")
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='am') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
