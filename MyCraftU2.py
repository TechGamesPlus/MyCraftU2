import discord
import discord as api
import random
import asyncio
from discord.ext import commands, tasks

client = commands.Bot(command_prefix=',')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='I ate the fking Wii'))
    print('Bot is Online')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Sorry, I had an error. I can give you the details...\nMyCraftU2 Error: Command Not Found')
        return

@client.command()
async def help(ctx):
    await ctx.send('Check Out The Official MyCraftU2 Page to see a list of commands\n<https://techgamesplus.webador.com/discord-links>')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def AmIGay(ctx):
    ra = random.choice(['Yes', 'No'])
    await ctx.send("Your Answer:")
    await asyncio.sleep(2)
    await ctx.send(ra)
    await ctx.send("This is not homophobic in any way")

@client.command()
async def AmIOk(ctx):
    ra = random.choice(['Yes', 'No', 'Yes, but *BEANS*', 'No, but *BEANS*'])
    await ctx.send("Your Answer:")
    await asyncio.sleep(2)
    await ctx.send(ra)

@client.command()
async def AmIKarlson(ctx):
    ra = random.choice(['Yes, you are KARLSON', 'No, you aren\'t KARLSON', 'You are just a bean'])
    await ctx.send('Your Answer:')
    await asyncio.sleep(2)
    await ctx.send(ra)

@client.command()
async def AmIBeans(ctx):
    ra = random.choice(['Just Beans', 'Special Beans', 'KARLSON BEANS', 'You\'re one of the beans from "Jack and the Beanstalk', 'NEIN! YOU\'RE A POTATO'])
    await ctx.send('Your Answer:')
    await asyncio.sleep(2)
    await ctx.send(ra)

@client.command()
async def crysis(ctx):
    ra = random.choice(['Markiplier', 'Jacksepticeye', 'PewDiePie', 'OSFirstTimer', 'Raid: Shadow Legends'])
    await ctx.send(f'{author.name}: Can it run CRYSIS?\nMyCraftU2: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: It should be able to run CRYSIS.\nMyCraftU2: Yet Again...\n:regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Can anything in this store run CRYSIS?\nMyCraftU2: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Well you arent much help are you?!\nMyCraftU2: :regional_indicator_n: :regional_indicator_o:')
    await asyncio.sleep(1)
    await ctx.send(f'{author.name}: Well I don\'t need your help, anyway!\nMyCraftU2: :regional_indicator_n: :regional_indicator_o:')
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
    if ctx.author.id == 657890901758312448:
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

    if ctx.author.id != 657890901758312448:
        await ctx.send('This Command Is Under Maintenance')
        await ctx.send('Sorry, I had an error. I can give you the details...\nMyCraftU2 Error: Under Maintenance')
        return

@client.command()
async def lick(ctx):
    author = ctx.author
    Nope = 'Eww! Stop That!'
    Yes = '***Nice***'
    ra = random.choice([Nope, Yes])

    await ctx.send(f'Bot: *Licks {author.mention}*\n{author.mention}: {ra}')

    if ra == Nope:
        await asyncio.sleep(1)
        await ctx.send('lmao')
        return

    elif ra == Yes:
        await asyncio.sleep(1)
        await ctx.send('*Oh God-*')
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
    await ctx.send('https://tenor.com/view/the-simpsons-homer-simpson-good-bye-bye-no-gif-5173989')
    
@client.command()
async def spam(ctx, number : int, *, spam : str):
    author = ctx.author
    for example in range(number):
        await ctx.send(spam)
        return

    if number > 1000:
        await ctx.send('Sorry, I had an error. I can give you the details...\nMyCraftU2 Error Code: Max Limit has been reached')
        return

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

    if amount > 500:
        await ctx.send('Sorry, I had an error. I can give you the details...\nMyCraftU2 Error: Max Limit has been reached')
        return

@client.command()
async def invite(ctx):
    await ctx.send('Here is the OAuth2 Link for MyCraftU2')
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=756726765719912501&permissions=8&scope=bot')

@client.command()
async def bigrigs(ctx):
    await ctx.send('Here\'s a Link to a Free Version of BigRigs: <https://bit.ly/3psDhNs>')
    await ctx.send(';)')
    await ctx.channel.purge(limit=1)

@client.command()
async def command(ctx):
    author = ctx.author
    await ctx.send(f"Congratulations {author.mention}! You Commanded the bot with its command to say command!")
    await asyncio.sleep(1)
    await ctx.send("Command")
    
@client.command()
async def dm(ctx, member : api.Member, *, text="placeholder"):
    if member.dm_channel == None:
        channel = await member.create_dm()
        await channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')
    elif member.dm_channel != None:
        await member.dm_channel.send(text)
        await ctx.send('`' + text + '`' + f' was sent to {member.display_name}')

@client.command()
async def dmd(ctx, member : api.Member, *, text="placeholder"):
    if member.dm_channel == None:
        channel = await member.create_dm()
        await ctx.channel.purge(limit=1)
        await channel.send(text)
        await ctx.author.send(':mailbox_with_mail:')
    elif member.dm_channel != None:
        await ctx.channel.purge(limit=1)
        await member.dm_channel.send(text)
        await ctx.author.send(':mailbox_with_mail:')
    
@client.command()
async def hello(ctx):
    author = ctx.author
    await ctx.send(f'Hello {author.name}')
    
@client.command()
async def avatar(ctx, member:api.Member=None):
    if member == None:
        member = ctx.author
    await ctx.send(member.avatar_url)
    
@client.command()
async def prefix(ctx):
    await ctx.send(f'The prefix is ,')

@client.command()
async def rank(ctx):
    await ctx.send('Your rank for the server is...')
    await asyncio.sleep(2)
    await ctx.send('You do know I\'m not MEE6, right?')

@client.command()
async def corn(ctx):
    author = ctx.author
    video = 'https://www.youtube.com/watch?v=j8qp3ITVqY0'
    photo = 'https://cdn.discordapp.com/attachments/744104860219211796/759318896502636544/corn.jpg'
    await ctx.send(ra)

@client.command()
async def abc(ctx):
    author = ctx.author
    await ctx.send('a')
    await ctx.send('b')
    await ctx.send('c')
    await ctx.send('wait...')
    await asyncio.sleep(1)
    await ctx.send(f'...you should know your abc\'s already {author.name}')

@client.command()
async def abcFull(ctx):
    var='a'
    alphabets=[]
    # starting from the ASCII value of 'a' and keep increasing the
    # value by i.
    alphabets=[(chr(ord(var)+i)) for i in range(26)]
    await ctx.send(str(alphabets))

@client.command()
async def activity(ctx):
    author = ctx.author
    await ctx.send('Please wait while bot gets the following information...')
    await asyncio.sleep(3)
    await ctx.send(f'**{author.name}** - Are you blind? Can you not read what it says under the bot?')

@client.command()
async def eMeme(ctx):
    await ctx.send('E')

@client.command()
async def something(ctx):
    ra = random.choice(['Gretta', 'John', 'Dave', 'Mr. Potato Head', 'Spider', 'Spud', 'Elkraps'])
    await ctx.author.send(f'Hi {ra}')
    await ctx.send(':mailbox_with_mail:')

@client.command()
async def swear(ctx):
    ra = random.choice(['fuck', 'shit', 'fuk', 'dick', 'd1ck' 'pussy', 'asshole', 'bitch', 'blowjob', 'cock', 'c0ck'])
    
    await ctx.send(ra)

@client.command()
async def face(ctx):
    ra = random.choice(['D:', ':(', ':|', ':)', ':D', ':/', '¯\_(ツ)_/¯', '):', '|:', '(:', 'D=', ')=', '|=', '=|', '=)', '=D'])
    
    await ctx.send(ra)

@client.command()
async def peepee(ctx):
    author = ctx.author
    ra = random.choice(['8D', '8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8=========D', '8==========D', 'ubX Size PP'])

    await ctx.author.send(ra)
    await ctx.send(':mailbox_with_mail:')
    await asyncio.sleep(15)
    await ctx.send(f'{author} got {ra}')
    return
    
@client.command()
async def memCount(ctx):
    a = ctx.guild.member_count
    b = discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

@client.command()
async def checkIn(ctx):
    ra = random.choice(['your mom', 'The dentist', 'The bus with that one guy on the bus', 'Discord', 'E Meme', 'E Game', 'The CODEC House in The Sims 2'])
    
    await ctx.send(f'You just checked into {ra}. Thank you for helping to keep WA safe.')

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Sorry, I had an error. I can give you the details...\nMyCraftU2 Error: Missing Required Arguments')


client.run('NzU2NzI2NzY1NzE5OTEyNTAx.X2WCuA.0FaPgo84o1G0K_fzXlr8vKXJV8Y')
