from dotenv import load_dotenv
import os

# python-dotenv kutubxonasidan foydalanish
load_dotenv()


# .env file ichidagi ma'lumotlarni o'qib olish
TOKEN = str(os.getenv("TOKEN")) # bot tokeni
ADMINS = list(os.getenv("ADMINS").split(',')) # adminlar ro'yhati
