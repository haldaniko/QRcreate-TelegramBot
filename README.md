# QR Code Telegram Bot

This is a simple Telegram bot that converts links into QR codes and sends them back to the user. Users can send any valid URL to the bot, and it will generate a QR code image for that URL.

## Features

- Convert links to QR codes.
- Send QR code images back to users.

## Installation
```bash
https://github.com/haldaniko/QRcreate-TelegramBot.git
cd QRcreate-TelegramBot

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

(Copy .env.sample to .env and populate it with all required data)

python main.py
```

## Demo
![demo.png](demo.png)