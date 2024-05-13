from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from loader import i18n

_ = i18n.gettext


async def menu_buttons(state: FSMContext):

    meun_list = (_("Ish joyi kerak"), _("Xodim kerak"), _("Sherik kerak"), _("Xizmat ko'rsatish"))

    buttons = []
    for i in meun_list:
        buttons.append([KeyboardButton(text=i)])

    menu_buttons = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return menu_buttons

# for i in menu_list:
#     menu_buttons.keyboard.append(
#         [KeyboardButton(text=i)]
#     )
