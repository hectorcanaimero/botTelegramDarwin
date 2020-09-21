import json
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler, ConversationHandler
from config import TELEGRAM_TOKEN

from resources.calls import callback
from resources.handlers import welcome, error


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, None, use_context=True)
dp.add_handler(CommandHandler('start', welcome))
dp.add_handler(CallbackQueryHandler(callback))
dp.add_error_handler(error)


def lambda_handler(event, context):
    dp.process_update(Update.de_json(json.loads(event["body"]), bot))
    return {"statusCode": 200}
