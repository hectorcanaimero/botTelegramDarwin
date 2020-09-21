from sys import stderr
from time import sleep
from random import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatAction, ParseMode


STATE1 = 1


def welcome(update, context):
    try:
        text = (
            f"Hola *{update.effective_chat.first_name} {update.effective_chat.last_name}*,\n"
            f"Bienvenido a nuestro bot para la hacienda en Francisco Linares Alcantara:\n"
            f"*Digite en la opcion que anda buscando:*"
        )
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(random() * .7 + 1.)
        context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(str(e))


def feedback(update, context):
    try:
        message = 'Por favor, digite um feedback para o nosso tutorial:'
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))


def main_menu(update, context):
    text = f"*Digite en la opcion que anda buscando:*"
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * .7 + 1.)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=main_menu_keyboard())


def first_menu(update, context):
    query = update.callback_query
    query.answer()
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * 2 + 1.)
    query.edit_message_text(text="Escoja:", reply_markup=first_menu_keyboard())


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Não sei o que fazer com esse comando.")


def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Ver Requisitos", callback_data='m1'),
            InlineKeyboardButton("Enviar Voucher", callback_data='m2')
        ],
        [InlineKeyboardButton("Denuncias", callback_data='m3')]
    ]
    return InlineKeyboardMarkup(keyboard)


def first_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Licores", callback_data='m1_1'),
            InlineKeyboardButton("Actividades Economicas", callback_data='m1_2')
        ],
        [InlineKeyboardButton("Regresar al Menu", callback_data='main')]
    ]
    return InlineKeyboardMarkup(keyboard)


def error(update, context):
    """Log Errors caused by Updates."""
    stderr.write("ERROR: '%s' caused by '%s'" % context.error, update)
    pass