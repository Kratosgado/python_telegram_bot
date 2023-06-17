import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Sends a welcome message to the user.

    Args:
        update (telegram.Update): The update object from Telegram.
        context (telegram.ext.Context): The context object from Telegram.

    Returns:
        None
    """
    message = "Hi, I'm a KratosGado bot, please talk to me!"
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=message)

async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Asynchronous function that sends a message to a chat. 
    
    :param update: An instance of the Update class containing information about the new message.
    :type update: Update
    
    :param context: An instance of the ContextTypes.DEFAULT_TYPE class containing a Bot object, which is used to send the message.
    :type context: ContextTypes.DEFAULT_TYPE
    
    :return: None
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

if __name__ == '__main__':
    application = ApplicationBuilder().token("6086120952:AAGoSxTW6iFidtqa_-SaP6I8TTZ-aFXN-6A").build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)

    application.add_handler(echo_handler)
    application.add_handler(start_handler)
    application.add_handler(caps_handler)

    application.run_polling()