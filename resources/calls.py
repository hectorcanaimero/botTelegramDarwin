from time import sleep
from random import random
from os import path, getcwd
from .handlers import first_menu_keyboard, main_menu_keyboard
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton


public = path.join(getcwd(), 'public')

# def calls(update, context):
#     public = path.join(getcwd(), 'public')
#     query = update.callback_query
#     query.answer()
#     data = query.data
#     context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
#     sleep(random() * 2 + 1.)
#     query.edit_message_text(text=f"Opcion enviada {data}")
#     if data == 'm1_1':
#         query.edit_message_text(text='Todos los requisitos para la Licencia de Licores')
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
#                                path.join(public, 'images', '01.png'), 'rb'))
#     elif data == 'm1_2':
#         query.edit_message_text(text='Todos los requisitos para la Licencia de Actividad Economica')
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
#                                path.join(public, 'images', '01.png'), 'rb'))


def callback(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(random() * 2 + 1.)
    query = update.callback_query
    query.answer()
    data = query.data
    if data == 'm1':
        query.edit_message_text(text='Escoja su opcion: ', reply_markup=first_menu_keyboard())
    if data == 'main':
        query.edit_message_text(text='Escoja su opcion: ', reply_markup=main_menu_keyboard())
    if data == 'm1_1':
        query.edit_message_text(text='Requisitos para la Licencia de Licores')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(path.join(public, 'images', '01.png'), 'rb'))
        query.edit_message_text(text='', reply_markup=return_main_menu_keyboard())
    if data == 'm1_2':
        query.edit_message_text(text='Requisitos para la Licencia de Actividad Economica')
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(path.join(public, 'images', '01.png'), 'rb'))
        query.edit_message_text(text='', reply_markup=return_main_menu_keyboard())


def return_main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Denuncias", callback_data='m2')]]
    return InlineKeyboardMarkup(keyboard)