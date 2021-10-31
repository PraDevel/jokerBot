import datetime
import math
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
STATE = None
BIRTH_YEAR = 1
BIRTH_MONTH = 2
BIRTH_DAY = 3

# function to handle the /start command
def start(update, context):
    update.message.reply_text(f"Hi , nice to meet you!")


def joke(update, context):
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    ppp=(r.json())
    update.message.reply_text(str(ppp['setup']+"  "+ str(ppp['punchline'])))

def main():
    TOKEN = ""
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("joke", joke))



    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
