import random
import selector
import discord
from discord.ext import commands
from discord.ext import tasks

token="NzM5ODQ3OTk1MTUxMDg5NzE1.XygbIw.7bNYIDU6WmMU0cEC4YiVAHMMHvc"

client = commands.Bot(command_prefix = "+")
leaderboard = []

global guessed
guessed=False

@client.command()
async def generate(ctx):
     global lyrics, name 
     lyrics, name=selector.select_lyric()
     formatted=("'"+lyrics+"'")
     await ctx.send(formatted)
     global guessed
     guessed=False

@client.command()
async def score(ctx):
    leaderboard=[]
    found=False
    user = str(ctx.author)
    openleaderboard=open("leaderboard.txt")
    for item in openleaderboard:
        leaderboard.append(item)
    openleaderboard.close()
    for item in leaderboard:
        if user in item:
            index=leaderboard.index(item) 
            found=True

    if found==False:
        ctx.send("Error")
    else:
         
        score=leaderboard[index].split(":")
        await ctx.send("Your score is"+" "+score[1])
        print(leaderboard)


@client.command()
async def guess(ctx,*,arg):
    global guessed
    if guessed == True:
        await ctx.send("Sorry!, somebody else has guessed it before you!")
        return
    else:
        arg=arg.lower()
        if arg == name:
            await ctx.send("Correct!")
            guessed=True
            user=str(ctx.author)
            there=False
            for item in leaderboard:
                 if user in item:
                      there=True
                      index=leaderboard.index(item)
                      item=item.split(":")
                      score=int(item[1])
                      score=score+1
            if there == True:
                 newEntry=(user+":"+str(score)+"\n")
                 leaderboard[index]=newEntry
            else:
                 newEntry=(user+":"+"1"+"\n")
                 leaderboard.append(newEntry)
            rewriteleaderboard=open("leaderboard.txt", "w")
            for line in leaderboard:
                 rewriteleaderboard.write(line)
            rewriteleaderboard.close()
                 
        else:
            await ctx.send("incorrect")

   
#for troubleshooting
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.event
async def on_ready():
    print("Keane Bot Online!")

client.run(token)
