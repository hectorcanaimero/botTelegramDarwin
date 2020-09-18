from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    text = (
        f"Hola {update.effective_chat.first_name} {update.effective_chat.last_name},\n"
        f"bienvenido a nuestro bot para la hacienda en Linares Alcantara \n"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=menuKeyboard())


def menu(update):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Escoha la opcion a usar:", reply_markup=menuKeyboard())


def menuSolicitud(update):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Vea su solicitud:", reply_markup=menuSolicitudKeyboard())


def menuKeyboard():
    keyboard = [[InlineKeyboardButton('Ver Solicitudes', callback_data='m1')],
                [InlineKeyboardButton('Agendar Cita', callback_data='m2')],
                [InlineKeyboardButton('Denunciar al Funcionario', callback_data='m3')]]
    return InlineKeyboardMarkup(keyboard)


def menuSolicitudKeyboard():
    keyboard = [[InlineKeyboardButton('Patente de Comercio', callback_data='m1_1')],
                [InlineKeyboardButton('Patente de Industria', callback_data='m1_2')],
                [InlineKeyboardButton('Patente de Licores', callback_data='m1_3')],
                [InlineKeyboardButton('Regresar al Menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Não sei o que fazer com esse comando.")
