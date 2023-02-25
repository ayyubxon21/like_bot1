from flask import Flask,request
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext,CallbackQueryHandler,Dispatcher,callbackqueryhandler
from telegram import Update,Bot
from handler import start,get_image,callback_like

TOKEN = os.environ['TOKEN']

bot = Bot(TOKEN)
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    print(request.form)
    data = request.get_json(force=True)
    
    #dispatcher
    dp : Dispatcher = Dispatcher(bot, None, workers=0)
    
    #update
    update: Update = Update.de_json(data, bot)
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.photo, get_image))
    dp.add_handler(CallbackQueryHandler(callback_like))
    
    dp.process_update(update)
    return {"status":200}

# if __name__ == '__main__':
#   app.run(debug=True)
#bot.set_webhook("https://ayyubxon1234.pythonanywhere.com/")