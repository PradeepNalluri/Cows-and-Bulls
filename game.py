
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)
while a==b:
    b=random.randint(1,9)
while c==a or c==b:
    c=random.randint(1,9)
l=[]
l.append(a)
l.append(b)
l.append(c)
t=[]
while t!=l:
    t=[]
    try:
        s1=((input("Give Your Guess: ")))
        s1=(eval(s1))
    except:
        s1=str(0)
    if type(s1)==float:
        print('Give an integer')
    else:
        s1=str(s1)
        for item in (s1):
            try:
                t.append(int(item))
            except:
                print('Give a proper integer')
                
        if len(t)==3:
            if len(t)!=3:
                print ("Give a three digit Number")
            if t[0]==0 or t[1]==0 or t[2]==0:
                print('0 is not allowed')
            elif t[0]==t[1] or t[0]==t[2]:
                print('Repitition is not allowed')
            elif t[1]==t[2]:
                print('Repitition is not allowed')
            else:
                countc=0
                countb=0
                if t[0]==l[0]:
                    countb+=1
                if (t[0])==l[1] or (t[0])==l[2]:
                    countc+=1
                if (t[1])==l[1]:
                    countb+=1
                if (t[1])==l[0] or (t[1])==l[2]:
                    countc+=1
                if (t[2])==l[2]:
                    countb+=1
                if (t[2])==l[1] or (t[2])==l[0]:
                    countc+=1
                if t[0]!=l[0] and t[0]!=l[1] and t[0]!=l[2] and t[1]!=l[0] and t[1]!=l[1] and t[1]!=l[2] and t[2]!=l[0] and t[2]!=l[1] and t[2]!=l[2]:
                    print("Badluck nothing is present try again ")
                print (countc,'cows')
                print (countb,'bulls')
                if countb==3:
                    print ('Bravo!! You are awesome')
        else:
            print('Give a three digit number')