import logging, asyncio, sys

from loader import dp, bot, db
import handlers
from utils.notify_admins import on_startup_notify

async def main() -> None:    
    # botning adminlariga xabar yuborish 
    await on_startup_notify(bot)

    # botnign boshlang'ich buyruqlarini o'rnatish
    
    # Ma'lumotlar bazasini yaratish
    try:
        ... # yangi table larni yaratish
    except Exception as err:
        logging.exception(err)

    # 
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())