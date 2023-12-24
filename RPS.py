import random
def who_win(computer,user):
    if(computer==user):
        return 0
    elif(computer=="Rock" and user=="Paper"):
        return 2
        
    elif(computer=="Rock" and user=="Scissor"):
        return 1
        
    elif(computer=="Paper" and user=="Rock"):
        return 1
        
    elif(computer=="Paper" and user=="Scissor"):
        return 2
        
    elif(computer=="Scissor" and user=="Rock"):
        return 2
        
    elif(computer=="Scissor" and user=="Paper"):
        return 1
    else:
        return -1        
        
#    Taking Input From User....

print('1) Rock \n2) Paper\n3) Scissor')
user="0"
while(user not in ["1","2","3"] ):
    user=input("Enter Choice :- ")
    if (user=="1"):
        user="Rock"
        break
    elif(user=='2'):
        user="Paper"
        break
    elif(user=='3'):
        user="Scissor"
        break
    else:
        print("Wrong Choice, Choose Again.")
        
        
        
options=["Rock","Paper","Scissor"]
computer=options[random.randint(0,2)]

print("GAME:  Computer Choice : ",computer," & Your Choice : ",user)
score=who_win(computer,user)
if(score==1):
    print("Computer Wins")
elif(score==2):
    print("You Win")
elif(score==0):
    print("Match Draw")     
        
 
