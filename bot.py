import logging,os
from read_config import read_config
from telegram import Update
from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler,Filters

#读取配置
config = read_config()
bottoken = config['bottoken']

#配置代理
os.environ['http_proxy'] = config['proxy']
os.environ['https_proxy'] = config['proxy']

updater = Updater(token=bottoken, use_context=True)
dispatcher = updater.dispatcher
#日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def cmd_learn(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="乐")


handlers = CommandHandler('learn', cmd_learn)
dispatcher.add_handler(handlers)

updater.start_polling()