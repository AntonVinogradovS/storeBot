from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

firstKeyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Каталог")).add(KeyboardButton(text="Связаться с нами"))

catalogKeyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="💄Косметика", callback_data="cosmetic"))\
    .insert(InlineKeyboardButton(text="🍬Азиатские сладости", callback_data="sweets"))\
    .add(InlineKeyboardButton(text="🎁Подарочные боксы", callback_data="box"))\
    .insert(InlineKeyboardButton(text="📿Аксессуары", callback_data="accessories"))

adminKeyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Каталог")).add(KeyboardButton(text="Добавить")).add(KeyboardButton(text="Удалить")).add(KeyboardButton(text="Количество пользователей"))

choosingCategoryKeyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="Косметика", callback_data="add cosmetic"))\
    .insert(InlineKeyboardButton(text="Азиатские сладости", callback_data="add sweets"))\
    .add(InlineKeyboardButton(text="Подарочные боксы", callback_data="add box"))\
    .insert(InlineKeyboardButton(text="Аксессуары", callback_data="add accessories"))

choosingCategoryDelKeyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text="Косметика", callback_data="del cosmetic"))\
    .insert(InlineKeyboardButton(text="Азиатские сладости", callback_data="del sweets"))\
    .add(InlineKeyboardButton(text="Подарочные боксы", callback_data="del box"))\
    .insert(InlineKeyboardButton(text="Аксессуары", callback_data="del accessories"))

def f(category, id):
    InlineDelKeyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text = 'Удалить', callback_data=f'product {category}|{id}'))
    return InlineDelKeyboard
