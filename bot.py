import logging,os,requests
from read_config import read_config
from telegram import Update,User
from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler,Filters
from learn import CyberTeens

#读取配置
config = read_config()
token = config['token']
proxy = config['proxy']
chatid = config['chatid']
openid = config['openid']

#配置代理
PROXY = {
    'proxy_url': proxy
}

updater = Updater(token=token, request_kwargs=PROXY)
dispatcher = updater.dispatcher
#日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def _learn():
    '''提交学习记录'''
    try:
        s = requests.session()
        teen = CyberTeens(openid)
        code = teen.get_code(s)
        user_info = teen.get_user(s)
        course = teen.get_course(s, code)
        teen.save_door(user_info, course, s)
    except:
        return False

def _check_chatid(cur_chatid):
    '''检测主人id'''
    master_chatid = chatid
    if cur_chatid == master_chatid:
        return True
    else:
        return False

def learn(update: Update, context: CallbackContext):
    '''响应/learn命令'''
    if _check_chatid(update.effective_chat.id):
        _learn()
        context.bot.send_message(chat_id=update.effective_chat.id, text="好！")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,text='坏！')


learn_handler = CommandHandler('learn', learn)
dispatcher.add_handler(learn_handler)

updater.start_polling()
updater.idle()