import telebot
import requests

bot = telebot.TeleBot("6065177825:AAF_FsGZDvOjWh7APHQ1ewKzkrlSEZBYkwA")

api_key = "e459295ba5efc5b6be65180283c0e8cb"

@bot.message_handler(commands=["start"])
def get_start(message):
    pass

def get_weather(city_name):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=en"
        result = requests.get(url).json()
        print(result)
        text = f"Температура - {result['main']['temp']}"
        return text
    except:
        return "Некоректні дані"


@bot.message_handler(content_types=["text"])
def get_message(message):
    city_name = message.text
    weather = get_weather(city_name)
    bot.send_message(message.chat.id,weather)

bot.polling()
