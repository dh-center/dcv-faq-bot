from config import CONFIG
from config import TOKEN, MODE, HEROKU_APP_NAME, PORT
from dialog_manager import LANGUAGES, MAIN_MENU, ANSWERS, SECOND_LEVEL

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(format=('%(asctime)s - %(name)s - '
                            '%(levelname)s - %(message)s'),
                    level=logging.INFO)
logger = logging.getLogger()

language = {}


def add_handlers(updater):
    """
    This function adds handlers for start and message_processing functions.
    :param updater: an Updater object
    :return: None
    """
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.all,
                                                  message_processing))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))


def start(update, context):
    """
    Function sends reply every time the Bot receives message with
    /start command.
    :return: None
    """

    keyboard = []
    for item in LANGUAGES:
        keyboard.append([InlineKeyboardButton(item, callback_data=item)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    start_text = (ANSWERS['greeting'] + '\n\n' +
                  ANSWERS['ru_greeting'])
    context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                             chat_id=update.effective_chat.id,
                             text=start_text, reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    logger.info(f'Query {query.data} for '
                f'{update.effective_user.name} at '
                f'{update.effective_message.date}')

    keyboard = []

    if query.data in LANGUAGES:
        language[update.effective_user.name] = query.data
        for item in LANGUAGES[query.data]:
            keyboard.append([InlineKeyboardButton(item,
                                                  callback_data=item)])

    elif query.data in MAIN_MENU:
        for item in MAIN_MENU[query.data]:
            keyboard.append([InlineKeyboardButton(item,
                                                  callback_data=item)])

    elif query.data in SECOND_LEVEL:
        for item in SECOND_LEVEL[query.data]:
            keyboard.append([InlineKeyboardButton(item,
                                                  callback_data=item[:5])])

    elif query.data in ANSWERS:
        if language[update.effective_user.name] == 'English':
            back_text = 'Back to main menu'
        else:
            back_text = 'Назад в главное меню'

        keyboard = [[InlineKeyboardButton(back_text, callback_data=
        language[update.effective_user.name])]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                                 chat_id=update.effective_chat.id,
                                 text=ANSWERS[query.data],
                                 reply_markup=reply_markup,
                                 disable_web_page_preview=True)
        return 1

    else:
        if language[update.effective_user.name] == 'Русский':
            error_text = ANSWERS['ru_default']
        else:
            error_text = ANSWERS['default']

        context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                                 chat_id=update.effective_chat.id,
                                 text=error_text)
        return 1

    reply_markup = InlineKeyboardMarkup(keyboard)

    if language[update.effective_user.name] == 'Русский':
        intro_text = 'Выберите вопрос:'
    else:
        intro_text = 'Choose the question:'

    context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                             chat_id=update.effective_chat.id,
                             reply_markup=reply_markup,
                             text=intro_text)


def help(update, context):
    if language[update.effective_user.name] == 'Русский':
        help_text = 'Напиши /start для входа в меню.'
    else:
        help_text = 'Use /start command for FAQ.'
    context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                             chat_id=update.effective_chat.id,
                             text=help_text)


def message_processing(update, context):
    """
    Function saves voice messages in wav format with simple rate 16MHz and
    photos if a face is detected there. All path store in database `bot`.
    :return: None
    """

    logger.info(f'Waiting for message_processing function for '
                f'{update.effective_user.name} at '
                f'{update.effective_message.date}')

    if language == 'Русский':
        answer_text = ANSWERS['ru_default']
    else:
        answer_text = ANSWERS['default']

    context.bot.send_message(parse_mode=ParseMode.MARKDOWN,
                             chat_id=update.effective_chat.id,
                             text=answer_text)

    logger.info(f'Answer ready for {update.effective_user.name} '
                f'at {update.effective_message.date}')


if MODE == 'prod_heroku':
    def run():
        updater = Updater(TOKEN, use_context=True)
        updater.start_webhook(listen='0.0.0.0',
                              port=PORT,
                              url_path=TOKEN)
        add_handlers(updater)
        updater.bot.set_webhook(
            f'https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}')

elif MODE == 'prod':
    def run():
        REQUEST_KWARGS = CONFIG['DEFAULT_REQUEST_KWARGS']
        updater = Updater(TOKEN,
                          request_kwargs=REQUEST_KWARGS,
                          use_context=True)
        add_handlers(updater)
        updater.start_polling()

elif MODE == 'dev':
    def run():
        # experiments here
        REQUEST_KWARGS = CONFIG['DEFAULT_REQUEST_KWARGS']
        updater = Updater(TOKEN,
                          request_kwargs=REQUEST_KWARGS,
                          use_context=True)
        add_handlers(updater)
        updater.start_polling()
else:
    logger.error('No MODE specified')
    exit(1)

if __name__ == '__main__':
    logger.info('Bot starting')
    run()
