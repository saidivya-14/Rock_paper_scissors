import random

computer = random.choice([-1,0,1])
mystr = input("enter your choice: ")
myDici = {"r":1,"p":-1,"s":0}
reverseDici = {1:"rock",-1:"paper",0:"siccors"}
you = myDici[mystr]

print(f"you chose {reverseDici[you]}\ncomputer chose {reverseDici[computer]}")

if(computer == you):
    print("its a draw")

else:
    if (computer-you)==-1 or (computer-you)==2:
        print("you win")
    else:
        print("you lose")

