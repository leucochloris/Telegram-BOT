import telebot
import sqlite3


#   5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198


bot = telebot.TeleBot("5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198",
                      parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def start(message):
    connect = sqlite3.connect('purple.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS purple_data (
        id INTEGER
    )""")
    connect.commit()


    #check data (uniq users should be ...)
    purple_id = message.chat.id
    cursor.execute(f"select id from purple_data where id = {purple_id}")
    data = cursor.fetchone()
    if data is None:
        #add values
        purple_list = [message.chat.id]
        cursor.execute("INSERT INTO purple_data VALUES(?);", purple_list)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Ooh.... you are already here!')
    # bot.reply_to(message, "Ooh, howdy.... thanks for join us!")




@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'эй':
        bot.reply_to(message, 'В жёпу себе ЭЙ`кни!')
    else:
        bot.reply_to(message, 'I DONT understand you...')


    # bot.reply_to(message, message.text)



bot.infinity_polling()
