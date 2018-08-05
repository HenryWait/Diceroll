import random

MIN = 1 #set lowest vlaue of the dice roll
MAX = 6 #set highest vlaue of the dice roll
DICE = 1 #set how many dice are rolled

ROLLAGAIN = "y" #continue playing if starting with y

while ROLLAGAIN.startswith('y'):
            #ask the user to input the highest value of the dice
            MAX = int(input("How many sides on the di?"))
            #ask the user to set how many dice are rolled
            DICE = int(input("How many dice do you want to Roll?"))
            print ("Rolling the dice")
            print ("You rolled...")
            count = 0
            #while loop repeats roll for how many dice are set
            for x in range(DICE):
                    print (random.randint(MIN, MAX))
            #ask user if they want to roll again
            ROLLAGAIN = input("Roll again?").lower()
