import logging, asyncio, sys
import handlers, keyboards

from loader import dp, bot, i18n

from aiogram.utils.i18n import FSMI18nMiddleware

async def main() -> None:

    dp.update.outer_middleware.register(FSMI18nMiddleware(i18n=i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())