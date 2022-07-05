# from importlib import import_module
# from random import Random


# with open("u.txt",'w') as g:
#     g.write("hi i wrote this,Sushant Manjunath Naik")
# with open("u.txt",'r') as h:
#     j = h.read()
#     print(j)
#     breakpoint
from random import random 
def score(s,randNo):
    if s==randNo:
        return 'This game is tied'
    elif randNo==1:
        if s==2:
            return print("you won") 
        elif s==3:
            return print("you lose")
    elif randNo==2:
        if s==1:
            return print("you won" )
        elif s==3:
            return print("you lose")
    elif randNo==3:
        if s==2:
            return print("you won" )
        elif s==1:
            return print("you lose")
s=input("your choise stone(1),paper(2),scissor(3)?")
randNo = random.randint(1, 3)
if randNo == 1:
        v = "stone"    
elif randNo == 2:
        v = "paper"
elif randNo == 3:
        v = "scissor"

print(v)
z = score( s,randNo)
print(z)
