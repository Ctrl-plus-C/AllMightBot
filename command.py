import re
from translate import translatefn
from news import fetch
from tweet import tweett
import tweepy
from bored import bore
from word import words
from weather import forecast
from currency import currency_convert
from quote import quote_generator
from jokes import random_joke
from mail import send_mail
from horoscope import hh
from pollution import pollution11

class Command(object):
    def __init__(self):
        self.commands = {
            "jump" : self.jump,
            "help" : self.help,
            "bored" : self.bored,
            "quote":self.quotes,
            "joke":self.joke,
            "weather" : self.weather,
            "news":self.news,
            "translate" :self.translate,
            "word" : self.word,
            "currency" : self.currency,
            "tweet":self.tweet,
            "mail" : self.mail, #todo
            "horoscope":self.horoscope,
            "pollution":self.pollution
        }
 
    def handle_command(self, user, command):
        response = "<@" + user + ">: "
        sentence = command.split()
        keyword = sentence[0]
     
        if keyword in self.commands:
            response += self.commands[keyword](sentence)
        else:
            response += "Sorry I don't understand the command: " + command + ".\n" + self.help(sentence)
         
        return response
         
    def jump(self, c_list):
        return "Kris Kross will make you jump jump"
     
    def help(self, c_list):
        response = "Currently I support the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"

    def translate(self, c_list):
        return translatefn(c_list)

    def news(self, c_list):
        return fetch(c_list)

    def tweet(self, c_list):
        return tweett(c_list)

    def bored(self, c_list):
        return bore(c_list)
    
    def word(self, c_list):
        return words(c_list[1])

    def mail(self, c_list):
        return send_mail(c_list)

    def weather(self, c_list):
        return forecast(c_list)

    def currency(self, c_list):
        return currency_convert(c_list[1],c_list[2],c_list[3])

    def quotes(self, c_list):
        return quote_generator()

    def joke(self, c_list):
        return random_joke()

    def horoscope(self, c_list):
        return hh(c_list[1],c_list[2])
    
    def pollution(self,c_list):
        return pollution11(c_list)