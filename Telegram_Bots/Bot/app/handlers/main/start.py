from app.config import *
from collections import Counter

file_name = '/home/crownlabs/Desktop/Bot/reg.txt'

def unique():
    l1 = list()
    with open(file_name, "r") as f:
        for i in f:
            l1.append(i)
    l1 = [*Counter(l1)]
    return l1

async def g_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Hello this is mini game, would you play?(/play)", reply_markup=types.ReplyKeyboardRemove())
    u = types.User.get_current()
    print(u)
    with open(file_name, 'a') as f:
        f.write(f"ID: {str(u.id)}\t")
        f.write(f"USERNAME: @{str(u.username)}\t")
        if str(u.full_name) != "ㅤ":
            try:
                f.write(f"FULLNAME: {str(u.full_name)}\n")
            except :
                f.write("FULLNAME: ")
                try:
                    for i in str(u.full_name):
                        f.write(i)
                except:
                    pass
        else:
            f.write(f"FULLNAME: <empty>\n")
    l1 = unique()
    with open(file_name, "w") as f:
        for i in l1:
            f.write(i)



async def g_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Finished!", reply_markup=types.ReplyKeyboardRemove())

def reg_m(dp: Dispatcher):
    dp.register_message_handler(g_start, commands="start", state="*")
    dp.register_message_handler(g_cancel, commands="cancel", state="*")

