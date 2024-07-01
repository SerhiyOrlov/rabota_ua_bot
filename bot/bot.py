import logging
import os
import asyncio
import sys
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram import Router


API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

@router.message(Command(commands=['get_today_statistic']))
async def send_today_statistic(message: types.Message):
    try:
        # Download file from localhost:5001/get_today_statistic
        url = 'http://flask-app:5000/get_today_statistic'
        local_filename = 'today_statistic.xlsx'  # Filename for saving

        response = requests.get(url)
        response.raise_for_status()  # Raise exception if request failed

        # Save the file
        with open(local_filename, 'wb') as f:
            f.write(response.content)

        # Send the file to the user
        await message.reply_document(types.FSInputFile(local_filename))

    except requests.RequestException as e:
        logging.error(f"Failed to download file: {e}")
        await message.reply("Не удалось скачать файл с сервера.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        await message.reply("Произошла непредвиденная ошибка.")

# Include the router in the dispatcher
dp.include_router(router)


async def main() -> None:
    # Start the bot
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
