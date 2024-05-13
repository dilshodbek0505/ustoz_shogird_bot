from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# langs = (
#     ("Uz🇺🇿", "lang_uz"),
#     ("Eng🇬🇧", "lang_en"),
# )

# inline_keyboards = []
# for i in langs:
#     inline_keyboards.append(
#         InlineKeyboardButton(text = i[0], callback_data = i[1]) 
#     )

# langs_inline_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[inline_keyboards]
# )
    
language_inline_keyboards = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Uz🇺🇿", callback_data="lang_uz"), InlineKeyboardButton(text="Eng🇬🇧", callback_data="lang_en")]
    ]
)