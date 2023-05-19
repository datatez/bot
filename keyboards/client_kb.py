from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


b1 = KeyboardButton("Связаться с менеджером👻")
b2 = KeyboardButton("Популярные вопросы🤓")
b3 = KeyboardButton("Больше о нас🧑‍💻")
b4 = KeyboardButton(
    "Оставить заявку для сотрудничества🙈")

kb_client_main = ReplyKeyboardMarkup(
    resize_keyboard=True, input_field_placeholder="Навигация")
kb_client_main.row(b1, b2, b3).add(b4)


b1 = KeyboardButton("Да")
b2 = KeyboardButton("Скорее да")
b3 = KeyboardButton("Скорее нет")
b4 = KeyboardButton("Нет")
kb_client_hospitals_answer = ReplyKeyboardMarkup(
    resize_keyboard=True, input_field_placeholder="Ваш ответ:")
kb_client_hospitals_answer.row(b1, b2, b3, b4)


b1 = KeyboardButton('Завершить')
b2 = KeyboardButton('Вернуться к списку')
kb_client_complete_or_replay = ReplyKeyboardMarkup(
    resize_keyboard=True, input_field_placeholder="Что делаем?")
kb_client_complete_or_replay.row(b1, b2)

kb_web = InlineKeyboardMarkup()
bb1 = InlineKeyboardButton(
    text="Перейди на сайт",  url='http://careconnect.ru/')
kb_web.insert(bb1)
