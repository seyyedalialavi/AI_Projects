import math
import  random

#compute conflict for per queen
def conflict(currentstate):
    conf=0
    for i in range(0,8):
        for j in range(i+1,8):
            if currentstate[i]==currentstate[j] or abs(i-j)==abs(currentstate[i]-currentstate[j]):
                conf+=1
    return conf

#chose randomly between colum and raw
def muted(currentstate):
    currentstate[random.randint(0, len(currentstate) - 1)] = random.randint(0, 7)
    return currentstate

#use simulated annealing
def simulated(bored):
    global temperature
    temperature = 20
    global counter
    counter=0

    while temperature!=0:
        counter+=1
        temperature -= 1
        currentstate = bored
        currentconf = conflict(currentstate)
        if temperature == 0 or currentconf==0 :
            return lastbord(currentstate,currentconf,counter)

        nextstate = muted(currentstate)
        nextconf = conflict(nextstate)
        delta_e = currentconf - nextconf

        #try to decide go to nextstate or chose onother state
        if delta_e > 0:
            currentstate = nextstate
        else:
            flag=probable(delta_e,temperature)

            if flag==1:
                currentstate = nextstate
            else:
               return simulated(currentstate)

#computing the probablity for successor
def probable(delta_e,temp):
    p=((math.e)**(delta_e/temp))*100
    numrandom=random.randint(0, 100)
    print(p)

    if numrandom<=p and numrandom>=0:
        return 1
    else:
        return 0

#printing the answer
def lastbord(board,h,numtry):
    print("bestresult: ",board,"     ","h = ",h,"    ","number of try :",numtry )

#getting board from user
n=8
position=[]
flag=1
print("the inputs value must be between 0 and 7")
for i in range (0,n):

    while True:
        temp = int(input())
        if temp>=0 and temp<8 :
            position.append(temp)
            break
        else:
            print("the inputs value must be between 0 and 7 please try again")
print("firstbord :",position,"      ","h = ",conflict(position) )
simulated(position)