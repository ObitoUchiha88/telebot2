
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
    keyboardmain.add(kno3, kno4)
    bot.send_message(message.chat.id, """\r
                            ```Й```*о*```х```*о*```х```*о*
    
                            *Я Капитан* `Кладмен`
                                              
                            *И я окуну тебя в пиратский мир*
                                
                            *Ведь здесь ты можешь отправиться 
                                             на поиски своего клад* 
                                
                                                        \U0001F449`_АМФЕТАМИН_`\U0001F443
                                                        
                                                        \U0001F449`_ГАШИШ_`\U0001F36B
                                                        
                                                        \U0001F449`_MDMA_`\U0001F444
                                                        
                                                        \U0001F449`_LSD_`\U0001F445
                                                        
                                                        \U0001F449`_ШИШКИ_`\U0001F33F
                                                        
    \U0001F4E2`Сюда попадают отзывы`
                                                                        `наших кладоискателей`\U0001F4DC
                                                                        
                                    t.me/joinchat/AAAAAFkAVrOz3ei9erSXyg
                                      
                                     \U0001F464*Так же есть Штурман*\U0001F5E3
                                                t.me/PoiskKRBRO
                                     
                                              *С Нами Легче Искать*
                                     
                                      *В какие воды ты хочешь выдвинутся???*""", parse_mode="Markdown", reply_markup=keyboardmain)




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
        bot.send_message(chat_id=call.message.chat.id, text="""\r
                            ```Й```*о*```х```*о*```х```*о*
    
                            *Я Капитан* `Кладмен`
                                              
                            *И я окуну тебя в пиратский мир*
                                
                            *Ведь здесь ты можешь отправиться 
                                             на поиски своего клад* 
                                
                                                        \U0001F449`_АМФЕТАМИН_`\U0001F443
                                                        
                                                        \U0001F449`_ГАШИШ_`\U0001F36B
                                                        
                                                        \U0001F449`_MDMA_`\U0001F444
                                                        
                                                        \U0001F449`_LSD_`\U0001F445
                                                        
                                                        \U0001F449`_ШИШКИ_`\U0001F33F
                                                        
    \U0001F4E2`Сюда попадают отзывы`
                                                                        `наших кладоискателей`\U0001F4DC
                                                                        
                                    t.me/joinchat/AAAAAFkAVrOz3ei9erSXyg
                                      
                                     \U0001F464*Так же есть Штурман*\U0001F5E3
                                                t.me/PoiskKRBRO
                                     
                                              *С Нами Легче Искать*
                                     
                                      *В какие воды ты хочешь выдвинутся???*""", parse_mode="Markdown", reply_markup=keyboard)

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
        bot.send_message(chat_id=call.message.chat.id,  text="""\r
        
        
        `Выбери берег куда отправится`""", parse_mode="Markdown",  reply_markup=keyboard)

    if call.data == "2":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="СОЦГОРОД", callback_data="1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ЧЕРВОНА", callback_data="2.1")
        kno3 = telebot.types.InlineKeyboardButton(text="СВЯТОГЕРОЕВСКАЯ", callback_data="4.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        
        
        `Выбери берег куда отправится`""", parse_mode="Markdown",  reply_markup=keyboard)


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
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        
        
        `Выбери берег куда отправится`""", parse_mode="Markdown",  reply_markup=keyboard)

    if call.data == "4":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="СТАРОВОКЗАЛЬНАЯ", callback_data="3.1")
        kno2 = telebot.types.InlineKeyboardButton(text="КАРЛА МАРКСА", callback_data="1.1")
        kno3 = telebot.types.InlineKeyboardButton(text="УКРАИНСКАЯ", callback_data="2.1")
        backbutton = telebot.types.InlineKeyboardButton(text="НАЗАД", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        
        
        `Выбери берег куда отправится`""", parse_mode="Markdown",  reply_markup=keyboard)

    if call.data == "1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        kno3 = telebot.types.InlineKeyboardButton(text="MDMA\LSD", callback_data="4.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери клад который желаешь найти`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "2.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери клад который желаешь найти`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "3.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="ШИШКИ", callback_data="2.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="ГАШИШ", callback_data="3.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери клад который желаешь найти`""", parse_mode="Markdown", reply_markup=keyboard)


    if call.data == "4.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="АМФЕТАМИН", callback_data="1.1.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери клад который желаешь найти`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "1.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="1г 350грн", callback_data="0.1.1")
        kno2 = telebot.types.InlineKeyboardButton(text="2г 600грн", callback_data="0.2.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери желаемый размер клада`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "2.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="1г 160грн", callback_data="0.3.1")
        kno2 = telebot.types.InlineKeyboardButton(text="2г 300грн", callback_data="0.4.1")
        kno3 = telebot.types.InlineKeyboardButton(text="3г 450грн", callback_data="0.5.1")
        kno4 = telebot.types.InlineKeyboardButton(text="5г 700грн", callback_data="0.6.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3,kno4)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери желаемый размер клада`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "3.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="0.5г 250грн", callback_data="0.7.1")
        kno2 = telebot.types.InlineKeyboardButton(text="1г 450грн", callback_data="0.8.1")
        kno3 = telebot.types.InlineKeyboardButton(text="2г 850грн", callback_data="0.9.1")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(kno3)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери желаемый размер клада`""", parse_mode="Markdown", reply_markup=keyboard)



    if call.data == "4.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        kno1 = telebot.types.InlineKeyboardButton(text="MDMA 550грн\шт", callback_data="0.0.1")
        kno2 = telebot.types.InlineKeyboardButton(text="LSD 550грн\шт", callback_data="0.0.2")
        backbutton = telebot.types.InlineKeyboardButton(text="ГЛАВНОЕ МЕНЮ", callback_data="mainmenu")
        keyboard.add(kno1, kno2)
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        `Выбери что предпочитаешь разделить со своей командой`
        *Тот кто это создал, говорит что одна штука убивает двоих в течении от 8 до 10 часов*
                               `Так что задумайся`""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.1.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *-1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*350UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*1g* `Амфетамин`\U0001F443
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.2.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *-1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*600UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*2g* `Амфетамин`\U0001F443
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.3.1":
        keyboard = telebot.types.InlineKeyboardMarkup()
        backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
        keyboard.add(backbutton)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *-1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*160UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*1g* `Шишек`\U0001F33F
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.4.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *-1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*300UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*2g* `Шишек`\U0001F33F
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.5.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*450UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*3g* `Шишек`\U0001F33F
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.6.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*700UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*5g* `Шишек`\U0001F33F
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.7.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*250UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*0.5g* `Гашиша`\U0001F36B
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.8.1":
            keyboard = telebot.types.InlineKeyboardMarkup()
            backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
            keyboard.add(backbutton)
            bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*450UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*1g* `Гашиша`\U0001F36B
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup = keyboard)

    if call.data == "0.9.1":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*850UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*2g* `Гашиша`\U0001F36B
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.0.1":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*550UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*1sz* `MDMA`\U0001F444
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D""", parse_mode="Markdown", reply_markup=keyboard)

    if call.data == "0.0.2":
                keyboard = telebot.types.InlineKeyboardMarkup()
                backbutton = telebot.types.InlineKeyboardButton(text="Связаться со Штурманом", url = 'https://t.me/PoisKKRBRO')
                keyboard.add(backbutton)
                bot.send_message(chat_id=call.message.chat.id, text="""\r
        \U0001F194""" + str(random.randint(100000, 200000)) + """

        `После удачного решения в поиске клада`
        
        *Тебе осталось только оплатить услуги Капитана*
        *На указаный кашелёк*
        
                     \n\U0001F4B3`BTC` *- 1LofV78v6S4SVP1yh8Xy6iHLfM9QyxqCwd*
                     
                     \n\U0001F4B3`EasyPay` *- 66333880*
                     
        ``` Тебе необходимо внести```
        \U0001F4B0*550UAH*\U0001F4B0`Для подтверждения своего участия в поиске`
        \U0001F4CD*1sz* `LSD`\U0001F39F
        *После оплаты нажми кнопку* "Связаться со штурманом" 
        ```Ведь именно у него будет находится твоя карта```\U0001F5FA
        
        
        _Удачных поисков_\U0001F44D """, parse_mode="Markdown", reply_markup=keyboard)



bot.polling(none_stop=True, interval=0)