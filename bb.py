import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json

TOKEN = '6180784063:AAFQ53Vb3rt-38jf1IB7-3kiNMUg2fXIRII'
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Info about creater'))
keyboard.add(KeyboardButton('Activity'))
keyboard.add(KeyboardButton('Cute dogs'))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "How i can help u?", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard)

def get_act():
    response = requests.get('https://www.boredapi.com/api/activity')
    resp = response.json()
    r = {resp['activity']}
    return r

def get_dog():
    c = r"https://random.dog/woof.json"
    respon = requests.get(c)
    resp = json.loads(respon.text)
    r = {resp['url']}
    return r

@bot.message_handler(func=lambda s: 'Activity' in s.text)
def echo_message(message):
    bot.send_message(message.chat.id, get_act())


@bot.message_handler(func=lambda s: 'Info about creater' in s.text)
def echo_message(message):
    bot.send_message(message.chat.id, "Автором данного бота является Кузнецова Елена, на данный момент ее возраст составляет 14 лет. Создание данного бота было благодаря практике на курсах",reply_markup=keyboard)

@bot.message_handler(func=lambda s: 'Cute dogs' in s.text)
def echo_message(message):
    bot.send_message(message.chat.id, get_dog())

bot.infinity_polling()