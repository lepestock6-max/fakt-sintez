import telebot
import pyttsx3
import requests
from config import token
bot = telebot.TeleBot(token)

engine = pyttsx3.init()

@bot.message_handler(command=["start"])
def bot_start(message):
    bot.send_message(
        message,
        f"Привет, я твой бот, для случайных и интересных фактов я не только напишу их тебе, но ещё и озвучу!\n Пробуй и узнавай факты!\n напиши команду /fact чтобы я написал и озвучил рандомный интересный факт. {message.from_user.first_name}!\n"
    )

@bot.message_handler(command=["fact"])
def bot_start(message):
    bot.reply_to(
        "def_fact"
    )

    rate = engine.getProperty('rate')   
        engine.setProperty('rate', 105)

        volume = engine.getProperty('volume')   
        print (volume)                          
        engine.setProperty('volume',1.0) 

        voices = engine.getProperty('voices')      
        engine.setProperty('voice', voices[0].id)  

        engine.say(def_fact)
        engine.runAndWait()
        engine.stop()

bot.polling()