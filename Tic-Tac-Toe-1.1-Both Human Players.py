#Python Tic Tac Toe Game 1.1  "Gurunath"
#Both Human Players
import numpy as np
print("press -1 for exit the game")
print("please choose the spot from 1-9 only\n")
print("\n")
a=np.array([[["","",""],
        ["","",""],
        ["","",""]]])
player1=input("Please enter Player1 name")
player2=input("Please enter Player2 name")
c=0
em="Already selected please select other square"
print("Please select Symbol: X , O ")
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
symb=input()
while symb!="x" and symb!="o":
  print("Please enter the valid symbol : X or O")
  symb=input()
if symb=="x":
  print(player1+" symbol is: X")
  print(player2+" symbol is: O")
  p1="X"
  p2="O"
else:
  print(player1+" symbol is: O")
  print(player2+" symbol is: X")
  p1="O"
  p2="X"
while c<10:
  if c==9:
    print(a)
    print("Game Draw")
    break
  print(a)
  if c%2==0:
        sel=10
        while int(sel)<1 or int(sel)>9:
            print(player1+" turn")
            sel=input()
            try:
                if int(sel):
                    sel=int(sel)
                    if sel==-1:
                        print("Successfully Exit")
                        break
                if int(sel)>9 or int(sel)<1:
                    print("please enter the number from 1-9 only")
            except:
                print("Please enter the numbers from 1-9 only")
                sel=10
  else:
    sel=10
    while int(sel)<1 or int(sel)>9:
        print(player2+" "+"turn")
        sel=input()
        try:
            if int(sel):
                sel=int(sel)
                if sel==-1:
                    print("Successfully Exit")
                    break
            if int(sel)>9 or int(sel)<1:
                print("please enter numbers from 1-9 only")
        except:
            print("Please enter numbers from 1-9 only")
            sel=10
  if sel==1:
    if c%2==0:
      if a[0][0][0]=="":
          a[0][0][0]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][0][0]=="":
        a[0][0][0]=p2
      else:
        print(em)
        c=c-1
  elif sel==2:
    if c%2==0:
      if a[0][0][1]=="":
        a[0][0][1]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][0][1]=="":
        a[0][0][1]=p2
      else:
        print(em)
        c=c-1
  elif sel==3:
    if c%2==0:
      if a[0][0][2]=="":
          a[0][0][2]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][0][2]=="":
        a[0][0][2]=p2
      else:
        print(em)
        c=c-1
  elif sel==4:
    if c%2==0:
      if a[0][1][0]=="":
        a[0][1][0]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][1][0]=="":
        a[0][1][0]=p2
      else:
        print(em)
        c=c-1
  elif sel==5:
    if c%2==0:
      if a[0][1][1]=="":
        a[0][1][1]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][1][1]=="":
        a[0][1][1]=p2
      else:
        print(em)
        c=c-1
  elif sel==6:
    if c%2==0:
      if a[0][1][2]=="":
        a[0][1][2]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][1][2]=="":
        a[0][1][2]=p2
      else:
        print(em)
        c=c-1
  elif sel==7:
    if c%2==0:
      if a[0][2][0]=="":
        a[0][2][0]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][2][0]=="":
        a[0][2][0]=p2
      else:
        print(em)
        c=c-1
  elif sel==8:
    if c%2==0:
      if a[0][2][1]=="":
        a[0][2][1]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][2][1]=="":
        a[0][2][1]=p2
      else:
        print(em)
        c=c-1
  elif sel==9:
    if c%2==0:
      if a[0][2][2]=="":
        a[0][2][2]=p1
      else:
        print(em)
        c=c-1
    else:
      if a[0][2][2]=="":
        a[0][2][2]=p2
      else:
        print(em)
        c=c-1
  else:
    break
  c=c+1
  if rowwin(a):
    break
  if clmwin(a):
    break
  if diagwin(a):
    break