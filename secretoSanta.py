#! python3

# secretoSanta.py - takes in a list of names, assigns them secre santa and emails
# them their assigned person

# 1. get the list
# 2. random shuffle
# 3.

import random, ezgmail, os

names = ["jon","jest","mich","erni"]
random.shuffle(names)

secretoSanta = {}

for i in range(len(names)):
    if i == len(names)-1:
        secretoSanta[names[i]] = names[0]
        break

    secretoSanta[names[i]] = names[i+1]

# print(secretoSanta)

# ezgmail.send('jesthinedisla@gmail.com', "Send Emails using Python", '''
#     So I figured out how to send emails using python. It's lit.''', cc="jondis26@gmail.com" )

#emailing the secretsantas

for k,v in secretoSanta.items():
    em = k + "@gmail.com"
    ezgmail.send(em,"Secreto Santa", "\nHello\n\nYour Secreto Santa is: "+v)

# v = "luse"
# em = "jondis26@gmail.com"
# ezgmail.send(em,"Secreto Santa", "\nHello\n\nYour Secreto Santa is: "+v)
