# - *- coding: utf- 8 - *-
import telebot
import os
import random
import urllib.request as urllib2
bot = telebot.TeleBot('1489033608:AAETh3fXu6GoCKnTDUhpx61OrH2kX0d_jMQ')
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Введите /start чтобы начать использование бота.
Вы можете:
- Получить рекомендации от создателя. 
- Получить список и ссылку на топ действующих аниме.
- Получить рандомный арт по аниме.""")

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Арт', 'Топ аниме' )
    user_markup.row('Рекомендации от создателя')
    bot.send_message(message.from_user.id, 'Добро пожаловать, ' + message.from_user.first_name, reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,'Надеюсь вам понравилось использовать бот, '+ message.from_user.first_name,
                     reply_markup=hide_markup)



@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Арт':
        bot.send_message(message.from_user.id,'Функция не работает.')
        #url = 'https://nyaa.shikimori.org/system/characters/preview/158925.jpg?1530483631'
        #urllib2.urlretrieve(url, 'url_image_jpg')
        #random_file = random.choice(all_files_in_directory)
        #with open('url_image_jpg', 'rb') as image:#'C:\lol\sos\lol.jpg', 'rb')
            #bot.send_chat_action(message.from_user.id, 'upload_photo')
            #bot.send_photo(message.from_user.id, image)#,parse_mode='HTML'
    elif message.text == 'Топ аниме':
        bot.send_message(message.chat.id, '<a href="https://shikimori.org/animes">Топ аниме</a>', parse_mode='HTML')
    elif message.text == 'Рекомендации от создателя':
        my_top = ['<a href="http://telegra.ph/Gorod-v-kotorom-menya-net-07-08">Город, в котором меня нет/'
                  'Boku dake ga inai machi</a>',
                  '<a href="http://telegra.ph/Kod-Gias-07-08">Код Гиас/Code Geass</a>',
                  '<a href="http://telegra.ph/Tetrad-SmertiDeath-Note-07-08">Тетрадь Смерти/Death Note</a>',
                  '<a href="http://telegra.ph/Vrata-SHtejna-07-08">Врата Штейна/Steins;Gate</a>',
                  '<a href="http://telegra.ph/Volejbol-07-08">Волейбол!!!/Haikyuu!!!</a>',
                  '<a href="http://telegra.ph/Gurren-Lagann-pronzayushchij-nebesa-07-08">'
                  'Гуррен Лаганн, пронзающий небеса/TTGL</a>',
                  '<a href="http://telegra.ph/Melanholiya-Haruhi-Sudzumii-07-08">Меланхолия Харухи Судзумии'
                  '/Suzumiya Haruhi no yuuutsu</a>',
                  '<a href="http://telegra.ph/Sozdannyj-v-bezdne-07-08">Созданный в бездне/Made in Abyss</a>',
                  '<a href="http://telegra.ph/Forma-Golosa-07-08">Форма голоса/Koe no Katachi</a>',
                  '<a href="http://telegra.ph/EHho-Terrora-07-08">Эхо Террора/Zankyou no Terror</a>']
        randomtop = random.choice(my_top)
        bot.send_message(message.chat.id, randomtop, parse_mode="HTML")
        # if bot.==randomtop:
        #     bot.send_message(message.chat.id, randomtop, parse_mode="HTML")
    #elif message.text == 'аудио'

    #     # url = 'https://cs7-2v4.vkuseraudio.net/p20/39cc00252b7ddc.mp3?extra=ewm_i53reK1n_eTDJeut98383nJj1TPvooDlsObUpTxo9fLP5elH2XIUBO3fmWAoCoPkpkeV5eBaMKjuyElNJWipahablxSB-v997fsh5l5B_Bo0YIzNTxqlMFpR0SAeeB0AeT8uB45hlqo'
    #     # urllib2.urlretrieve(url, 'url_audio_mp3')
    #     audio = open('D:\Programms\sokyoghoulop1.mp3', 'rb')
    #     bot.send_chat_action(message.from_user.id, 'upload_audio')
    #     bot.send_audio(message.from_user.id, audio)
    #     audio.close()

bot.polling(none_stop=True)
