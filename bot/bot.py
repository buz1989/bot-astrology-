from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio

from data.horoscope_texts import HOROSCOPES

# 🔑 ВСТАВ СЮДИ СВІЙ ТОКЕН ВІД BOTFATHER
TOKEN = "8083146438:AAGvTrr9kY2r2Hf0IufJcfPgETesoG6u8ZA"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def cmd_start(message: Message):
    builder = ReplyKeyboardBuilder()
    for sign in HOROSCOPES.keys():
        builder.button(text=sign)
    builder.adjust(3)

    await message.answer(
        "🔮 Привіт! Обери свій знак зодіаку, щоб отримати гороскоп:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message()
async def send_horoscope(message: Message):
    sign = message.text
    horoscope = HOROSCOPES.get(sign)

    if horoscope:
        await message.answer(f"<b>{sign}</b>\n\n{horoscope}")
    else:
        await message.answer("⚠️ Будь ласка, обери знак зодіаку з клавіатури.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
