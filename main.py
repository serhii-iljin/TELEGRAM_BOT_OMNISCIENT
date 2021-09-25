import telebot
import wolframalpha
bot = telebot.TeleBot('YOUR TOKEN HERE')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Just type your question in, come on!\nOther commands: /help, /start, /contacts.')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This bot can answer every your question!\nOther commands: /help, /start, /contacts.')

@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, 'Telegram: @serhii_iljin, GitHub: https://github.com/serhii-iljin, LinkedIn: https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D1%96%D0%B9-%D1%96%D0%BB%D1%8C%D1%97%D0%BD-aaaa3b219/')

@bot.message_handler(content_types=['text'])
def send_text(message):
    client = wolframalpha.Client('YOUR CLIENT ID HERE')
    res = client.query(message.text)
    try:
        bot.send_message(message.chat.id, (next(res.results).text))
    except:
        bot.send_message(message.chat.id, 'Sorry, I don\'t know.')

bot.polling()
