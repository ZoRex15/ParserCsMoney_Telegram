from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import menu, start
from FSM.states import FSMChoiseFilters
from database.requests import Database
from service.rebbit import RebbitMQ

import os


router = Router()

@router.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    Database.add_user(user_id=int(message.from_user.id))
    await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=start)

@router.message(Command(commands=['menu']))
async def send_menu(message: Message, state: FSMContext):
    await message.answer(text='Меню', reply_markup=menu)

@router.callback_query(F.data == 'menu')
async def go_to_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text='Меню', reply_markup=menu)

@router.callback_query(F.data == 'choise_filters')
async def choise_filters(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMChoiseFilters.choise_filters)
    await callback.message.delete()
    await callback.message.answer(text='<b>Введите фильтры по примеру</b>\n\n'
                                  'Пример: максемальная цена минимальная цена\n'
                                  'Пример_2: 100 10')
    
@router.message(StateFilter(FSMChoiseFilters.choise_filters))
async def set_filters(message: Message, state: FSMContext):
    prices = tuple(map(float, message.text.split(' ')))
    max_price, min_price = max(prices), min(prices)
    Database.set_filters(
        user_id=message.from_user.id,
        max_price=max_price,
        min_price=min_price
    )
    await state.clear()
    await message.answer(text='Меню', reply_markup=menu)

@router.callback_query(F.data == 'start')
async def start_parser(callback: CallbackQuery, state: FSMContext):
    os.system('sudo systemctl start Parser')
    await callback.answer(text='Запуск парсера')

@router.callback_query(F.data == 'stop')
async def stop_parser(callback: CallbackQuery, state: FSMContext):
    os.system('sudo systemctl stop Parser')
    RebbitMQ.clear_queue()
    await callback.answer(text='Остановка парсера')

