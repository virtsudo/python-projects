from app.config import *
from app.state.status import Status
from app.keyboard.keyboard import keyboard_gen


q1 = "Столица С.Ш.А ?"
a1 = ["Washington  D.C", "New York City"]
q2 = "В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства."
a2 = ["Правильно", "Неправильно"]
q3 = "Земля делает полный оборот вокруг своей оси за ..."
a3 = ["24 часа", "23 часа 56 минут и 4 секунды", "23 часа 59 минут и 50 секунды"]

router = Router()


@router.message(StateFilter(None), Command(commands=["play"]))
async def f_q(message: Message, state: FSMContext):
    await message.answer(q1, reply_markup=keyboard_gen(a1))
    await state.set_state(Status.f_level)


@router.message(Status.f_level, F.text.in_(a1))
async def s_q(message: Message, state: FSMContext):
    if message.text != "Washington  D.C":
        await message.answer("Fail!, to play again -> /play", reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    await message.answer(q2, reply_markup=keyboard_gen(a2))
    await state.set_state(Status.s_level)


@router.message(Status.s_level, F.text.in_(a2))
async def t_q(message: Message, state: FSMContext):
    if message.text != "Правильно":
        await message.answer("Fail!, to play again -> /play", reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    await message.answer(q3, reply_markup=keyboard_gen(a3))
    await state.set_state(Status.t_level)


@router.message(Status.t_level, F.text.in_(a3))
async def g_final(message: Message, state: FSMContext):
    if message.text != "23 часа 56 минут и 4 секунды":
        await message.answer("Fail!, to play again -> /play", reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    await message.answer("Congratulations, you are winner!", reply_markup=ReplyKeyboardRemove())
    await state.clear()
