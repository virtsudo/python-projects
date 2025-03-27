from app.config import *
from asyncio import run
from logging import basicConfig, INFO


async def main():
    basicConfig(level=INFO, format="%(asctime)s\n\t- %(levelname)s - %(name)s - %(message)s")
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    bot = Bot(token=BOT_TOKEN)

    dp.include_router(common.router)
    dp.include_router(game.router)

    await set_commands(bot)
    # await bot.delete_my_commands()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description="Start bot"),
        BotCommand(command='/play', description="Start the Game"),
        BotCommand(command='/cancel', description="Cancel all")
    ]
    await bot.set_my_commands(commands)


if __name__ == '__main__':
    run(main())
