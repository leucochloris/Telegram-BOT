import telebot
import sqlite3

bot = telebot.TeleBot("5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198",
                      parse_mode=None)

############### create function which will do something by command /start -------> append data to db
@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('purple.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS purple_data (
        id INTEGER
    )""")
    connect.commit()

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

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'эй':
        bot.reply_to(message, 'Cебе ЭЙ`кни!')
    else:
        bot.reply_to(message, 'I DONT understand you...')


bot.infinity_polling()
