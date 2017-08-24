import telepot
from telepot.loop import MessageLoop
import time
import sys


def handle_message(message):
    command = message['text'].lower()
    id = message['chat']['id']

    if command == '/start':
        bot.sendMessage(id, "Hi, this is your To Do List bot. Send /help to get the list of commands")

    elif command == '/help':
        response = 'Commands:\n'
        response += '/start: initialize the bot\n'
        response += '/todo: send some item\n'
        response += '/done: finish some item\n'
        response += '/list: list your items\n'

        bot.sendMessage(id, response)
        

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()
print("Waiting...")

while 1:
    time.sleep(10)
