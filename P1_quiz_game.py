print("Welcome to my game")

playing = input("do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Play!")
score = 0

answer = input("What does CPU stand for you? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stand for you? ")
if answer.lower() == "graphics processing":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supplyyes":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
