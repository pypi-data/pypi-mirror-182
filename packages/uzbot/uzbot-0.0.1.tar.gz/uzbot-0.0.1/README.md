```python
from uzbot import run_bot, types

bot = run_bot(TOKEN)

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "Hello!!!")

bot.polling()
```