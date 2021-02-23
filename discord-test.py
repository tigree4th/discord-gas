import discord
import random
client = discord.Client()

CHANNEL_ID = 813717329296228393
ACCESS_TOKEN = ""

random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
    "お嬢",
    "みら姉"
]

@client.event
async def on_ready():
    # Test Code
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):
    # Reject BOT
    if message.author.bot:
        return 

    if message.content == "鳴いて":
        content = random.choice(random_contents)
        message.channel = client.get_channel(CHANNEL_ID)
        await message.channel.send(content)
    elif message.content == "おはよう":
        message.channel = client.get_channel(CHANNEL_ID)
        await message.channel.send("おはよう！！")

client.run(ACCESS_TOKEN)