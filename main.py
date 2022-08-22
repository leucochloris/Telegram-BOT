import telebot
import sqlite3
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.utils import executor

bot = telebot.TeleBot("5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198",
                      parse_mode=None)


############### greeting output
@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     'Greeting!   I`m bot-assistant, your guide to the world of English language!\n\nAbout us - /about\nRegistration - /reg\nHelp - /help')


############### about us output  (who we are...)
@bot.message_handler(commands=['about'])
def send_help(message):
    bot.reply_to(message,
                 'We are - school of education English language "EASY WAY" 📚📖📕\n\nOur company is young startup with a potential of billion of dollars! 🤑💵💰\n'
                 '\nWe have schools and representative offices in 5 cities. Other 10 cities are in the plans ✈✈✈\n\n'
                 'Have any question?! Just write to me: https://vk.com/funnymanalex')


############### create function which will do something by command /start -------> append data to db
@bot.message_handler(commands=['reg'])
def start(message):
    connect = sqlite3.connect('purple.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS purple_data (
        id INTEGER
    )""")
    connect.commit()
    bot.reply_to(message, 'Registration was successful !!!')

    ############### check data (uniq users should be ...)
    purple_id = message.chat.id
    cursor.execute(f"select id from purple_data where id = {purple_id}")
    data = cursor.fetchone()
    if data is None:
        ############### add values
        purple_list = [message.chat.id]
        cursor.execute("INSERT INTO purple_data VALUES(?);", purple_list)
        connect.commit()
    else:
        bot.reply_to(message, 'Ooh.... you are already here!')


############### create function which will do something by command /delete -------> delete data from  db
@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('purple.db')
    cursor = connect.cursor()

    ##### delete data from bd
    purple_id = message.chat.id
    cursor.execute(f'DELETE FROM purple_data WHERE id = {purple_id}')
    connect.commit()


@bot.message_handler()
def angry_user(message):
    if message.text.lower() == 'эй':
        bot.reply_to(message, 'Cебе ЭЙ`кни!')
    # else:
    #     bot.reply_to(message, 'I DONT understand you...')


bot.infinity_polling()
