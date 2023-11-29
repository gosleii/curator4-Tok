import telebot

bot = telebot.TeleBot("6948601782:AAG_eF8L49Pi39eEaT2DmfRcRLWJnV9SLrQ")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Ну привет. \nВведи /gift или /sigar")


@bot.message_handler(commands=['gift'])
def main(message):
    bot.send_message(message.chat.id, "Ого ну держи вот для тебя есть одна класс команда /uwpm, введи ее")


@bot.message_handler(commands=['sigar'])
def main(message):
    bot.send_message(message.chat.id, "Курить плохо………… телефон на базу :/")


@bot.message_handler(commands=['uwpm'])
def main(message):
    bot.send_message(message.chat.id, " Спасибо! Ваш кредит успешно оформлен!")

bot.infinity_polling()