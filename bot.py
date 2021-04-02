import discord
import discord as api
import random
import asyncio
from discord.ext import commands, tasks

client = commands.Bot(command_prefix=',')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('something'))
    print('Bot is Online')

@client.event
async def on_command_error(ctx, error):
    author = ctx.author

@client.command()
async def help(ctx):
    author = ctx.author

    print(f'Command "help" has been Triggered by {author}')
    await ctx.send('HELP COMMAND')

@client.command()
async def ping(ctx):
    author = ctx.author
    print(f'Command "ping" has been Triggered by {author}')
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print(f'{round(client.latency * 1000)}ms - {author}')

@client.command()
async def AmIGay(ctx):
    author = ctx.author
    print(f'Command "AmIGay" has been Triggered by {author}')
    ra = random.choice(['Yes', 'No'])
    await ctx.send("Your Answer:")
    await asyncio.sleep(2)
    await ctx.send(ra)
    await ctx.send("This is not homophobic in any way")
    print(f'{author} got answer "{ra}"')

@client.command()
async def AmIOk(ctx):
    author = ctx.author
    print(f'Command "AmIOk" has been Triggered by {author}')
    ra = random.choice(['Yes', 'No', 'Yes, but *BEANS*', 'No, but *BEANS*'])
    await ctx.send("Your Answer:")
    await asyncio.sleep(2)
    await ctx.send(ra)
    print(f'{author} got answer "{ra}"')

@client.command()
async def AmIKarlson(ctx):
    author = ctx.author
    ra = random.choice(['Yes, you are KARLSON', 'No, you aren\'t KARLSON', 'You are just a bean'])
    print(f'Command "AmIKarlson" has been Triggered by {author}')
    await ctx.send('Your Answer:')
    await asyncio.sleep(2)
    await ctx.send(ra)
    print(f'{author} got answer "{ra}"')

@client.command()
async def AmIBeans(ctx):
    author = ctx.author
    ra = random.choice(['Just Beans', 'Special Beans', 'KARLSON BEANS', 'You\'re one of the beans from "Jack and the Beanstalk', 'NEIN! YOU\'RE A POTATO'])
    print(f'Command "AmIBeans" has been Triggered by {author}')
    await ctx.send('Your Answer:')
    await asyncio.sleep(2)
    await ctx.send(ra)
    print(f'{author} got answer {ra}')

@client.command()
async def crysis(ctx):
    author = ctx.author
    ra = random.choice(['Markiplier', 'Jacksepticeye', 'PewDiePie', 'OSFirstTimer', 'Raid: Shadow Legends'])
    print(f'Command "crysis" has been Triggered by {author}')
    print(f'Randomly Generated for {author.name} this time is {ra}')
    await ctx.send(f'{author.name}: Can it run CRYSIS?\nBOT NAME: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: It should be able to run CRYSIS.\nBOT NAME: Yet Again...\n:regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Can anything in this store run CRYSIS?\nBOT NAME: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Well you arent much help are you?!\nBOT NAME: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Well I don\'t need your help, anyway!\nBOT NAME: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(2)
    await ctx.send('**A few weeks later...**')
    await ctx.send(f'MyCraftU2: Hey, can you please sponsor me?\n{ra}: :regional_indicator_n:  :regional_indicator_o:')

@client.command()
async def lottery(ctx):
    author = ctx.author
    usNu = []
    for num in range(7):
        usNu.append(random.randint(13, 69))
    usSu = []
    for num in range(3):
        usSu.append(random.randint(13, 69))
    winN = []
    for num in range(7):
        winN.append(random.randint(13, 69))
    winS = []
    for num in range(3):
        winS.append(random.randint(13, 69))
    if ctx.author.id == YOUR USER ID:
        print(f'Command "lottery" has been Triggered by {author}')
        await ctx.send('**Please Note That This Command Is A Work In Progress**\n**Until it gets fixed you must check the Supplementaries MANUALLY**')
        await asyncio.sleep(3)
        await ctx.send(f'Your Numbers: {usNu[0]}, {usNu[1]}, {usNu[2]}, {usNu[3]}, {usNu[4]}, {usNu[5]}\nYour Supplementaries: {usSu[0]}, {usSu[1]}')
        await ctx.send('The Goal is to get at least:\n1 regular number **OR** 1 Supplementary')
        await ctx.send('The Numbers are...')
        await asyncio.sleep(3)
        await ctx.send(f'**Winning Numbers: {winN[0]}, {winN[1]}, {winN[2]}, {winN[3]}, {winN[4]}, {winN[5]}\nSupplementaries: {winS[0]}, {winS[1]}**')

        for byte in usNu:
            if byte in winN:
                await ctx.send(f'Congratulations {author.name}! One of your Numbers are a Winner!')
                return
        await ctx.send(f'Bad luck {author.name}. One of your Numbers are not a Winner.')

        for byte in usNu:
            if byte in winN:
                await ctx.send(f'Congratulations {author.name}! One of your Supplementaries are a winner!')
                return
        await ctx.send(f'Bad luck {author.name}. One of your Supplementaries are not a Winner.')
        return

    if ctx.author.id != YOUR USER ID:
        print(f'{author} attempted to use command "lottery"')
        await ctx.send('This Command Is Under Maintenance')
        return

@client.command()
async def hsdistract(ctx):
    author = ctx.author
    print(f'Command "hsdistract" has been Triggered by {author}')
    await ctx.send('https://tenor.com/view/henry-stickmin-the-henry-stickmin-collection-distraction-gif-18174155')

@client.command()
async def relax(ctx):
    author = ctx.author
    print(f'Command "relax" has been Triggered by {author}')
    await ctx.send('The Top Video That Will Make You Relaxed in SECONDS: https://www.youtube.com/watch?v=V-_O7nl0Ii0')
    await asyncio.sleep(60)
    await ctx.send(f'If {author.name} clicked the video they just got Rick Rolled!')
    
@client.command()
async def embarrassed(ctx):
    author = ctx.author
    print(f'Command "embarrassed" has been Triggered by {author}')
    await ctx.send('https://tenor.com/view/the-simpsons-homer-simpson-good-bye-bye-no-gif-5173989')
    
@client.command()
async def spam(ctx, number : int, *, spam : str):
    author = ctx.author
    print(f'Command "spam" has been Triggered by {author}')
    print(f'Command "spam" has been Triggered by {author}')
    for example in range(number):
        await ctx.send(spam)

    if number > 1000:
        await ctx.send('ERROR MESSAGE')
        return

@client.command()
async def clear(ctx, amount=10):
    author = ctx.author
    print(f'Command "clear" has been Triggered by {author}')
    await ctx.channel.purge(limit=amount)

    if amount > 500:
        await ctx.send('ERROR MESSAGE')
        return

@client.command()
async def oauth2(ctx):
    author = ctx.author
    print(f'Command "oauth2" has been Triggered by {author}')
    await ctx.send('Here is the OAuth2 Link for MyCraftU2')
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=756726765719912501&permissions=8&scope=bot')

@client.command()
async def bigrigs(ctx):
    author = ctx.author
    print(f'Command "bigrigs" has been Triggered by {author}')
    await ctx.send('Here\'s a Link to a Free Version of BigRigs: <https://bit.ly/3psDhNs>')
    heh = await ctx.send(';)')
    await heh.delete()

@client.command()
async def command(ctx):
    author = ctx.author
    print(f'Command "command" has been Triggered by {author}')
    await ctx.send(f"Congratulations {author.mention}! You Commanded the bot with its command to say command!")
    await asyncio.sleep(1)
    await ctx.send("Command")
    
@client.command()
async def dm(ctx, member : api.Member, *, text="placeholder"):
    author = ctx.author
    print(f'Comamnd "dm" has been Triggered by {author}')
    if member.dm_channel == None:
        channel = await member.create_dm()
        await channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')
    elif member.dm_channel != None:
        await member.dm_channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')

@client.command()
async def dmd(ctx, member : api.Member, *, text="placeholder"):
    author = ctx.author
    print(f'Comamnd "dmd" has been Triggered by {author}')
    await ctx.messge.delete()
    if member.dm_channel == None:
        channel = await member.create_dm()
        await channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')
    elif member.dm_channel != None:
        await member.dm_channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')
        
@client.command()
async def servers(ctx):
    author = ctx.author
    guilds = []
    for guild in client.guilds:
        guilds.append(guild.name)
    print(f'Command "servers" has been Triggered by {author}')
    await ctx.send(', \n'.join(guilds))
    
@client.command()
async def hello(ctx):
    author = ctx.author
    print(f'Command "hello" has been Triggered by {author}')
    await ctx.send(f'Hello {author.name}')
    
@client.command()
async def serverInvite(ctx, server):
    author = ctx.author
    guild = discord.utils.get(client.guilds, name=server)
    server = client.get_guild(guild.id)
    channels = []
    for channel in server.text_channels:
        channels.append(channel)
    invite = await channels[0].create_invite()
    print(f'Command "serverInvite" has been Triggered by {author}')
    await ctx.send(invite.url)
    
@client.command()
async def avatar(ctx, member:api.Member=None):
    if member == None:
        member = ctx.author
    print(f'Command "avatar" has been Triggered by {member}')
    await ctx.send(member.avatar_url)
    
@client.command()
async def prefix(ctx):
    author = ctx.author
    print(f'Command "prefix" has been Triggered by {author}')
    await ctx.send(f'The prefix is ,')

@client.command()
async def rank(ctx):
    author = ctx.author
    print(f'Command "rank" has been Triggered by {author}')
    await ctx.send('Your rank for the server is...')
    await asyncio.sleep(2)
    await ctx.send('You do know I\'m not MEE6, right?')

@client.command()
async def corn(ctx):
    author = ctx.author
    ra = random.choice(['https://cdn.discordapp.com/attachments/744104860219211796/759318896502636544/corn.jpg', 'https://www.youtube.com/watch?v=j8qp3ITVqY0'])
    print(f'Command "corn" has been Triggered by {author}')
    await ctx.send(ra)

    if ra == 'https://cdn.discordapp.com/attachments/744104860219211796/759318896502636544/corn.jpg':
        print(f'{author} received the image')
        return

    else:
        print(f'{author} received the video')

@client.command()
async def abc(ctx):
    author = ctx.author
    print(f'Command "abc" has been Triggered by {author}')
    await ctx.send('a')
    await ctx.send('b')
    await ctx.send('c')
    await ctx.send('wait...')
    await asyncio.sleep(1)
    await ctx.send(f'...you should know your abc\'s already {author.name}')

@client.command()
async def abcFull(ctx):
    author = ctx.author
    print(f'Command "abcFull" has been Triggered by {author}')
    var='a'
    alphabets=[]
    # starting from the ASCII value of 'a' and keep increasing the
    # value by i.
    alphabets=[(chr(ord(var)+i)) for i in range(26)]
    await ctx.send(str(alphabets))

@client.command()
async def AFairCode(ctx):
    author = ctx.author
    print(f'Command "AFairCode" has been Triggered by {author}')
    await ctx.send('**AFairCode** - For More Information, go to <https://g.co/AFairCode/>')

@client.command()
async def activity(ctx):
    author = ctx.author
    print(f'Command "activity" has been Triggered by {author}')
    await ctx.send('Please wait while bot gets the following information...')
    await asyncio.sleep(3)
    await ctx.send(f'**{author.name}** - Are you blind? Can you not read what it says under the bot?')

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    author = ctx.author
    print(f'Command "kick" has been Triggered by {author}')
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    author = ctx.author
    print(f'Command "ban" has been Triggered by {author}')
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')

@client.command()
async def unban(ctx, *, member):
    author = ctx.author
    print(f'Command "unban" has been Triggered by {author}')
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run('TOKEN')
