#! python3

# secretoSanta.py - takes in a list of names, assigns them secre santa and emails
# them their assigned person

import random, ezgmail, os

names = []
emails = {}
#TOD- How many people are in the secret santa
numofPeeps = int(input("How many people are in the Secret Santa?: "))

# TOO - what are the names of the poeple and what is there corresponding
# emails

#for loop
for i in range(numofPeeps):
    #ask what is person number i's name
    i = str(i+1)
    name = input("What is person #"+i+"'s name? ")

    #what is there email
    email = input("What's "+ name+"'s email? ")

    #add it to list
    names.append(name)
    #add to dictionairy

    emails[name] = email

print(emails)
random.shuffle(names)

secretoSanta = {}

for i in range(len(names)):
    if i == len(names)-1:
        secretoSanta[names[i]] = names[0]
        break
    
    secretoSanta[names[i]] = names[i+1]

print(secretoSanta)


for i in names:
    n= secretoSanta.get(i)
    ezgmail.send(emails.get(n),"Secreto Santa", "\nHello\n\nYour Secreto Santa is: "+i)


# # ezgmail.send('a@gmail.com', "Send Emails using Python", '''
# #     So I figured out how to send emails using python. It's lit.''', cc="jondis26@gmail.com" )

# #emailing the secretsantas

# for k,v in secretoSanta.items():
#     em = k + "@gmail.com"
#     ezgmail.send(em,"Secreto Santa", "\nHello\n\nYour Secreto Santa is: "+v)

# v = "luse"
# em = "jondis26@gmail.com"
# ezgmail.send(em,"Secreto Santa", "\nHello\n\nYour Secreto Santa is: "+v)
