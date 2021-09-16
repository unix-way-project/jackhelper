
import telebot
import os

api_token = os.environ["API_TOKEN"]

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if "dima" in message.text:
		bot.reply_to(message, "Oh, I know you")
	else:
		bot.reply_to(message, message.text)

bot.polling()
