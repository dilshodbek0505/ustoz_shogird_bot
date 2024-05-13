from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data import config
from aiogram.utils.i18n import I18n



bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
i18n = I18n(path="locales")