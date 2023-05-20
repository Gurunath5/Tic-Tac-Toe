#Python Tic Tac Toe Game 1.3 "Gurunath"
import numpy as np
import random
from time import sleep
a=np.array([[["","",""],
        ["","",""],
        ["","",""]]])
rem=[1,2,3,4,5,6,7,8,9]
player1="player X"
player2="player O"
c=0
def rowwin(a):
  for i in range(3):
    tem=[j for j in a[0][i] if j!=""]
    if len(tem)==3 and len(set(tem))==1:
      if tem[0]==p1:
        print(a)
        print("Congratulations "+player1+" You won the game")
        return True
      elif tem[0]==p2:
        print(a)
        print("Congratulations "+player2+" You won the game")
        return True
def clmwin(a):
  for i in range(3):
    tem=[]
    for j in range(3):
      add=a[0][j][i]
      if add!="":
        tem.append(a[0][j][i])
      if len(tem)==3 and len(set(tem))==1:
        if tem[0]==p1:
          print(a)
          print("Congratulations "+player1+" You won the game")
          return True
        elif tem[0]==p2:
          print(a)
          print("Congratulations "+player2+" You won the game")
          return True
def diagwin(a):
  for i in range(3):
    tmp=[a[0][i][i] for i in range(3) if a[0][i][i]!=""]
    if len(tmp)==3 and len(set(tmp))==1:
      if tmp[0]==p1:
        print(a)
        print("Congratulations "+player1+" You won the game")
        return True
      elif tmp[0]==p2:
        print(a)
        print("Congratulations "+player2+" You won the game")
        return True
  for j in range(3):
    tmp=[a[0][j][-j-1] for j in range(3) if a[0][j][-j-1]!=""]
    if len(tmp)==3 and len(set(tmp))==1:
      if tmp[0]==p1:
        print(a)
        print("Congratulations "+player1+" You won the game")
        return True
      elif tmp[0]==p2:
        print(a)
        print("Congratulations "+player2+" You won the game")
        return True
print(player1+" symbol is: X")
print(player2+" symbol is: O")
p1="X"
p2="O"
while c<10:
  sleep(2)
  if c==9:
    print(a)
    print("Game Draw")
    break
  print(a)
  if c%2==0:
    print(player1+" Turn")
    sel=random.choice(rem)
    rem.pop(rem.index(sel))
  else:
    print(player2+" Turn")
    sel=random.choice(rem)
    rem.pop(rem.index(sel))
  if sel==1:
    if c%2==0:
        a[0][0][0]=p1
    else:
        a[0][0][0]=p2
  elif sel==2:
    if c%2==0:
        a[0][0][1]=p1
    else:
        a[0][0][1]=p2
  elif sel==3:
    if c%2==0:
        a[0][0][2]=p1
    else:
        a[0][0][2]=p2
  elif sel==4:
    if c%2==0:
      a[0][1][0]=p1
    else:
      a[0][1][0]=p2
  elif sel==5:
    if c%2==0:
      a[0][1][1]=p1
    else:
      a[0][1][1]=p2
  elif sel==6:
    if c%2==0:
      a[0][1][2]=p1
    else:
      a[0][1][2]=p2
  elif sel==7:
    if c%2==0:
      a[0][2][0]=p1
    else:
      a[0][2][0]=p2
  elif sel==8:
    if c%2==0:
      a[0][2][1]=p1
    else:
      a[0][2][1]=p2
  elif sel==9:
    if c%2==0:
      a[0][2][2]=p1
    else:
      a[0][2][2]=p2
  else:
    break
  c=c+1
  if rowwin(a):
    break
  if clmwin(a):
    break
  if diagwin(a):
    break