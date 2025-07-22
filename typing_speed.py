from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):  # fixed variable name from 'pratest' to 'partest'
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test = [
    "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
    "The anger of a good man lasts an instant; that of a meddler two hours; that of a base man a day and a night; and that of a great sinner until death.",
    "The anger of a good man lasts an instant; that of a meddler two hours; that of a base man a day and a night; and that of a great sinner until death.",
    "Communication is a skill that you can learn. It's like riding a bicycle or typing. If you're willing to work at it, you can rapidly improve the quality of every part of your life."
]

test1 = r.choice(test)

print("         ***********TYPING SPEED CALCULATOR***********")
print()
print(test1)
print()
time_1 = time()
testinput = input("Enter : ")
time_2 = time()

print("Speed: ", speed_time(time_1, time_2, testinput), "w/s")
print("Error : ", mistake(test1, testinput))

