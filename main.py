import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 1. Вставь сюда свой ТОКЕН (который дал BotFather)
API_TOKEN = '8826211617:AAFiaTHrmaCm_llFN409ixzkztcOdPTVLX4'

# 2. Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 3. Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я живой! Это мой первый бот для портфолио 😎")

# 4. Обработчик любого текста
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

# 5. Запуск бота
async def main():
    print("Бот запущен и ждет сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())