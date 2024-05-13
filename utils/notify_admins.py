import logging

from data.config import ADMINS


async def on_startup_notify(bot):
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=int(admin),
                text="Bot qayta ishga tushdi!"
            )
        except Exception as err:
            logging.exception(err)
