import random
Cchoice=["Rock","Paper","Scissor"]
while (True):
    print ("Rock Paper Scissor's Game:")
    youwin,computerwin=0,0
    for i in range (1,6):
        print("Round",i,"start:")
        print ("please select any one option:")
        print ("1.Rock","2.Paper","3.Scissor",sep="\n")
        yourchoice=int(input())
        if (yourchoice==1):
            print ("You have choosen 'Rock'")
            yourchoice="Rock"
        elif(yourchoice==2):
            print ("You have choose 'Paper'")
            yourchoice="Paper"
        elif(yourchoice==3):
            print("You have choosen 'Scissor'")
            yourchoice="Scissor"
        else:
            print ("Invalid Choice")
            break
        
        computerchoice=random.choice(Cchoice)
        print("Computer selects:",computerchoice)
        if (yourchoice==computerchoice):
            print("This Round is Draw")
        elif (yourchoice=="Paper" and computerchoice=="Rock")or(yourchoice=="Rock" and computerchoice=="Scissor")or(yourchoice=="Scissor" and computerchoice=="Paper"):
            youwin+=1
            print("You win this Round")
        else:
            computerwin+=1
            print ("Computer win this Round")
    if (youwin>computerwin):
        print ("You won the Game")
        print ("Score is:","Your Score:",youwin,"computer Score:",computerwin,sep=" ")
    elif(computerwin>youwin):
        print ("Computer won the Game")
        print ("Score is:","Your Score:",youwin,"computer Score:",computerwin,sep=" ")
    else:
        print ("Match Draw")
        print ("Score is:","Your Score:",youwin,"computer Score:",computerwin,sep=" ")
    user_choice=input("want to continue the game?(Yes/Exit)")
    if user_choice=="YES" or user_choice=="Yes" or user_choice=="yes":
        continue
    else:
        break