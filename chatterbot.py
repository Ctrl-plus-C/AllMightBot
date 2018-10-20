from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def chat(query):
    chatbot = ChatBot("BotBot")
    response = chatbot.get_response(query)
    return response