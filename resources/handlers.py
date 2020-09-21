from time import sleep
from random import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction


def start(update, context):
    text = (
        f"Hola {update.effective_chat.first_name} {update.effective_chat.last_name},\n"
        f"Bienvenido a nuestro bot para la hacienda en Francisco Linares Alcantara. \n"
        f"Digite en la opcion que anda buscando"
    )
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * 2 + 1.)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=main_menu_keyboard())


def main_menu(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * 2 + 1.)
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=main_menu_keyboard())


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
        [InlineKeyboardButton("Ver Requisitos", callback_data='m1')],
        [InlineKeyboardButton("Denuncias", callback_data='m2')]
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