from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader


def hello(bot, update):
    update.message.reply_text(
        'Hola {}, soy un bot de prueba'.format(update.message.from_user.first_name))


def echo(bot, update):
    update.message.reply_text(text='Hola, no se lo que pusiste') ##update.message.text


def write_command (bot, update):
    update.message.reply_text(text='lei un comando')


updater = Updater('897986769:AAFGG7kN0IDOiCqTADqVxc735n6uAIeMD5k')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.dispatcher.add_handler(MessageHandler(Filters.command, lambda b, u: write_command))

updater.start_polling()
updater.idle()


class Precio(Item):
    pregunta = Field()


class Necxus(Spider):
    name = "precio4k"
    start_url = 'https://www.necxus.com.ar/categoria/50/500675/Smart-TV-UHD-4K/page/1/marca/23/'
    def parse(self, response):