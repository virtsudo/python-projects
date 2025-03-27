from app.config import *
from .status import Status

q1 = "Столица С.Ш.А ?"
q2 = "В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства."
q3 = "Земля делает полный оборот вокруг своей оси за ..."

async def f_q(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Washington  D.C", "New York City")
    await message.answer(q1, reply_markup=keyboard)
    await Status.f_level.set()

async def s_q(message: types.Message, state: FSMContext):
    if message.text != "Washington  D.C":
        await message.answer("Fail!, to play again -> /play", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Правильно", "Неправильно")
    await message.answer(q2, reply_markup=keyboard)
    await Status.s_level.set()


async def t_q(message: types.Message, state: FSMContext):
    if message.text != "Правильно":
        await message.answer("Fail!, to play again -> /play", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("24 часа", "23 часа 56 минут и 4 секунды", "23 часа 59 минут и 50 секунды")
    await message.answer(q3, reply_markup=keyboard)
    await Status.t_level.set()

async def g_final(message: types.Message, state: FSMContext):
    if message.text != "23 часа 56 минут и 4 секунды":
        await message.answer("Fail!, to play again -> /play", reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    await message.answer("Congratulations, you are winner!", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

def reg_g(dp: Dispatcher):
    dp.register_message_handler(f_q, commands="play", state="*")
    dp.register_message_handler(s_q, state=Status.f_level)
    dp.register_message_handler(t_q, state=Status.s_level)
    dp.register_message_handler(g_final, state=Status.t_level)