import telebot
import requests
import json


bot = telebot.TeleBot('6104589582:AAGwJhlGLDlif-0FKeW8fTyDh7llTUr9TAs')
API = 'f47af694c647ce2582108ba7861d772f'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hello,send me name your city,please')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message,f'In the moment:{temp}')

        image = 'sun.png' if temp > 5.0 else 'sky.png'
        file = open('./' + image,'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, 'This is city is not have in world')


bot.polling(none_stop=True)