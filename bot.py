import json
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler

from config import TELEGRAM_TOKEN

from models.handlers import start, menu, menuSolicitud
from models.requisitos import sendMessage, sendDocument


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, None, use_context=True)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(menu, pattern='main'))
dp.add_handler(CallbackQueryHandler(menuSolicitud, pattern='m1'))
dp.add_handler(CommandHandler('poll', sendDocument))
dp.add_handler(CommandHandler('prueba', sendMessage))


def lambda_handler(event, context):
    dp.process_update(Update.de_json(json.loads(event["body"]), bot))
    return {"statusCode": 200}
