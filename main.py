print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

# Q1.
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q2.
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q3.
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q4.
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q5.
answer = input("What does CD stand for? ")
if answer.lower() == "compact disc":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q6.
answer = input("What does DOS stand for? ")
if answer.lower() == "disk operating system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q7.
answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q8.
answer = input("What does HLL stand for? ")
if answer.lower() == "high level language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q9.
answer = input("What does LCD stand for? ")
if answer.lower() == "liquid crystal display":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q10.
answer = input("What does LAN stand for? ")
if answer.lower() == "local area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q11.
answer = input("What does LLL stand for? ")
if answer.lower() == "low level language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q12.
answer = input("What does MAN stand for? ")
if answer.lower() == "metropolitan area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q13.
answer = input("What does MPU stand for? ")
if answer.lower() == "microprocessor unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q14.
answer = input("What does PC stand for? ")
if answer.lower() == "personal computer":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q15.
answer = input("What does PDA stand for? ")
if answer.lower() == "personal digital assistant":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q16.
answer = input("What does PLC stand for? ")
if answer.lower() == "programmable logic controller":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q17.
answer = input("What does TB stand for? ")
if answer.lower() == "tera bytes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q18.
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q19.
answer = input("What does WAN stand for? ")
if answer.lower() == "wide area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Q20.
answer = input("What does ISP stand for? ")
if answer.lower() == "internet service provider":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/20) * 100) + "%.")


# note - currently there are only 20 questions in this quiz, but you can always add more questions to make things more interesting