from aiogram import Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils import get_weather_data

storage = MemoryStorage()
dp=Dispatcher(storage=storage)

class Form(StatesGroup):
    answer = State()

@dp.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer('Добрый день! Погоду в каком городе вы бы хотели узнать?')
    await state.set_state(Form.answer)

@dp.message(Form.answer)
async def answer(message: types.Message, state: FSMContext):
    town = message.text
    await state.clear()
    success, weather = get_weather_data(town)
    if success:
        await message.answer(weather['detailed_status'] + '\nТемпература: ' + str(weather['temp']) + 'C' + '\nВлажность: ' + str(weather['humidity']) + '%')
    else:
        await message.answer('Некорректный ввод. Попробуйте еще раз')
        await message.bot.send_message('/start', message.from_user.id)