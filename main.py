from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Доходы').add('Расходы')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Доходы').add('Расходы').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить доход').add('Добавить расход').add('Админ-панель')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
	await message.answer_sticker('CAACAgIAAxkBAAICAmXg6D2UYDRshrLCDXiNZIYT83vgAAIVKgAC7AABwUpA5EMJg_c8oTQE')
	await message.answer(f'{message.from_user.first_name}, добро пожаловать, я ваш личный бухгалтер',
						 reply_markup=main)
	if message.from_user.id == int(os.getenv('ADMIN_ID')):
		await message.answer(f'Вы авторизовались как администратор', reply_markup=main_admin)


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
	await message.answer(f'{message.from_user.id}')


@dp.message_handler(text='Доходы')
async def contacts(message: types.Message):
	await message.answer(f'История доходов')


@dp.message_handler(text='Расходы')
async def contacts(message: types.Message):
	await message.answer(f'История расходов')


@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
	if message.from_user.id == int(os.getenv('ADMIN_ID')):
		await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
	else:
		await message.reply('Я тебя не понимаю')






# @dp.message_handler(content_types=['sticker'])
# async def check_sticker(message: types.Message):
# 	await message.answer(message.sticker.file_id) # узнать id стикера
# 	await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler()
async def answer(message: types.Message):
	await message.reply('Я тебя не понимаю')


if __name__ == '__main__':
	executor.start_polling(dp)