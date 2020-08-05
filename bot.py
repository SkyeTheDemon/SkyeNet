import discord
import datetime

TOKEN = ""

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

    if "wawa" in message.content:
        await message.channel.send("wawa!!")

    if any(message.content.startswith(f"skye {verb}") for verb in ["fell asleep", "passed out"]):
        skye = message.guild.get_member(283837101554794497)
        bed = message.guild.get_channel(715335459433087098)
        if not skye.voice or not skye.voice.channel:
            await message.channel.send(f"<@{message.author.id}>, Skye hasn't passed out yet, liar.")
        elif skye.voice.channel.id == bed.id:
            await message.channel.send(f"<@{message.author.id}>, Skye already passed out.")
        else:
            await skye.move_to(bed, reason=message.content)
            await message.add_reaction("💙")

    elif message.content.startswith("wholesome "):
        if message.content.endswith("na"):
            await message.channel.send("that's a fucking joke.")
        elif message.content.endswith("jp"):
            await message.channel.send("are your friends american?")
        elif message.content.endswith("au"):
            await message.channel.send("They may be wholesome but they lag :(")
        elif message.content.endswith("eu"):
            await message.channel.send("\u200B\n\u200B")

    elif any(weeb_shit in message.content.split() for weeb_shit in ["owo", "uwu", "umu", "88w88", "ÕwÕ", "ŌwŌ", "ÓwÒ", "ÒwÓ", "ÔwÔ"]):
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
