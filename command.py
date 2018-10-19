import re

class Command(object):
    def __init__(self):
        self.commands = {
            "jump" : self.jump
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
     