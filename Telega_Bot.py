import telebot
from telebot import types
from Config import token
from Key_GraphQL import find_keys_kvest

bot = telebot.TeleBot(token)

#Стартовый диалог бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, я твой помощник в игре "Escape from Tarkov", для работы со мной напиши "/menu"')

#кнопки в меню
@bot.message_handler(commands=['menu'])
def button_info(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_key = types.KeyboardButton(text = 'Ключи')
    keyboard.add(button_key)
    bot.send_message(message.chat.id,'Что вы хотите узнать?',reply_markup=keyboard)

#Хендлер отвечающий за работу кнопки "Ключи"
@bot.message_handler(content_types=['text'])
def keys_info(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if message.text.lower() == 'ключи':
       msg = bot.send_message(message.chat.id, 'Какой ключ вас интересует?', reply_markup=keyboard)
       bot.register_next_step_handler(msg, message_key)

#Хендлер отвечающий за работу кнопки "Ключи"
@bot.message_handler(content_types=['text'])
def message_key(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    text,photo = find_keys_kvest(message.text)
    bot.send_message(message.chat.id, text,reply_markup=keyboard, disable_web_page_preview=True)
    if photo != '':
        bot.send_photo(message.chat.id,photo, reply_markup=keyboard)



if __name__=='__main__':
    bot.infinity_polling()