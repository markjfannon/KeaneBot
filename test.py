import selector
import random

global lyrics, name 
lyrics, name=selector.select_lyric()
formatted=("'"+lyrics+"'")
print(formatted)


while True:
    guess=input(">>>")
    if guess == name:
        print("correct")
    else:
        print("incorrect")
        print(name)
