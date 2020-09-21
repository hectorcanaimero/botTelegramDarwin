from time import sleep
from random import random
from os import path, getcwd
from .handlers import first_menu_keyboard, main_menu_keyboard
from telegram import ChatAction, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


public = path.join(getcwd(), 'public')


def callback(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * 1 + 1.)
    query = update.callback_query
    query.answer()
    data = query.data
    data.lower()
    query.edit_message_text(f'Opcion escojida: {data}')
    if data == 'm1':
        query.edit_message_text(text='*Escoja su opcion: *',
                                parse_mode=ParseMode.MARKDOWN,
                                reply_markup=first_menu_keyboard())
    if data == 'm1_1':
        query.edit_message_text(text='Requisitos para la Licencia de Licores')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(path.join(public, 'images', '01.png'), 'rb'),
                               reply_markup=first_menu_keyboard())
    if data == 'm1_2':
        query.edit_message_text(text='Requisitos para la Licencia de Actividad Economica')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(path.join(public, 'images', '01.png'), 'rb'),
                               reply_markup=first_menu_keyboard())
    if data == 'm2':
        query.edit_message_text(text='Digite su codigo de Patente:')
    if data == 'm3':
        pass
    if data == 'main':
        text = f"*Digite en la opcion que anda buscando:*"
        query.edit_message_text(text=text, parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu_keyboard())


def return_main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Regresar al Menu", callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)