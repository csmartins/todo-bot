# todo-bot

## steps hands-on
1: creating the bot

```python
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
```

2: responding something

```python
    def handle_message(message):
        command = message['text'].lower()
        id = message['chat']['id']
        
        if command == '/start':
            bot.sendMessage(id, "Hi, this is your To Do List bot. Send /help to get the list of commands")
```

3: get some help

```python
     elif command == '/help':
        response = 'Commands:\n'
        response += '/start: initialize the bot\n'
        response += '/todo: send some item\n'
        response += '/done: finish some item\n'
        response += '/list: list your items\n'
    
        bot.sendMessage(id, response)
```

4: send something to do

```python
    elif command.startswith('/todo'):
        new_item = command.split('/todo ')[1]
        bot.sendMessage(id, "This is your to do: {}".format(new_item))
```

5: save an item

```python
    elif command.startswith('/todo'):
        new_item = command.split('/todo ')[1]
        
        global todo_items
        todo_id = len(todo_items.items()) + 1
        todo_items[todo_id] = new_item
        
        bot.sendMessage(id, "Your to do '{}' was saved".format(new_item))
```

6: list your to dos
```python
    elif command == '/list':
        response = "Your to dos:\n"
        for k in todo_items.keys():
            response += '{}: {}\n'.format(k, todo_items[k])
        
        bot.sendMessage(id, response)
```

7: finish something
```python
    elif command.startswith('/done'):
        todo_id = command.split('/done ')[1]
        todo_items.pop(int(todo_id))
        
        bot.sendMessage(id, "To do #{} was marked as done. Use /list to see all your to dos.".format(todo_id))
```
