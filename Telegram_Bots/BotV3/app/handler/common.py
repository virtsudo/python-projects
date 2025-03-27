from app.config import *

router = Router()


@router.message(Command(commands=["start"]))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Hello this is mini game, would you play?(/play)", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=["cancel"]))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Finished!", reply_markup=ReplyKeyboardRemove())
