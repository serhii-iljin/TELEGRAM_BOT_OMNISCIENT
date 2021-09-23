import telebot
from telebot import types
import wolframalpha

bot = telebot.TeleBot('1930969642:AAEH0CC-EYezvPVOvuM45OEg4_L8Wjproxo')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Just type your question in, come on!\nIf you use this bot in group chats just type \"!\" before your question.\nAll commands: /help, /start, /contacts, /review, /examples.')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'This bot can answer every your question!\nAll commands: /help, /start, /contacts, /review, /examples.')

@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.chat.id, 'Developer:\n-Telegram: @serhii_iljin;\n-GitHub: https://github.com/serhii-iljin,\n-LinkedIn: https://www.linkedin.com/in/%D1%81%D0%B5%D1%80%D0%B3%D1%96%D0%B9-%D1%96%D0%BB%D1%8C%D1%97%D0%BD-aaaa3b219/\nLogo designed by @Andrii_e_o.')

@bot.message_handler(commands=['examples'])
def start_message(message):
    bot.send_message(message.chat.id, 'General questions:\n-Temperature in Kherson?\n-Weather in kherson?\n-What is your name?\n\nMaths questions:\n-Solve x^5-x^3+3x^2-3=0\n-Integral x^2+ln(x)-1/x-32\n-Derivative x^3+sqrt(x)')

@bot.message_handler(commands=['review'])
def start_message(message):
    if (message.chat.type == 'supergroup') or (message.chat.type == 'group'):
        bot.send_message(message.chat.id,"Write your review directly in the bot.")
        return
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    dismiss = types.KeyboardButton('Cancel')
    sendMessage = types.KeyboardButton('Send message')
    markup.add(dismiss)
    markup.add(sendMessage)
    bot.send_message(message.chat.id, "Please, write your review with \"#\" at the beggining in the next message ans press \"Send message\" button or press \"Cancel\" to exit review writing mode", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def send_text(message):
    #Name case
    if ((message.text.find("your") != -1) and (message.text.find("name")) != -1):
        bot.send_message(message.chat.id, 'I\'m omniscient bot - the most clever bot on telegram!')
        return
    #Cancellation case
    if(message.text == 'Cancel' or message.text == 'Send message'):
        return
    #Review case
    if(message.text[0] == '#'):
        bot.send_message(443610747, message.text)
        bot.send_message(443610747, message.chat.id)
        try:
            bot.send_message(443610747, message.from_user.username)
        except:
            try:
                bot.send_message(443610747, message.from_user.first_name)
                try:
                    bot.send_message(443610747, message.from_user.second_name)
                except:
                    bot.send_message(443610747, "No second name\n")
            except:
                bot.send_message(443610747, "No first name\n")
        return
    #Determine bot behaviour depending on chat type
    if (message.text[0] != '!') and ((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        return
    if (message.text[0] == '!') and ((message.chat.type == 'supergroup') or (message.chat.type == 'group')):
        q = message.text[1:]
    else:
        q = message.text
    #Getting answer
    client = wolframalpha.Client('7HXRW2-X5A2AXYYPY')
    res = client.query(q)
    try:
        bot.send_message(message.chat.id, (next(res.results).text))
    except:
        bot.send_message(message.chat.id, 'Sorry, I don\'t know.')

bot.polling()
