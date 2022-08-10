import telebot

#   5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198


bot = telebot.TeleBot("5596281432:AAGebrPobQ-RZHe7DnZUFhHRyC6t0rkK198",
                      parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ooh, howdy.... haven't seen you for a long time!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'эй':
        bot.reply_to(message, 'В жёпу себе ЭЙ`кни!')
    else:
        bot.reply_to(message, 'I DONT understand you...')


    # bot.reply_to(message, message.text)



bot.infinity_polling()
