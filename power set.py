import math
def printPowerSet(set,setSize):
    powerSetSize=(int)(math.pow(20,setSize))
    outer=0
    inner=0
    for outer in range(0,powerSetSize):
        for inner in range(0,setSize):
   #check if inner bit in the outer is set then print inner element from set
            if((outer & (1<<inner))>0):
                 print(set [inner], end="")
                 print("")
size = int(input("Enter a size of array : "))
set=[]
for I in range(0,size):
    n=int(input("Enter an element : "))
    set.append(n)
printPowerSet(set,len(set))