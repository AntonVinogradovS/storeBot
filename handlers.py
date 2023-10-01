from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery, MediaGroup, InputMediaDocument
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from texts import *
from keyboards import * 
from database import *

async def cmdStart(message: types.Message):
    await message.answer(text=welcomeMessage, reply_markup=firstKeyboard)
    await sql_start_bot_write(message.from_user.id)


    

async def catalog(message: types.Message):
    print(message.from_user.id)
    await message.answer(text="🛒 Выберите категорию:", reply_markup=catalogKeyboard)
async def connection(message: types.Message):
    await message.answer(text="✉️ Свяжитесь с администраторами по следующим контактам:\n\
\n\
@lucky99_girl\n\
@alina666vagner\n\
\n\
Если вам необходимо обсудить заказ по телефону, вы можете позвонить по номеру: +7 902 356-55-74.")
async def cosmetic(callback_query: types.CallbackQuery):
    res = await sql_read_cosmetic()
    if len(res) != 0:
        for i in res:
            #await bot.send_photo(chat_id=callback_query.from_user.id,photo=i[1],caption=f"🎁 Название: {i[2]}\n📄 Описание: {i[3]}\n💰 Цена: {i[4]}₽\n🏷️ Артикул: {i[5]}")

            await bot.send_photo(chat_id=callback_query.from_user.id, photo = i[1], caption= f'Название: {i[2]}\nОписание: {i[3]}\nЦена: {i[4]}₽\nАртикул: {i[5]}')
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Товаров в данной категории, к сожалению, пока нет.")

async def sweets(callback_query: types.CallbackQuery):
    res = await sql_read_sweets()
    if len(res) != 0:
        for i in res:
            await bot.send_photo(chat_id=callback_query.from_user.id,photo=i[1],caption=f"🎁 Название: {i[2]}\n📄 Описание: {i[3]}\n💰 Цена: {i[4]}₽\n🏷️ Артикул: {i[5]}")
            #await bot.send_photo(chat_id=callback_query.from_user.id, photo = i[1], caption= f'Название: {i[2]}\nОписание: {i[3]}\nАртикул: {i[4]}')
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Товаров в данной категории, к сожалению, пока нет.")

async def box(callback_query: types.CallbackQuery):
    res = await sql_read_box()
    if len(res) != 0:
        for i in res:
            await bot.send_photo(chat_id=callback_query.from_user.id,photo=i[1],caption=f"🎁 Название: {i[2]}\n📄 Описание: {i[3]}\n💰 Цена: {i[4]}₽\n🏷️ Артикул: {i[5]}")
            #await bot.send_photo(chat_id=callback_query.from_user.id, photo = i[1], caption= f'Название: {i[2]}\nОписание: {i[3]}\nАртикул: {i[4]}')
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Товаров в данной категории, к сожалению, пока нет.")

async def accessories(callback_query: types.CallbackQuery):
    res = await sql_read_accessories()
    if len(res) != 0:
        for i in res:
            await bot.send_photo(chat_id=callback_query.from_user.id,photo=i[1],caption=f"🎁 Название: {i[2]}\n📄 Описание: {i[3]}\n💰 Цена: {i[4]}₽\n🏷️ Артикул: {i[5]}")
            #wait bot.send_photo(chat_id=callback_query.from_user.id, photo = i[0], caption= f'Название: {i[1]}\nОписание: {i[2]}\nАртикул: {i[3]}')
    else:
         await bot.send_message(chat_id=callback_query.from_user.id, text="Товаров в данной категории, к сожалению, пока нет.")

ADMIN = [1313463136, 1366797671, 5605262004]
async def adminInput(message: types.Message):
    if message.from_user.id in ADMIN:
        await message.answer("Вы администратор этого бота.", reply_markup= adminKeyboard)

class FSMAdd(StatesGroup):
    a0 = State()
    a1 = State()
    a2 = State()
    a3 = State()
    a4 = State()
    a5 = State()



async def choosingCategory(message: types.Message):
    await message.answer(text = "Выберите категорию, в которую хотите добавить товар.", reply_markup=choosingCategoryKeyboard) 
    await FSMAdd.a0.set()

async def cmdStop(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Добавление товара остановлено")

async def addProduct(callback_query: types.CallbackQuery, state: FSMContext):
    tmp = callback_query.data.replace('add ', '')
    async with state.proxy() as data:
        data['a0'] = tmp
    await FSMAdd.next()
    await bot.send_message(chat_id=callback_query.from_user.id, text="Прикрепите фото нового товара")
    

async def addProduct1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a1'] = message.photo[0].file_id
    await FSMAdd.next()
    await message.answer("Введите название продукта")

async def addProduct2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a2'] = message.text
    await FSMAdd.next()
    await message.answer("Введите описание продукта")

async def addProduct3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a3'] = message.text
    await FSMAdd.next()
    await message.answer("Введите цену продукта")

async def addProduct4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a4'] = message.text
    await FSMAdd.next()
    await message.answer("Отлично! Осталось указать артикул")


async def addProduct5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a5'] = message.text
    await state.finish()
    await sql_write(list(data.values()))
    await message.answer("Товар добавлен в каталог")


async def choosingCategoryDel(message: types.Message):
    await message.answer(text = "Выберите категорию, из которой хотите удалить товар", reply_markup=choosingCategoryDelKeyboard)

async def deleteProduct(callback_query: types.CallbackQuery):
    category = callback_query.data.replace('del ', '')
    if category == "cosmetic":
        res = await sql_read_cosmetic()
    elif category == "sweets":
        res = await sql_read_sweets()
    elif category == "box":
        res = await sql_read_box()
    else:
        res = await sql_read_accessories()
    if len(res) != 0:
        for i in res:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo = i[1], caption= f'Название: {i[2]}\nОписание: {i[3]}\nАртикул: {i[4]}', reply_markup=f(category, i[0]))
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Товаров в данной категории, к сожалению, пока нет.")


async def finishDel(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    info = callback_query.data.replace('product ', '')
    info = info.split("|")
    category = info[0]
    id = int(info[1])
    await sql_delete(category, id)

async def checkCountUsers(message: types.Message):
    count = await sql_start_bot_read()
    await message.answer(f"Количество людей, запустивших бота - {count}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmdStart, commands=['start'])
    dp.register_message_handler(cmdStop, commands=['stop'], state="*")
    dp.register_message_handler(catalog, text = 'Каталог')
    dp.register_message_handler(connection, text = 'Связаться с нами')
    dp.register_callback_query_handler(cosmetic, lambda c: c.data == "cosmetic")
    dp.register_callback_query_handler(sweets, lambda c: c.data == "sweets")
    dp.register_callback_query_handler(box, lambda c: c.data == "box")
    dp.register_callback_query_handler(accessories, lambda c: c.data == "accessories")
    dp.register_message_handler(adminInput, commands=['admin'])
    dp.register_message_handler(choosingCategory, text = "Добавить")
    dp.register_callback_query_handler(addProduct, lambda x: x.data and x.data.startswith('add '), state=FSMAdd.a0)
    dp.register_message_handler(addProduct1,content_types=['photo'], state=FSMAdd.a1)
    dp.register_message_handler(addProduct2, state=FSMAdd.a2)
    dp.register_message_handler(addProduct3, state=FSMAdd.a3)
    dp.register_message_handler(addProduct4, state=FSMAdd.a4)
    dp.register_message_handler(addProduct5, state=FSMAdd.a5)
    dp.register_message_handler(choosingCategoryDel, text = "Удалить")
    dp.register_message_handler(checkCountUsers, text = "Количество пользователей")
    dp.register_callback_query_handler(deleteProduct, lambda x: x.data and x.data.startswith('del '))
    dp.register_callback_query_handler(finishDel, lambda x: x.data and x.data.startswith('product '))
    
