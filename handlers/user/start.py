from loader import dp

from aiogram import F
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline.language import language_inline_keyboards
from keyboards.default.menu import menu_buttons 
from loader import i18n

_ = i18n.gettext


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(_("Tilni tanlang"), reply_markup=language_inline_keyboards)


@dp.callback_query()
async def main_menu(callback: CallbackQuery, state: FSMContext):
    lang_code = callback.data.split("lang_")[-1]
    await state.update_data(locale = lang_code)
    lang = (_("O'zbek", locale = lang_code), _("Ingliz", locale = lang_code))[lang_code == 'en']
    await callback.answer(text=_("{lang} til tanlandi", locale = lang_code).format(lang = lang))


@dp.message()
async def select_menu(message: Message, state: FSMContext):
    buttons = await menu_buttons(state)

    await message.answer(_("Bo'limni tanlang"), reply_markup=buttons)

    
