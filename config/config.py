import logging
import os
import sys
import time
import spamwatch
import aiohttp

import telegram.ext as tg
from redis import StrictRedis
from Python_ARQ import ARQ
from os import getenv
from pyrogram import Client, errors
from telethon.sessions import StringSession
from telethon import TelegramClient
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

class Config:
    INFOPIC = getenv('INFOPIC', "true").lower() == "true"
    EVENT_LOGS = getenv('EVENT_LOGS', "-1001800732275")
    WEBHOOK = getenv('WEBHOOK', "False").lower() == "true"
    ARQ_API_URL = getenv("ARQ_API_URL", "https://thearq.tech/")
    ARQ_API_KEY = getenv("ARQ_API_KEY", "")
    URL = getenv('URL', "")  # Does not contain token
    PORT = int(getenv('PORT', 5000))
    CERT_PATH = getenv("CERT_PATH")
    API_ID = getenv('API_ID', "4665778")
    API_HASH = getenv('API_HASH', "10e3ed833b0d09699973420d45359409")
    DB_URI = getenv('DATABASE_URL', "postgres://fqiiaofs:v-Fbgtr09XIsiwR6D5q3qz4mcwxy9Img@silly.db.elephantsql.com/fqiiaofs")
    DONATION_LINK = getenv('DONATION_LINK', "https://t.me/xelcius")
    LOAD = getenv("LOAD", "").split()
    NO_LOAD = getenv("NO_LOAD", "rss").split()
    DEL_CMDS = getenv('DEL_CMDS', "true").lower() == "true"
    STRICT_GBAN = getenv('STRICT_GBAN', "true").lower() == "true"
    WORKERS = int(getenv('WORKERS', "8"))
    BAN_STICKER = getenv('BAN_STICKER', 'CAADAgADOwADPPEcAXkko5EB3YGYAg')
    ALLOW_EXCL = getenv('ALLOW_EXCL', "true").lower() == "true"
    CASH_API_KEY = getenv('CASH_API_KEY', "-xyz")
    TIME_API_KEY = getenv('TIME_API_KEY', "-xyz")
    AI_API_KEY = getenv('AI_API_KEY', "")
    WALL_API = getenv('WALL_API', "")
    SUPPORT_CHAT = getenv('SUPPORT_CHAT', "https://t.me/Mitsuri_BotSupport")
    SPAMWATCH_SUPPORT_CHAT = getenv('SPAMWATCH_SUPPORT_CHAT', "")
    SPAMWATCH_API = getenv('SPAMWATCH_API', "")
    REPOSITORY = getenv("REPOSITORY", "https://github.com")
    IBM_WATSON_CRED_URL = getenv("IBM_WATSON_CRED_URL", "")
    IBM_WATSON_CRED_PASSWORD = getenv("IBM_WATSON_CRED_PASSWORD", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
    TELEGRAPH_SHORT_NAME = getenv("TELEGRAPH_SHORT_NAME", "xelcius")
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
    BOT_NAME = getenv("BOT_NAME", "Mitsuri")  # Name Of your Bot.4
    BOT_USERNAME = getenv("BOT_USERNAME", "MitsuriGroupBot")  # Bot Username
    OPENWEATHERMAP_ID = getenv("OPENWEATHERMAP_ID", "")  # From:- https://openweathermap.org/api
    LOG_GROUP_ID = getenv('LOG_GROUP_ID', "-1001800732275")
    BOT_ID = getenv("BOT_ID", "6251112181")
    ERROR_LOGS = getenv("ERROR_LOGS", "-1001800732275")  # Error Logs (Channel Ya Group Choice Is Yours) (-100)
    STRICT_GMUTE = getenv('STRICT_GMUTE', "True").lower() == "true"
    MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ok:lol@cluster1.udhzs7r.mongodb.net/?retryWrites=true&w=majority")
    DEBUG = getenv('IS_DEBUG', "False").lower() == "true"
    REDIS_URL = getenv("REDIS_URL", "")  # REDIS URL (From:- Heraku & Redis)
    OWNER_NAME = getenv("OWNER_NAME", "U N K N O W N")
    TOKEN = getenv('TOKEN', '6251112181:AAH8XwNf4ffv_KpcjGnbMc45lryd_EreKGg')
    OWNER_ID = getenv('OWNER_ID', '5500572462')
    JOIN_LOGGER = getenv('OWNER_ID', '-1001800732275')
    OWNER_USERNAME = getenv('OWNER_USERNAME', 'CrimsonDrops')
    DRAGONS = getenv('DRAGONS', '')
    DEV_USERS = getenv('DEV_USERS', '')
    WOLVES = getenv('WOLVES', '')
    TIGERS = getenv('TIGERS', '')


