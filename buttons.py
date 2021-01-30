from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("🎲 Рандомное число")
item2 = types.KeyboardButton("😊 Как дела?")

markup.add(item1,item2)


markup1 = types.InlineKeyboardMarkup(row_width=2)
item3 = types.InlineKeyboardButton("Хорошо", callback_data='good')
item4 = types.InlineKeyboardButton("Не очень", callback_data='bad')
markup1.add(item3, item4)