import telebot
import config
import validators
import os
from PIL import Image
import png
from QRcode import *


bot = telebot.TeleBot(config.ActiveBotToken)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello. Send me a link and I will convert it into QR-Code")


@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id, "Help Menu\n\n1. To convert link into image with QR-Code - just send me a link\n"
                                      "2. To convert picture with QR-Code into image - send me this picture. ")


@bot.message_handler(content_types=['text'])
def photoToLink(message):
    try:
        flag = True
        for i in message.text:
            if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.!~*( )'/:":
                flag = False
                break
        if validators.url(message.text) and flag:
            qrName = str(message.from_user.username) + str(message.message_id) + ".png"
            qrCreate(qrName, message.text)
            bot.send_photo(message.chat.id, photo=open('{}'.format(qrName), 'rb'))
            os.remove(qrName)
        elif validators.url('https://' + message.text) and flag:
            qrName = str(message.from_user.username) + str(message.message_id) + ".png"
            qrCreate(qrName, 'https://' + message.text)
            bot.send_photo(message.chat.id, photo=open('{}'.format(qrName), 'rb'))
            os.remove(qrName)

    except TypeError as e:
        print("Wild Type Error occured! It uses \033[93m", e)
        print('\033[0m')
        pass


# @bot.message_handler(content_types=['photo'])
# def photoToLink(message):
#     try:
#         file_info = bot.get_file(message.photo[0].file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#         src = file + message.photo[0].file_id
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#     except TypeError as e:
#         print("Wild Type Error occured! It uses \033[93m", e)
#         print('\033[0m')
#         pass


bot.polling(none_stop=True)
