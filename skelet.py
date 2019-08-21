
import telebot


import random

import constant

bot = telebot.TeleBot(constant.token)
#bot.send_message(466835416, "test")
upd = bot.get_updates()
#print(upd)
print(bot.get_me())

a = 42
b = "qwerty"

print(type(a), type(b))

@bot.message_handler(content_types=["text"])
def any_msg(message):
    answer = ""
    answer2 = ""
    keyboardmain = telebot.types.InlineKeyboardMarkup(row_width=4)
    kno1 = telebot.types.InlineKeyboardButton(text="ПОКРОВСКИЙ", callback_data="1")
    kno2 = telebot.types.InlineKeyboardButton(text="ДЗЕРЖИНСКИЙ", callback_data="2")
    kno3 = telebot.types.InlineKeyboardButton(text="САКСАГАНСКИЙ", callback_data="3")
    kno4 = telebot.types.InlineKeyboardButton(text="ЦЕНТРАЛЬНЫЙ", callback_data="4")
    keyboardmain.add(kno1, kno2)
    keyboardmain.add(kno3,kno4)
    bot.send_message(message.chat.id,"\U0001F50DТЕБЯ ПРИВЕТСТВУЕТ МАГАЗИН\n\n"
                                     "\U0001F50DПОИСК КР №1\n\n"
                                     "\U0001F9EDВить здесь ты найдёшь\U0001F50D\n\n"
                                     "\U0001F449АМФЕТАМИН\U0001F443\n\n"
                                     "\U0001F449ГАШИШ\U0001F36B\n\n"
                                     "\U0001F449MDMA\U0001F444\n\n"
                                     "\U0001F449LSD\U0001F445\n\n"
                                     "\U0001F449ШИШКИ\U0001F33F\n\n"
                                     "\U0001F4E2ОТЗЫВЫ О РАБОТЕ ТУТ\U0001F4DC\n"
                                     "\nt.me/joinchat/AAAAAFkAVrOz3ei9erSXyg"
                                     "\n\nU0001F464ТАК ЖЕ ЕСТЬ ОПЕРАТОР\U0001F5E3"
                                     "\n"
                                     "\nt.me/PoiskKRBRO"
                                     "\n\n\U0001F50DЛЕГКО НАЙТИ\U0001F463\n\n "
                                     "\U0001F449ДЛЯ НАЧАЛА ВЫБЕРИ РАЙОН \U0001F575", reply_markup=keyboardmain)




@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="ПОКРОВСКИЙ", callback_data="1")
        kno2 = telebot.types.InlineKeyboardButton(text="ДЗЕРЖИНСКИЙ", callback_data="2")
        kno3 = telebot.types.InlineKeyboardButton(text="САКСАГАНСКИЙ", callback_data="3")
        kno4 = telebot.types.InlineKeyboardButton(text="ЦЕНТРАЛЬНЫЙ", callback_data="4")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3, kno4)
        bot.send_message(chat_id=call.message.chat.id, text="\U0001F44BТЕБЯ ПРИВЕТСТВУЕТ МАГАЗИН\n\n"
                                                            "\U0001F50DПОИСК КР №1\n\n"
                                     "\U0001F9EDВить здесь ты найдёшь\n\n"
                                     "\U0001F449АМФЕТАМИН\U0001F443\n\n"
                                     "\U0001F449ГАШИШ\U0001F36B\n\n"
                                     "\U0001F449MDMA\U0001F444\n\n"
                                     "\U0001F449LSD\U0001F445\n\n"
                                     "\U0001F449ШИШКИ\U0001F33F\n\n"
                                     "\U0001F4E2ОТЗЫВЫ О РАБОТЕ ТУТ\U0001F4DC\n"
                                     "\nt.me/joinchat/AAAAAFkAVrOz3ei9erSXyg"
                                     "\n\n\U0001F464ТАК ЖЕ ЕСТЬ ОПЕРАТОР\U0001F5E3"
                                     "\n"
                                     "\nt.me/PoiskKRBRO"
                                     "\n\n\U0001F50DЛЕГКО НАЙТИ\U0001F463\n\n "
                                     "\U0001F449ДЛЯ НАЧАЛА ВЫБЕРИ РАЙОН \U0001F575", reply_markup=keyboard)

    if call.data == "1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="РОЗА", callback_data="2.1")
        kno2 = telebot.types.InlineKeyboardButton(text="МУСОРСКОГО", callback_data="1.1")
        kno3 = telebot.types.InlineKeyboardButton(text="СВИТАНОК", callback_data="2.1")
        kno4 = telebot.types.InlineKeyboardButton(text="СУХАЯ", callback_data="3.1")
        kno5 = telebot.types.InlineKeyboardButton(text="КРЕС", callback_data="3.1")
        kno6 = telebot.types.InlineKeyboardButton(text="ПИОНЕР", callback_data="2.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3, kno4)
        keyboard.add(kno5, kno6)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id,  text="ВЫБЕРИ УЛИЦУ ПОИСКА:", reply_markup=keyboard)

    if call.data == "2":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="СОЦГОРОД", callback_data="1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ЧЕРВОНА", callback_data="2.1")
        kno3 = telebot.types.InlineKeyboardButton(text="СВЯТОГЕРОЕВСКАЯ", callback_data="4.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="\U0001F575"
                                                            "\n"
                                                            "ВЫБЕРИ УЛИЦУ ПОИСКА:", reply_markup=keyboard)


    if call.data == "3":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="ЮБИЛЕЙНАЯ", callback_data="2.1")
        kno2 = telebot.types.InlineKeyboardButton(text="АРТЁМ", callback_data="3.1")
        kno3 = telebot.types.InlineKeyboardButton(text="ОЛИМП", callback_data="2.1")
        kno4 = telebot.types.InlineKeyboardButton(text="95-й", callback_data="1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3, kno4)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ УЛИЦУ ПОИСКА:", reply_markup=keyboard)

    if call.data == "4":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="СТАРОВОКЗАЛЬНАЯ", callback_data="3.1")
        kno2 = telebot.types.InlineKeyboardButton(text="КАРЛА МАРКСА", callback_data="1.1")
        kno3 = telebot.types.InlineKeyboardButton(text="УКРАИНСКАЯ", callback_data="2.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ УЛИЦУ ПОИСКА:", reply_markup=keyboard)

    if call.data == "1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        kno3 = telebot.types.InlineKeyboardButton(text="MDMA\LSD", callback_data="4.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ ЧТО БУДЕШЬ ИСКАТЬ:", reply_markup=keyboard)

    if call.data == "2.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ ЧТО БУДЕШЬ ИСКАТЬ:", reply_markup=keyboard)

    if call.data == "3.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ГАШИШ", callback_data="3.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ ЧТО БУДЕШЬ ИСКАТЬ:", reply_markup=keyboard)


    if call.data == "4.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ВЫБЕРИ ЧТО БУДЕШЬ ИСКАТЬ:", reply_markup=keyboard)

    if call.data == "1.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="1г 350грн", callback_data="0.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="2г 700грн", callback_data="0.2.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="КАКОЙ КЛАД ТЕБЕ НУЖЕН???", reply_markup=keyboard)

    if call.data == "2.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="1г 160грн", callback_data="0.3.1")
        kno2 = telebot.types.InlineKeyboardButton(text="2г 300грн", callback_data="0.4.1")
        kno3 = telebot.types.InlineKeyboardButton(text="3г 420грн", callback_data="0.5.1")
        kno4 = telebot.types.InlineKeyboardButton(text="5г 600грн", callback_data="0.6.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3,kno4)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="КАКОЙ КЛАД ТЕБЕ НУЖЕН???", reply_markup=keyboard)

    if call.data == "3.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="0.5г 250грн", callback_data="0.7.1")
        kno2 = telebot.types.InlineKeyboardButton(text="1г 450грн", callback_data="0.8.1")
        kno3 = telebot.types.InlineKeyboardButton(text="2г 850грн", callback_data="0.9.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="КАКОЙ КЛАД ТЕБЕ  НУЖЕН???", reply_markup=keyboard)



    if call.data == "4.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="MDMA 550грн\шт", callback_data="0.0.1")
        kno2 = telebot.types.InlineKeyboardButton(text="LSD 550грн\шт", callback_data="0.0.2")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="КАКОЙ КЛАД ТЕБЕ НУЖЕН???\n\n"
                                                            "LSD\MDMA ДОЗИРОВКА 1шт"
                                                            "\nНА ДВОИХ", reply_markup=keyboard)

    if call.data == "0.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                            "\U0001F9FEID" + str(random.randint(1000,2000)) + ""
                                                            "\n\n"
                                                            "\U0001F48AАМФЕТАМИН 1г 350грн"
                                                            "\n\n"
                                                            "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                            "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                            "\n\n"
                                                            "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                            "t.me/PoiskKRBRO"
                                                            "\n"
                                                            "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.2.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F48AАМФЕТАМИН 2г 700грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.3.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                            "\U0001F9FEID" + str(random.randint(1000,2000)) + ""
                                                            "\n\n"
                                                            "\U0001F4A8ШИШКИ 1г 160грн"
                                                            "\n\n"
                                                            "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                            "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                            "\n\n"
                                                            "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                            "t.me/PoiskKRBRO"
                                                            "\n"
                                                            "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.4.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F4A8ШИШКИ 2г 300грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.5.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F4A8ШИШКИ 3г 420грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.6.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F4A8ШИШКИ 5г 600грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.7.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F449ГАШИШ 0.5г 250грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.8.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                "\n\n"
                                                                "\U0001F449ГАШИШ 1г 450грн"
                                                                "\n\n"
                                                                "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                "\n\n"
                                                                "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                "t.me/PoiskKRBRO"
                                                                "\n"
                                                                "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.9.1":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                    "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                    "\n\n"
                                                                    "\U0001F449ГАШИШ 2г 850грн"
                                                                    "\n\n"
                                                                    "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                    "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                    "\n\n"
                                                                    "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                    "t.me/PoiskKRBRO"
                                                                    "\n"
                                                                    "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.0.1":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                    "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                    "\n\n"
                                                                    "\U0001F9FCMDMA 1шт 550грн"
                                                                    "\n\n"
                                                                    "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                    "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                    "\n\n"
                                                                    "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ \n"
                                                                    "t.me/PoiskKRBRO"
                                                                    "\n"
                                                                    "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)

    if call.data == "0.0.2":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="ХОРОШИЙ ВЫБОР\U0001F44D\n\n\n"
                                                                    "\U0001F9FEID" + str(random.randint(1000, 2000)) + ""
                                                                    "\n\n"
                                                                    "\U0001F39FLSD 1шт 550грн"
                                                                    "\n\n"
                                                                    "\U0001F4B0\U0001F4B0ОПЛАТА\U0001F4B0\U0001F4B0"
                                                                    "\n\U0001F4B3EasyPay - 66333880\U0001F4B3"
                                                                    "\n\n" 
                                                                    "НЕ ЗАБУДЬ ПОДТВЕРДИТЬ ОПЛАТУ\n"
                                                                    "t.me/PoiskKRBRO"
                                                                    "\n"
                                                                    "НУЖНО ТОЛЬКО ЧЕК ИЛИ СКРИН ОПЛАТЫ", reply_markup=keyboard)


















bot.polling(none_stop=True, interval=0)