from aiogram import Dispatcher, types


async def zero_text(message: types.Message):
    await message.answer('Я тебя не понимаю😩')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(zero_text)
