import telebot
import wolframalpha
bot = telebot.TeleBot('YOUR TOKEN HERE')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Just type your question in, come on!\nIf you use this bot in group just type \"!\" before your question.\nAll commands: /help, /start, /contacts.')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This bot can answer every your question!\nAll commands: /help, /start, /contacts.')

@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, 'Developer:\n-Telegram: @serhii_iljin;\n-GitHub: https://github.com/serhii-iljin,\n-LinkedIn: https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D1%96%D0%B9-%D1%96%D0%BB%D1%8C%D1%97%D0%BD-aaaa3b219/\nLogo designed by @Andrii_e_o.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    #Determine bot behaviour depending on chat type
    if (message.text[0] != '!') and ((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        return
    if (message.text[0] == '!') and ((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        q = message.text[1:]
    else:
        q = message.text
    #Getting answer
    client = wolframalpha.Client('YOUR CLIENT ID HERE')
    res = client.query(q)
    try:
        bot.send_message(message.chat.id, (next(res.results).text))
    except:
        bot.send_message(message.chat.id, 'Sorry, I don\'t know.')

bot.polling()
