

import discord
from Regras import listaRegras
from discord.ext import commands


token = 'MTIwNjU4MjA3MTgyMTIwNTUwNg.G_yg4O.A878B3_VhZMCYHI1zu5Wh17EGxJ2eYc3ZH_3-w'
NameBot = "Copper"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


class MyClient(discord.Client):


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
   
    
    async def on_message(self, message):

        if message.content.lower() == "olá" or message.content.lower()== "oi":
            await message.channel.send(f'Seja bem vindo ao servidor! meu nome é {NameBot}, eu estou aqui para ajudar você!')
            await message.channel.send(f'Antes de começa digite:  !Regras')
        

        if  message.content.lower() == "!regras":
            await message.channel.send(f'Essas são as regras que devem ser seguindas : ')
            for regra in listaRegras:
              Seguinregras = regra["Regras"]
              await message.channel.send(Seguinregras)



client = MyClient()
client.run(token)