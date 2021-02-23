import discord
import random
client = discord.Client()

random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
    "お嬢",
    "みら姉"
]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if message.content == "鳴いて":
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")

client.run("")