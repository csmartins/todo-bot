import telepot
from telepot.loop import MessageLoop
import time
import sys

def handle_message(message):
    print(message)

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()
print("Waiting...")

while 1:
    time.sleep(10)
