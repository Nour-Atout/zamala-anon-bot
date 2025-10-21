import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_to_group(message):
    if message.chat.type == "private":
        text = f"💬 رسالة مجهولة:\n\n{message.text}"
        bot.send_message(GROUP_ID, text)

bot.polling(non_stop=True)
