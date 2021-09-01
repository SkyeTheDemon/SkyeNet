import discord
import datetime
import json

# Get Token
with open("config.json") as file:
    config = json.load(file)

TOKEN = config["token"]

# Actual Bot
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as:')
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("Booted up at: {}".format(datetime.datetime.utcnow()))
    print("Used in {} servers".format(len(client.guilds)))
    print('------')


@client.event
async def on_message(message):
    # This if statement stops the bot replying to itself
    if message.author == client.user:
        return
    if message.author.id == 699892206126760026:
        await message.add_reaction("💩")

    lower = message.content.lower()
    if lower.startswith("wawa")
        await message.channel.send("wawa!!")
    if any(lower.startswith(f"skye {verb}") for verb in ["fell asleep", "passed out"]):
        if message.author.id == 615249674084810763:
            await message.channel.send(f"<@{message.author.id}>, Fuck you")
        skye = message.guild.get_member(283837101554794497)
        bed = message.guild.get_channel(752293783558815854) 
        if not skye.voice or not skye.voice.channel or skye.voice.channel.id == 757711076912529460:
            await message.channel.send(f"<@{message.author.id}>, Skye hasn't passed out yet, liar.")
        elif skye.voice.channel.id == bed.id:
            await message.channel.send(f"<@{message.author.id}>, Skye already passed out.")
        else:
            await skye.move_to(bed, reason=message.content)
            await message.add_reaction("💙")

    elif lower.startswith("wholesome "):
        if lower.endswith("na"):
            await message.channel.send("that's a fucking joke.")
        elif lower.endswith("jp"):
            await message.channel.send("are your friends american?")
        elif lower.endswith("au"):
            await message.channel.send("They may be wholesome but they lag :(")
        elif lower.endswith("eu"):
            await message.channel.send("\u200B\n\u200B")

    elif any(weeb_shit in message.content.split() for weeb_shit in ["owo", "uwu", "umu", "88w88", "ÕwÕ", "ŌwŌ", "ÓwÒ", "ÒwÓ", "ÔwÔ", "8w8", "0w0", "69w69"]):
        shot = client.get_emoji(740427994602012692)
        await message.add_reaction(shot)

        
@client.event
async def on_voice_state_update(member, before, after):
    channels = {
        # Voice Channel: Role
        724674837817065572: 724674548703952979,
    }
    if after.channel:
        channel = after.channel
    elif before.channel:
        channel = before.channel

    if role := channels.get(channel.id):
        if after.channel == channel:
            await member.add_roles(role)
        else:
            await member.remove_roles(role)


client.run(TOKEN)
