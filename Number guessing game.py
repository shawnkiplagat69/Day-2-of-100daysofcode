import random as rd
from secrets import choice
choice_1=rd.randint(1,10)
choice_2=rd.randint(1,50)
choice_3=rd.randint(1,100)
def clue_1(choice):
    if choice %2==0:
        print("Try an even number")
    else:
        print("Try an odd number")
def clue_2(choice):
    if choice%5==0:
        print("Try a number that is a multiple of five")
    else:
        print("try a number that isn't a multiple of five")
def clue_3(choice):
    if choice>5:
        print("Try a number greater than 5")
    else:
        print("Try a number less than 6")
def clue_3i(choice):
    if choice>25:
        print("Try a number greater than 25")
    else:
        print("Try a number less than 26")
def clue_3ii(choice):
    if choice>50:
        print("Try a number greater than 50")
    else:
        print("Try a number less than 51")
def clue_4(choice):
    if choice%7==0:
        print("The number is a multiple of 7")
    else:
        print("The number is not a multiple of 7")
def clue_5(choice):
    if choice%10==0:
        print("Try a  multiple of 10")
    else:
        print("The number is not a multiple of 10")
def clue_6(choice):
    if choice>75:
        print("Try a number greater than 75")
    elif choice<25:
        print("Try a number less than 25")
    else:
        print("Try a number greater than 25 but less than 75")
def clue_7(choice):
    flag=False
    if choice>1:
        for i in range(2,choice):
            if choice%i==0:
                flag=True
                break
    if flag==False:
        print("Try looking for a prime number")
    else:
        print("Try looking for a non-prime number")
def clue_8(choice):
    if choice%5==0:
        print("Try a multiple of 5")
    else:
        print("Try a number that isn't a multiple of 5")
def clue_9(choice):
    if choice>7:
        print("Try a number greater than 7")
    elif choice<3:
        print("Try a number less than 3")
    else:
        print("Try a number greater than 3 but less than 7")
def clue_10(choice):
    if choice>38:
        print("Try a number greater than 38")
    elif choice<18:
        print("Try a number less than 18")
    else:
        print("Try a number greater than 18 but less than 38")
def mode_1():
    print("This is an easy mode for the numbers in the range of (1 to 10)")
    #choice=choice_1
    score=100
    num=int(input("How about you try guessing a number between 1 and 10 inclusive:"))
    if num!=choice_1:
        print("Thats not quite it. Try again")
        clue_1(choice_1)
        score-=10
    elif num==choice_1:
        print("Eureka! You guessed the number!")
        print("Your score:", score)
    num=int(input())
    if num!=choice_1:
        print("That isn't it either. Give it another go")
        clue_3(choice_1)
        score-=10
    elif num==choice_1:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_1:
        print("You still haven't gotten it right. You're almost there")
        clue_7(choice_1)
        score-=10
    elif num==choice_1:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_1:
        print("Not there yet. Here's another clue:")
        clue_9(choice_1)
        score-=10
    elif num==choice_1:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_1:
        print("You couldn't quite get it right. Better luck next time")
        print("The number is:", choice_1)
        print("Your score:", score)
    else:
        print("the number is:", choice_1)
        print("Your score:", score)
def mode_3():
    print("This is a hard mode for the numbers in the range of (1 to 100)")
    #choice=choice_1
    score=100
    num=int(input("How about you try guessing a number between 1 and 100 inclusive:"))
    if num!=choice_3:
        print("That's not the right number. Try again")
        clue_1(choice_3)
        score-=8
    elif num==choice:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_3:
        print("That's not it either. Give it another shot")
        clue_3ii(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_3:
        print("You still haven't gotten it right. Here's another clue")
        clue_4(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_3:
        print("Come on mahn, give it another try")
        clue_2(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_3:
        print("That is still not the right answer, try again?")
        clue_7(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice:
        print("You're getting closer. Don't give up now")
        clue_6(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_3:
        print("Oops! That is still ot the right number. You still have a chance to get it right though")
        clue_5(choice_3)
        score-=8
    elif num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num==choice_3:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    else:
        print("The number is:", choice_3)
        print("Your score:", score)
def mode_2():
    print("This is an intermediate mode for the numbers in the range of (1 to 50)")
    #choice=choice_1
    score=100
    num=int(input("How about you try guessing a number between 1 and 50 inclusive:"))
    if num!=choice_2:
        print("That is not the right number")
        clue_1(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_2:
        print("That is still not right")
        clue_3i(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_2:
        print("Oops! That is not quite it. Give it another go")
        clue_2(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_2:
        print("I'm afraid that is still not the right answer. Don't shy w\away though, just give it another shot")
        clue_7(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_2:
        print("Not yet there. Try again?")
        clue_5(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num!=choice_2:
        print("Sorry, that still isn't the number we're looking for")
        clue_10(choice_2)
        score-=10
    elif num==choice_2:
        print("Eureka! You guessed the number")
        print("Your score:", score)
    num=int(input())
    if num==choice_2:
        print("Eureka! You've guessed the right number")
        print("Your score:"), score
    else:
        print("The number is actually ", choice_2)
        print("Your score:", score)
def main():
    print("welcome to the number guessing game.")
    level=int(input("Please enter your selection as below:\n1. Easy\n2. Intermediate\n3. Hard\n"))
    if level==1:
        mode_1()
    elif level==2:
        mode_2()
    elif level==3:
        mode_3()
    else:
        print("Invalid selection.\n Please try that again")
    retry=input(("Would you like to restart the game? (y/n)\n"))
    if retry=="y":
        main()
    else:
        print("Thank you for playing")
main()


    
