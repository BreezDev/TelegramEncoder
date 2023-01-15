# TelegramEncoder
Introducing the Code Generator Bot for Telegram, a simple tool that encodes text into secret messages. Built using python-telegram-bot library and perfect for adding an extra layer of security.

This bot has two command handlers, one for the /start command and another for the /encode command. When the /start command is received, the bot will reply with a welcome message. When the /encode command is received, the bot will take the text of the message and replace each letter with the letter that comes after it in the alphabet (using the ord() and chr() functions). The encoded message is then sent as a reply.

Also please make sure to replace YOUR_BOT_TOKEN with your actual token for this script to work.
