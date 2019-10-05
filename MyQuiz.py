import time

score= 0

name = str(input("What's your name? "))
print("Welcome to the quiz,"+name)
time.sleep(2)

def scorePlus():
    global score
    score+=1
    print("Your Score: ",score)

def scoreMinus():
    global score
    score-=1
    print("Your Score: ",score)


def q1():
    global score
    print("\nQ1)Who is the CEO of Apple? ")
    time.sleep(3)
    print("a.Steve Jobs")
    time.sleep(0.5)
    print("b.Tim Cook")
    time.sleep(0.5)
    print("c.Eddie Cue\n")
    time.sleep(0.5)
    answer = str(input("What is your answer?: "))

    time.sleep(0.5)
    if answer == "b":
        print("\nWell Done! The answer is correct!")
        time.sleep(1)
        scorePlus()
    else:
        print("Sorry,This is the wrong answer")
        time.sleep(1)
        scoreMinus()

    time.sleep(1)
    q2()

def q2():
    global score
    print("\nQ2)Who is the CEO of Tesla? ")
    time.sleep(3)
    print("a.Elon Musk")
    time.sleep(0.5)
    print("b.Nicola Tesla")
    time.sleep(0.5)
    print("c.Zach Kikhorn\n")
    time.sleep(0.5)    
    answer = str(input("What is your answer: "))

    time.sleep(0.5)
    if answer == "a":
        print("\nWell Done! The answer is correct!")
        time.sleep(1)
        scorePlus()
    else:
        print("Sorry,This is the wrong answer")
        time.sleep(1)
        scoreMinus()

    time.sleep(1)
    q3()

def q3():
    global score
    print("\nQ3)Who is the CEO of Google? ")
    time.sleep(3)
    print("a.Sundar Pichai")
    time.sleep(0.5)
    print("b.Larry Page")
    time.sleep(0.5)
    print("c.Sergey Brin\n")
    time.sleep(0.5)
    answer = str(input("What is your answer: "))

    time.sleep(0.5)
    if answer == "a":
        print("\nWell Done! The answer is correct!")
        time.sleep(1)
        scorePlus()
    else:
        print("Sorry,This is the wrong answer")
        time.sleep(1)
        scoreMinus()

    time.sleep(1)
    q4()

def q4():
    global score
    print("\nQ4)Who is the CEO of Microsoft? ")
    time.sleep(3)
    print("a.Satya Nadela")
    time.sleep(0.5)
    print("b.Bill Gates")
    time.sleep(0.5)
    print("c.Paul Allen\n")
    time.sleep(0.5)
    answer = str(input("What is your answer: "))

    time.sleep(0.5)
    if answer == "a":
        print("\nWell Done! The answer is correct!")
        time.sleep(1)
        scorePlus()
    else:
        print("Sorry,This is the wrong answer")
        time.sleep(1)
        scoreMinus()

    time.sleep(1)
    q5()

def q5():
    global score
    print("\nQ5)Who is the CEO of Youtube? ")
    time.sleep(3)
    print("a.Susan Wojcicki")
    time.sleep(0.5)
    print("b.Chad Hurley")
    time.sleep(0.5)
    print("c.Steve Chen\n")
    time.sleep(0.5)
    answer = str(input("What is your answer: "))

    time.sleep(0.5)
    if answer == "a":
        print("\nWell Done! The answer is correct!")
        time.sleep(1)
        scorePlus()
    else:
        print("Sorry,This is the wrong answer")
        time.sleep(1)
        scoreMinus()

time.sleep(1)
q1()

