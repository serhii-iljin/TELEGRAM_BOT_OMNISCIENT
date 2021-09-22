import telebot
import wolframalpha
bot = telebot.TeleBot('1930969642:AAEH0CC-EYezvPVOvuM45OEg4_L8Wjproxo')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Just type your question in, come on!\nIf you use this bot in group just type \"!\" before your question.\nOther commands: /help, /start, /contacts.')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This bot can answer every your question!\nOther commands: /help, /start, /contacts.')

@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, 'Telegram: @serhii_iljin, GitHub: https://github.com/serhii-iljin, LinkedIn: https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D1%96%D0%B9-%D1%96%D0%BB%D1%8C%D1%97%D0%BD-aaaa3b219/')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if (message.text[0] != '!') and ((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        return
    if (message.text[0] == '!') and not((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        q = message.text[1:]
    else:
        q = message.text
    client = wolframalpha.Client('7HXRW2-X5A2AXYYPY')
    res = client.query(q)
    try:
        bot.send_message(message.chat.id, (next(res.results).text))
    except:
        bot.send_message(message.chat.id, 'Sorry, I don\'t know.')

bot.polling()
