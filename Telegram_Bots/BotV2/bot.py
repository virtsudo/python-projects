import asyncio

from app.config import *
from app.handlers.game import reg_g
from app.handlers.main.start import reg_m

logger = logging.getLogger(__name__)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description="Start bot"),
        BotCommand(command='/play', description="Start the Game"),
        BotCommand(command='/cancel', description="Cancel all")
    ]
    await bot.set_my_commands(commands)

async def main():
    logging.basicConfig(
        level=logging.INFO,
    )
    logger.error("Starting bot")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    reg_m(dp)
    reg_g(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
