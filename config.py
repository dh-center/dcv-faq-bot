"""
TOKEN_ID - an authorization token for your bot
DEFAULT_REQUEST_KWARGS - proxy url for working in Russia
STICKER_PATH - path to image that sends when the bot gets something except
voice or photo message
DATABASE_NAME - name for creating database
"""
import os

TOKEN = os.getenv('TOKEN')
PORT = os.getenv('PORT')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
MODE = os.getenv('MODE')

CONFIG = dict(DEFAULT_REQUEST_KWARGS={'proxy_url':
                                      'socks5h://sox.ctf.su:1080'},
              STICKER_PATH='http://b.webpurr.com/anY5.webp')
