# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:11:37 2021

@author: Kumar
"""

import random
kc=0
ck=0
mb=[]
ma=[]
k=[]
m=[]
print("enter player1 name")
p1=input()
print("enter player2 name")
p2=input()
print(p1," Ticket")
while(len(k)!=15):
    a=random.randint(1,99)
    if a not in k:
            k.append(a)
for i in range(0,3):
    t=[]
    for j in range(0,5):
        t.append(k[ck])
        ck=ck+1
    ma.append(t)
for i in range(0,3):
    print(ma[i])
    
print(p2,"Ticket")
while(len(m)!=15):
    a=random.randint(1,99)
    if a not in m:
        m.append(a)
for i in range(0,3):
    t=[]
    for j in range(0,5):
        t.append(m[kc])
        kc=kc+1
    mb.append(t)
for i in range(0,3):
    print(mb[i])
b=c=z=0
x=y=14
f=1
w=[]
while(f):  
    a=random.randint(1,99)
    if a not in w:
          w.append(a)
          print("Random number is:")
          print(a)
          for i in range(0,3):
              for j in range(0,5):
                  
                  if(a==ma[i][j]):
                    ma[i][j]=0
                    print(p1)
                    print("Your item matched")
                    print("You just need ",x," numbers to match in your to ticket to win")
                    for i in range(0,3):
                        print(ma[i])
                    print("Do you like to continue")
                    print("press 1 to continue")
                    print("press 0 to exit")
                    b=b+1
                    x=x-1
                    if(x==-1):
                        print(p1,"You won the Game")
                    s=int(input( ))
                    if(s==0):
                        print("sucessfully quited the game")
                        f=0
                    if(s==1):
                        continue
                  if(a==mb[i][j]):
                    mb[i][j]=0
                    print(p2)
                    print("Your item matched")
                    print("You just need ",y,"numbers to match in your to ticket to win")
                    for i in range(0,3):
                        print(mb[i])
                    print("Do you like continue")
                    print("Press 1 to continue")
                    print("Press 0 to exit")
                    c=c+1
                    y=y-1
                    if(y==-1):
                        print(p2,"You won the Game")
                    s=int(input( ))
                    if(s==0):
                        print("sucessfully quited the game")
                        f=0
                    if(s==1):
                        continue
                  if(a!=k[i] and a!=m[i]):
                    z=z+1
                  if(z==15):
                    print("Doesn't match in any player's ticket")
                    print("Do you like continue")
                    print("Press 1 to continue")
                    print("Press 0 to exit")
                    z=0
                    s=int(input( ))
                    if(s==0):
                        print("sucessfully quitted the game")
                        f=0
                    if(s==1):
                        pass
                  if(b==15):
                    print(p1," won the game")
                    f=0
                  if(c==15):
                    print(p2," won the game")
                    f=0