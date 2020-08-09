import random

def select_lyric():
    songlist=[]

    opensongs=open("songlist.txt")
    for item in opensongs:
        songlist.append(item)
    opensongs.close()

    selection=random.choice(songlist)
    split=selection.split("- ")

    lyrics=split[0]
    name=split[1]
    name=name[:-1]

    return(lyrics, name)
