from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Доходы').add('Расходы')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.answer_sticker('CAACAgIAAxkBAAICAmXg6D2UYDRshrLCDXiNZIYT83vgAAIVKgAC7AABwUpA5EMJg_c8oTQE')
	await message.answer(f'{message.from_user.first_name}, добро пожаловать, я ваш личный бухгалтер',
						 reply_markup=main)


@dp.message_handler(text='Доходы')
async def contacts(message: types.Message):
	await message.answer(f'История доходов')


@dp.message_handler(text='Расходы')
async def contacts(message: types.Message):
	await message.answer(f'История расходов')


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
	await message.answer(message.sticker.file_id) # узнать id стикера
	await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(content_types=['document', 'photo'])
async def check_sticker(message: types.Message):
	await bot.forward_message()


@dp.message_handler()
async def answer(message: types.Message):
	await message.reply('Я тебя не понимаю')


if __name__ == '__main__':
	executor.start_polling(dp)