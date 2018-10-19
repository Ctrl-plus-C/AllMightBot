import re
from news import fetch
from quote import quote_generator

class Command(object):
    def __init__(self):
        self.commands = {
            "jump" : self.jump,
            "help" : self.help,
            "quote":self.quotes,
            "news":self.news
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

    def news(self, c_list):
        return fetch(c_list)

    def quotes(self, c_list):
        return quote_generator()

       