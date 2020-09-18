from os import path, getcwd


def sendDocument(update, context):
    path_pdf = path.join(getcwd(), 'public', 'pdf', 'one.pdf')
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=path_pdf)


def sendMessage(update, context):
    context.bot.sendDocument(chat_id=update.effective_chat.id, text='Prueba del Sistema')
