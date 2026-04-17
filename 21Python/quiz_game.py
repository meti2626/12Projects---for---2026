
print("welcome to this quiz")

playing = input("do you want to play?  ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets's play: ")    
score = 0

answer = input("what does GPU stands for?")

if answer.lower() == "q2":
     print("correct!")
     score += 1

else:
    print("incorrect!")


answer = input("what does RAM stands for?")

if answer.lower() == "mem":
     print("correct!")
     score += 2
else:
    print("incorrect!")

answer = input("what does psu stands for?")

if answer.lower() == "power":
     print("correct!")
     score += 1
else:
    print("incorrect!")

print ("you got "  + score + " questions correct!")    


