from aiogram import Bot, Dispatcher, types, executor

TOKEN = '6198687861:AAHXYEh4DacXEdslG_NFfVjan_fQHTs8HuE'

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом 
"""

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):

    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])   
async def help_command(message: types.Message):
    await message.answer(text="Добро пожаловать!")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
