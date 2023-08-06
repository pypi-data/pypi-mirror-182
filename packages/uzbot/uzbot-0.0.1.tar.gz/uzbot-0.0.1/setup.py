# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['uzbot']
install_requires = \
['pyTelegramBotAPI>=4.8.0,<5.0.0']

setup_kwargs = {
    'name': 'uzbot',
    'version': '0.0.1',
    'description': 'A simple library for creating a Telegram-bot.',
    'long_description': '```python\nfrom uzbot import run_bot, types\n\nbot = run_bot(TOKEN)\n\n@bot.message_handler(commands=["start"])\ndef hello(message):\n    bot.send_message(message.chat.id, "Hello!!!")\n\nbot.polling()\n```',
    'author': 'ozodbeksobirjonovich',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
