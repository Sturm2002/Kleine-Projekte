import discord
import csv,json,os,asyncio

jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)
jsonvals = json.load(jsonfile)

SecretKey = jsonvals["DiscordBot"]["Settings"]["SecretToken"]

client = discord.Client()

def StartDisBot():
    client.run(SecretKey)

def StopDisBot():
    if not client.is_closed():
        client.close()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message: discord.message):
    if message.author == client.user:
        #await message.channel.send("Lol!")
        return

    if message.content.startswith("§help"):
        await message.channel.send("halt die fresse, noch nicht implementiert 🖕")

    if message.content.startswith("§myInfos"): 
        await message.channel.send(message.author)

    if message.content.startswith("§rate"):
        await message.channel.send(f"brudi {message.author} lass mal ein Like da du huan")
    
    if message.content.startswith("§devStats"):
        await message.channel.send(client.get_user(184016791880728576))

@client.event
async def on_reaction_add(reaction,user):
    if user == client.user:
        return
    else:
        print(reaction)


#client.run('NzgzMzY2MzAwMzY1MDk1MDAy.X8ZsuA.itTA1eFUg6QfDXEwTkzH6qyV0tg')