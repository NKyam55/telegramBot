import telebot
token="7118386944:AAFMh5b2AqXqfUale6tKY_KtG7zeZiuh3yo"
bot=telebot.TeleBot(token)
@bot.message_handler()
def main(message):
	bot.send_message(message.chat.id,message.text)
bot.polling(none_stop=True)