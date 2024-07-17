import telebot
from telebot import types
from Config import token
from Item_GraphQL import return_item_task
from Item_GraphQL import search_task
from sqlite_test import search_ammo



bot = telebot.TeleBot(token)
dict_item_task = search_task()
#Стартовый диалог бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, я твой помощник в игре "Escape from Tarkov", для работы со мной напиши "/menu"')

#кнопки в меню
@bot.message_handler(commands=['menu'])
def button_info(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_item = types.KeyboardButton(text = 'Предмет')
    button_ammo = types.KeyboardButton(text='Патроны')
    keyboard.add(button_item)
    keyboard.add(button_ammo)
    bot.send_message(message.chat.id,'Что вы хотите узнать?',reply_markup=keyboard)

#Хендлер отвечающий за работу кнопки "Предметы"
@bot.message_handler(content_types=['text'])
def items_info(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if message.text.lower() == 'предмет':
       msg = bot.send_message(message.chat.id, 'Какой предмет вас интересует?', reply_markup=keyboard)
       bot.register_next_step_handler(msg, message_item)
    if message.text.lower() == 'патроны':
       msg = bot.send_message(message.chat.id, 'Какой патрон вас интересует?', reply_markup=keyboard)
       bot.register_next_step_handler(msg, message_ammo)

#Хендлер отвечающий за работу кнопки "Предметы"
@bot.message_handler(content_types=['text'])
def message_item(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    text,photo = return_item_task(dict_item_task,message.text)
    bot.send_message(message.chat.id, text,reply_markup=keyboard, disable_web_page_preview=True, parse_mode = 'html')
    if photo != '':
        bot.send_photo(message.chat.id,photo, reply_markup=keyboard)


#Хендлер отвечающий за работу кнопки "Патроны"
@bot.message_handler(content_types=['text'])
def message_ammo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    text = search_ammo(message.text)
    bot.send_message(message.chat.id, text,reply_markup=keyboard, disable_web_page_preview=True, parse_mode = 'html')




if __name__=='__main__':
    bot.infinity_polling()