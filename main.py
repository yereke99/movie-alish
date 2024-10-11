#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from FormaAdmin import *
from keyboard import*
from database import*
from config import*
from Forma import*
import asyncio
from traits import*
import time
from FormaAdmin import*

from aiogram.types import ParseMode


generator = Generator()
btn = Button()
db = Database()

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video_handler(message: types.Message, state: FSMContext):

    video_file_id = message.video.file_id
    
    async with state.proxy() as data:
        data['file_id'] = video_file_id 
    
    await bot.send_message(
        message.from_user.id,
        text="*FileID: %s*"%str(data['file_id']),
        parse_mode="Markdown",
    )   

@dp.message_handler(Text(equals="💸 Money"), content_types=['text'])
async def handler(message: types.Message):
    
    if message.from_user.id == admin or message.from_user.id == admin2 or message.from_user.id == admin3:
        sum = db.get_money_sum()
        await bot.send_message(
                message.from_user.id,
                text="""*💳 Жалпы қаражат: %d*"""%sum,
                parse_mode="Markdown",
                reply_markup=btn.admin()
            )    

@dp.message_handler(Text(equals="📨 Хабарлама жіберу"), content_types=['text'])
async def handler(message: types.Message):
    if message.from_user.id == admin or message.from_user.id == admin2 or message.from_user.id == admin3:
        await FormaAdmin.s1.set()
        await bot.send_message(
                message.from_user.id,
                text="""*✏️ Хабарлама типін таңдаңыз*""",
                parse_mode="Markdown",
                reply_markup=btn.typeMsg()
            )     


@dp.message_handler(Text(equals="📨 Әкімшіге хабарлама"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*@senior_coffee_drinker*\n\nhttps://wa.me/77088609319""",
        parse_mode="Markdown",
    ) 


@dp.message_handler(Text(equals="📲 Байланыс номері"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*https://wa.me/77088609319*""",
        parse_mode="Markdown",
    ) 

