import telebot
import time


bot = telebot.TeleBot("1132561268:AAE3wOl1o1V0rb_s6QVgmjVDDyBCgn_qMhU");



@bot.message_handler(commands=['start'])#старт
def welcome(message):
	bot.send_message(message.chat.id, "test")


while True:
	try:
	  bot.polling(none_stop=True)
	except: 
	  print('bolt')
	  time.sleep(5)
