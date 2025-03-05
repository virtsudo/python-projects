from aiogram import Bot, Dispatcher, types, executor
import logging
logging.basicConfig(level=logging.INFO)

U1 = "User1"
U2 = "User2"

TOKEN = "telegrambot token"
user_id = "admin"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Welcome!")
    print(f"ID: {message.chat.id}")


@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    if message.text:
        await message.bot.send_message(chat_id=user_id, text=message.text)


@dp.message_handler(content_types=['animation'])
async def animation_handler(message: types.Message):
    if message.animation:
        await message.bot.send_animation(chat_id=user_id, animation=message.animation['file_id'])


@dp.message_handler(content_types=['voice'])
async def voice_handler(message: types.Message):
    if message.voice:
        await message.bot.send_voice(chat_id=user_id, voice=message.voice['file_id'])


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(message: types.Message):
    if message.document:
        await message.document.download(destination_dir="C:/users/bekhz/Desktop/") # inside the dir ./documents dir
        await message.bot.send_document(user_id, document=message.document.file_id)


@dp.message_handler(content_types=['photo'])
async def photo_handler(message: types.Message):
    if message.photo:
        await message.photo[-1].download(destination_dir='C:/users/bekhz/Desktop/test.jpg')
        await message.bot.send_photo(user_id, message.photo)


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def music_handler(message: types.Message):
    if message.audio:
        await message.audio.download(destination_file='C:/users/bekhz/Desktop/test.mp3')
        await message.bot.send_audio(user_id, audio=message.audio.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
