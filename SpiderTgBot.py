# -*- coding: utf-8 -*-
import telebot

# Инициализируем бота
bot = telebot.TeleBot("")

@bot.message_handler(commands=['чай'])
def send_tea_animation(message):
    caption = "Всем чай, фыр-фыр!"

    bot.send_animation(
        chat_id=message.chat.id,
        animation='https://99px.ru/sstorage/86/2020/07/image_862007201029445860614.gif',
        caption=caption,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(commands=['правила'])
def send_tea_animation(message):
    bot.send_message(message.chat.id, "Полные правила - https://telegra.ph/Pravila-Pautinki-02-13", reply_to_message_id=message.message_id)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'animation', 'sticker', 'video', 'video_note', 'voice'])
def main(message):
    if message.from_user.id == 777000:
        bot.send_message(message.chat.id, "Ребят, БЕЗ СПОЙЛЕРОВ! Уважайте других. Правила - https://telegra.ph/Pravila-Pautinki-02-13", reply_to_message_id=message.message_id)

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='https://telegra.ph/Pravila-Pautinki-02-13 - Правила Чатика. Добро пожаловать')
    bot.send_sticker(message.chat.id, sticker = 'CAACAgIAAxkBAAMEaHVV276PEA1yvRz6TTqu0GaKtmsAAqNzAAK5J9FJeP2is1NBOnk2BA', reply_to_message_id=message.message_id)

bot.infinity_polling()