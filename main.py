import datetime
import requests
import discord
from discord.ext import commands, tasks

bot = commands.Bot('*')

# Avisar no termina q ele esta rodando
@bot.event
async def on_ready():
    print(f'O bot {bot.user} esta Rodando no Servidores')
    current_time.start()
    

@bot.event
async def on_message(message):    
    if message.author == bot.user:
        return

    if "Mucalol" in message.content:
        await message.channel.send(
            f"Eu e minha casa servimos ao MACACO, {message.author.name} entre no link https://www.nimo.tv/Smurfdomuca e venha servir ao MACACO"
        )
    await bot.process_commands(message)


# *oi
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    
    response = 'Olá, ' + name
    
    await ctx.send(response)
    

@bot.command()
async def binance(ctx, coin, base):
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")      
        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"O valor do par {coin}/{base} é {price}")
        else:
            await ctx.send(f"O valor do par {coin}/{base} é inválido")
    except Exception as error:
        await ctx.send("Ops... Deu algum erro!")
        print(error)
        
        
@bot.command(name="segredo")
async def secret(ctx):
    try:
        await ctx.author.send("https://www.youtube.com/watch?v=sLtSVa_5sbA entra ai agr arrombado")
    except discord.errors.Forbidden:
        await ctx.send("Não posso te contar o segredo habilite receber mensagem de qualquer pessoa do servidor (Opções > Privacidade)")

@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    expression = "".join(expression)
    response = eval(expression)
    
    await ctx.send("A resposta é: "+ str(response))
    
    
@bot.command(name="foto")
async def get_random_image(ctx):
    url_image = "https://picsum.photos/1920/1080"
    
    embed = discord.Embed(
        title = "Resultado da pesquisa",
        description = "a busca e full randon",
        color = 0x0000ff
    )

    embed.set.author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set.footer(text=bot.user.name , icon_url=bot.user.avatar_url)
    embed.set.image(url=url_image)
    embed.add_field(name=API, value="https://picsum.photos/1920/1080")
    
    await ctx.send(embed=embed)

            

@tasks.loop(minutes=1)
async def current_time():
    now = datetime.datetime.now()
    
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    
    channel = bot.get_channel(878339004485992540)
        
    await channel.send("Data Atual: " + now)




# Run 
bot.run('TOKEN')
