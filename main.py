import telebot
from telebot import types
bot = telebot.TeleBot('5606712276:AAEtldtsFdxq3LOj6eOylLqd31qLl8Qeu-M')
f = open('questions.txt', "r", encoding="utf-8")
l = [0]*29
a = []
#pro = open('prof.txt', 'r', encoding='utf-8')

#for i in pro:
#    prof.append(i)

for i in f:
    a.append(i)
@bot.message_handler(commands=['start'])
def start(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Начать тестирование")
    markup.add(item1)

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGbAhjcreIMcC-pDZAa3pLcMuRnt05NwACuAADMNSdEfdlhg3PDOsVKwQ')
    bot.send_message(message.chat.id, 'Привет, '+str(message.from_user.first_name)+'! Рады приветствовать тебя в телгерамм-боте'
                                ' команды Шаг Вперёд. Наша команда подобрала парочку вопросов, с целью помочь тебе определиться с будущей профессией)\n Условия:\n'
                    'Если Вам очень нравится то, о чем спрашивается в вопросе, в бланке ответов рядом с его номером поставьте два ("2")  , \n если просто нравится - один ("1"),'
                    ' если не знаете, сомневаетесь - ноль ("0"),\n если не нравится - минус один ("-1"), а если очень не нравится - минус два("-2").'
                        ' Отвечайте на вопросы, не пропуская ни одного из них.'
                                        ' Нажми на кнопку <strong>"Начать тестирование"</strong>, чтобы начать тестирование'.format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private' and message.text == "Начать тестирование":
        for i in range(len(a)):
            #keyboard
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item_min2 = types.InlineKeyboardButton("-2", callback_data='-2')
            item_min1 = types.InlineKeyboardButton("-1", callback_data='-1')
            item_null = types.InlineKeyboardButton("0", callback_data='0')
            item_pl1  = types.InlineKeyboardButton("1", callback_data='1')
            item_pl2  = types.InlineKeyboardButton("2", callback_data='2')

            markup.add(item_min2, item_min1, item_null, item_pl1, item_pl2)

            bot.send_message(message.chat.id, a[0].format(message.from_user, bot.get_me()), parse_mode='html',
                                reply_markup=markup)
            if message.text =='Ответ принят.':
                    bot.send_message(message.chat.id, a[i].format(message.from_user, bot.get_me()),
                                 reply_markup=markup)
            #bot.send_message()
@bot.callback_query_handler(func=lambda call: call.data in ['-2','-1', '0', '1','-2'])
def callback_inline(call):
    try:
        global l
        if call.message:
            if call.data == '-2':
                 l[i%30] += -2
                 bot.send_message(call.message.chat.id, 'Ответ принят.')
            elif call.data == '-1':
                 l[i%30] += -1
                 bot.send_message(call.message.chat.id, 'Ответ принят.')
            elif call.data == '0':
                 l[i%30] += 0
                 bot.send_message(call.message.chat.id, 'Ответ принят.')
            elif call.data == '1':
                 l[i%30] += -2
                 bot.send_message(call.message.chat.id, 'Ответ принят.')
            elif call.data == '2':
                 l[i%30] += 2
                 bot.send_message(call.message.chat.id, 'Ответ принят.')
            else:
                bot.send_message(call.message.chat.id, 'Uncorrect answer')

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="✅")

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
