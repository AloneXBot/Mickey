from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27353035"))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6079943111"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "AlonesHeaven")
UPDATE_CHNL = getenv("UPDATE_CHNL", "AloneXBots")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ALONE_WAS_BOT")

# Random Start Images
IMG = [
    "https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ",
    "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ",
    "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
