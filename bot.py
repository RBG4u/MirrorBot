import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text('Здравствуй!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater('6254464605:AAEWf8X2fWANC-SKAD2OPTKFyUyh-2Lbfn8', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

main()