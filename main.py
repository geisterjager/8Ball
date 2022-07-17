#Import the random number generator
import random

#Greet the user
print("Welcome to the Magic 8-Ball!")

#Get the user's name and question
print("What is your name?")
name = input("My name is:  ")
print("What is your question?")
question = input("My question is:  ")

#Init Answer Variable
answer = ""

#Generating Random Integer
random_number = random.randint(1,9)

#Assigning Answers to Random Integer Result
if random_number == 1:
    answer = "Yes, Definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error."

#Clear Screen Before Answer Reveal
print("Consulting the Oracle...\n"*20)

#Printing the Answer
print(name, "You asked: ", question,)
print("Your Answer is:  ", answer)
