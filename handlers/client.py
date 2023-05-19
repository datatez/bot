from aiogram import Dispatcher,  types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from database import UserController

from keyboards import kb_client_main, kb_web
from create_bot import bot


async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, f'Добро пожаловать <b>{message.from_user.first_name}</b>!\nЯ - <b>Care Call</b>, бот созданный чтобы лучшать взаимодействие между клиентом и компанией.', parse_mode="html")
    await bot.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgIAAxkBAAEHhNNj1_Z_f-Nj481yLi4XFVR4uSq4zwACNhYAAlxA2EvbRm7S3ZV6DS0E", reply_markup=kb_client_main)

    await message.delete()


async def main_command(message: types.Message):
    await message.answer('Рады вас слышать, куда направимся?😊', reply_markup=kb_client_main)

    await message.delete()


async def help_command(message: types.Message):
    await message.answer(text='<b>Список команд:\n</b>/start - начало работы\n/main - вернуться на главную страницу\n/help - список команд', parse_mode='html')

    await message.delete()


async def question_text(message: types.Message):
    await message.answer('<b>Сколько стоит?💰</b>\nПредварительная цена составляет 9999 рублей и включает в себя многие преймущества комуникации с клиентом.\n\n<b>Нужно ли мне постоянно сидеть в телеграмме?📲</b>\nБезусловно нет! Мы разработали бота, который сам опрашивает аудиторию и отображает статистику в вашем личном кабинете!\n\n<b>Почему мне стоит выбрать именно вас?🏥</b>\nЭто хороший вопрос! У Вас есть небольшое преимущество, поскольку Вы точно знаете, о своих клиентах гораздо больше, чем другие.', parse_mode='html')


async def contact_text(message: types.Message):
    res = await UserController.create_applications(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.full_name, message.from_user.last_name)
    if res:
        await message.answer("<b>Отлично, заявка отпралена!</b>\nВ скором времени с вами свяжется наш специалист,\nожидайте!🤝", parse_mode='html')
    else:
        await message.answer("<b>Произошла ошибка!</b>\nПопробуйте ещё раз!\nИли свяжитесь со специалистом: @pavloging🤝", parse_mode='html')
        


async def about_text(message: types.Message):
    await message.answer('Мы <b>Care Call</b> - платформа мониторинга пациентов, персонализации лечения  и управления качеством медицинских услуг.\n\n-Персонализируйте подход к каждому пациенту.\n-Контролируйте качество оказание услуг.\n-Работайте над повышением удовлетворенности.\n-Стимулируйте продажи.\n\nОбщая медицина, стоматология, реабилитация, пластическая и эстетическая хирургия, косметология.',  parse_mode='html', reply_markup=kb_web)


async def manager_text(message: types.Message):
    await message.answer('Мы рады, что вас заинтересовали🤪\nПо любым вопросам, можете писать @mikhnusha', reply_markup=kb_web)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(main_command, commands=["main"])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(question_text, text=["Популярные вопросы🤓"])
    dp.register_message_handler(
        contact_text, text=["Оставить заявку для сотрудничества🙈"])
    dp.register_message_handler(about_text, text=["Больше о нас🧑‍💻"])
    dp.register_message_handler(manager_text, text=["Связаться с менеджером👻"])