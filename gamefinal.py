import random
import string
t=True
Answer=0
while t==True: #Tic Tac Toe rules to be accepted
   

    print("RULES FOR TIC-TAC-TOE")

    print("1. The game is played on a grid that's 3 squares by 3 squares.")

    print("2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.")

    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")

    print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

    Answer=input("Do you agree to the Terms And Conditions {Y/N}")
    if Answer=="Y" or Answer=="y":
        t=False
    else:
        print()
        print()
        print("----------------------------------------------")
        print("You must agree to the terms to play the game..")
        print("----------------------------------------------")
        print()
        t=True

choice=input("Do you want to play with computer?(Y/N)") #CHOICE TO PLAY WITH COMPUTER
if choice=="N" or choice=="n":
    



    player1=input("Enter Player one name: ") #ENTER PLAYER 1 NAME
    player2=input("Enter Player two name: ") #ENTER PLAYER 2 NAME
    name=[]  #Get name player 1 in list
    m=0
#Get list of name
    for j in player1:
        name.insert(m,j)
        m+=1
    n=0
#Compare name by letters
    for i in player2:
        if name[n]!=i:
            dice2=i.upper()            #Assigning letter
            dice1=name[n].upper()
            break
        n+=1
        if n==2:
            dice1=random.choice(string.ascii_letters)
            dice2=chr(ord(dice1)+1)
            break

    dice1=dice1.upper()
    dice2=dice2.upper()


    print("Player one name is ",dice1)  
    print("Player two name is",dice2)   

    board=[['0' ,'0' ,'0' ],    #NESTED LIST
           ['0' ,'0' ,'0' ],    
           ['0' ,'0' ,'0' ]]
    print('  R1 R2 R3')     #BOARD PRINT
    print('C1  |  |  ')
    print('  - +- +- ')
    print('C2  |  |  ')
    print('  - +- +- ')
    print('C3  |  |  ')
    print('****')


    h=True
    d=True          #DECLARING VARIABLES FOR "WHILE" LOOP
    while h==True: 
        a=True
        i=True
        while i==True:
    
            j=True
            k=True
        
            while j==True:
                row=input("Player one please enter a row number")  #ENTER ROW NUMBER
                
                if row.isdigit():           #IF ROW NUMBER IF BETWEEN 1-3 LOOP ENDS
                    row1=int(row)    
                    if row1>=4 or row1<=0:
                        j=True
                        print("Enter number between 1-3")
                    elif row1<=3 or row1>=0:
                        j=False
                elif row.isalpha():
                    j=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
                
            while k==True:   
                column=input("Player one please enter a column number") # IF ROW NUMBER IF BETWEEN 1-3 LOOP ENDS
                if column.isdigit():
                    column1=int(column)
                    if column1>=4 or column1<=0:
                        k=True
                        print("Enter number between 1-3")
                    elif column1>0 or column1<=3:
                        k=False
                elif column.isalpha():
                    k=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
                
                    
            if board[column1-1][row1-1]=='0':    #POSITION LOGIC
                board[column1-1][row1-1]=dice1
                for item in board:         #PRINT BOARD
                    for x in item:
                        print(x,end="  ")
                    print()
                i=False
            else:
                print("Already used position")

        if (board[0][0]==dice1 and board[1][1]==dice1 and board[2][2]==dice1) or (board[0][0]==dice1 and board[1][0]==dice1 and board[2][0]==dice1) or (board[0][1]==dice1 and board[1][1]==dice1 and board[2][1]==dice1) or (board[0][2]==dice1 and board[1][2]==dice1 and board[2][2]==dice1) or (board[0][0]==dice1 and board[0][1]==dice1 and board[0][2]==dice1) or(board[1][1]==dice1 and board[1][0]==dice1 and board[1][2]==dice1) or(board[2][0]==dice1 and board[2][1]==dice1 and board[2][2]==dice1):
            print("Player one wins")                        #WINNING LOGIC
            print("Player two better luck next time ")
            h=False
            a=False
        elif (board[0].count("0")==0) and (board[1].count("0")==0) and (board[2].count("0")==0):
            print("------------------")             #DRAW  LOGIC
            print("Draw")
            print("------------------")
            h=False
            a=False
            d=False
    
        while a==True:          #SECOND PLAYER 
    
            l=True
            m=True
        
            while l==True:
                row=input("Player Two please enter a row number")
                
                if row.isdigit():        #ROW BETWEEN 1-3
                    row1=int(row)    
                    if row1>=4 or row1<=0:
                        l=True
                        print("Enter number between 1-3")
                    elif row1<=3 or row1>0:
                        l=False
                elif row.isalpha():
                    l=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
            while m==True:
                column=input("Player Two please enter a column number")
                if column.isdigit():
                    column1=int(column)
                    if column1>=4 or column1<=0:
                        m=True
                        print("Enter number between 1-3")
                    elif column1<=3 or column1>0:
                        
                        m=False
                elif column.isalpha():
                    m=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
                    
            if board[column1-1][row1-1]=='0':
                board[column1-1][row1-1]=dice2         #POSITION LOGIC
                for item in board:
                    for x in item:
                        print(x,end="  ")
                    print()
                a=False
            else:
                print("Already used position")
    
        if (board[0][0]==dice2 and board[1][1]==dice2 and board[2][2]==dice2) or (board[0][0]==dice2 and board[1][0]==dice2 and board[2][0]==dice2) or (board[0][1]==dice2 and board[1][1]==dice2 and board[2][1]==dice2) or (board[0][2]==dice2 and board[1][2]==dice2 and board[2][2]==dice2) or (board[0][0]==dice2 and board[0][1]==dice2 and board[0][2]==dice2) or(board[1][1]==dice2 and board[1][0]==dice2 and board[1][2]==dice2) or(board[2][0]==dice2 and board[2][1]==dice2 and board[2][2]==dice2):
            print("Player two wins")
            print("Player one better luck next time ")
            h=False         # VARIABLES DECLARED FALSE
            h=False
            a=False
            i=False
        if d==True:
            if (board[0].count("0")==0) and (board[1].count("0")==0) and (board[2].count("0")==0):
                print("------------------")                                 # DRAW LOGIC
                print("Draw")
                print("------------------")
                h=False
            
else:  #COMPUTER PLAYER
    player1=input("Enter Player one name: ")
    player2="Computer"
    name=[]  #get name player 1 in list
    m=0
#get list of name
    for j in player1:
        name.insert(m,j)
        m+=1
    n=0
#compare name by letters
    for i in player2:
        if name[n]!=i:
            dice2=i.upper()            #assigning letter
            dice1=name[n].upper()
            break
        n+=1
        if n==2:
            dice1=random.choice(string.ascii_letters)
            dice2=chr(ord(dice1)+1)
            break

    dice1=dice1.upper()
    dice2=dice2.upper()


    print("Player one name is ",dice1)
    print("Player two name is",dice2)

    board=[['0' ,'0' ,'0' ],
           ['0' ,'0' ,'0' ],
           ['0' ,'0' ,'0' ]]
    print('  R1 R2 R3')     #BOARD PRINT
    print('C1  |  |  ')
    print('  - +- +- ')
    print('C2  |  |  ')
    print('  - +- +- ')
    print('C3  |  |  ')
    print('****')
    h=True
    d=True
    while h==True:
        a=True
        i=True
        while i==True:
    
            j=True
            k=True
        
            while j==True:
                row=input("Player One please enter a row number")
                
                if row.isdigit():
                    row1=int(row)    
                    if row1>=4 or row1<=0:
                        j=True
                        print("Enter number between 1-3")
                    elif row1<=3 or row1>0:
                        j=False
                elif row.isalpha():
                    j=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
            while k==True:
                column=input("Player one please enter a column number")
                if column.isdigit():
                    column1=int(column)
                    if column1>=4 or column1<=0:
                        k=True
                        print("Enter number between 1-3")
                    elif column1>0 or column1<=3:
                        k=False
                elif column.isalpha():
                    k=True
                    print("Enter number between 1-3")
                else:
                    j=True
                    print("Enter number between 1-3")
            if board[column1-1][row1-1]=='0':
                board[column1-1][row1-1]=dice1
                for item in board:
                    for x in item:
                        print(x,end="  ")
                    print()
                print("-----------------")
                i=False
            else:
                print("Already used position")

        if (board[0][0]==dice1 and board[1][1]==dice1 and board[2][2]==dice1) or (board[0][0]==dice1 and board[1][0]==dice1 and board[2][0]==dice1) or (board[0][1]==dice1 and board[1][1]==dice1 and board[2][1]==dice1) or (board[0][2]==dice1 and board[1][2]==dice1 and board[2][2]==dice1) or (board[0][0]==dice1 and board[0][1]==dice1 and board[0][2]==dice1) or(board[1][1]==dice1 and board[1][0]==dice1 and board[1][2]==dice1) or(board[2][0]==dice1 and board[2][1]==dice1 and board[2][2]==dice1):
            print("Player one wins")
            print("Player two better luck next time ")
            h=False
            a=False
        elif (board[0].count("0")==0) and (board[1].count("0")==0) and (board[2].count("0")==0):
            print("Draw")
            h=False
            d=False
        while a==True:
    
            l=True
            m=True
        
            while l==True:
                row=random.randint(1,3)   #USING RANDOM FUNCTION TO GET INTEGERS FROM 1-3
                l=False
            while m==True:
                column=random.randint(1,3)  #USING RANDOM FUNCTION TO GET INTEGERS FROM 1-3
                m=False
            if board[column-1][row-1]=='0':
                board[column-1][row-1]=dice2
                for item in board:
                    for x in item:
                        print(x,end="  ")
                    print()
                a=False
            
    
        if (board[0][0]==dice2 and board[1][1]==dice2 and board[2][2]==dice2) or (board[0][0]==dice2 and board[1][0]==dice2 and board[2][0]==dice2) or (board[0][1]==dice2 and board[1][1]==dice2 and board[2][1]==dice2) or (board[0][2]==dice2 and board[1][2]==dice2 and board[2][2]==dice2) or (board[0][0]==dice2 and board[0][1]==dice2 and board[0][2]==dice2) or(board[1][1]==dice2 and board[1][0]==dice2 and board[1][2]==dice2) or(board[2][0]==dice2 and board[2][1]==dice2 and board[2][2]==dice2):
            print("Player two wins")
            print("Player one better luck next time ")
            h=False
            a=False
            i=False
        elif d is True:
            if (board[0].count("0")==0) and (board[1].count("0")==0) and (board[2].count("0")==0):
                print("------------------")
                print("Draw")
                print("------------------")
                h=False
print("--------------------")
print("Game ended")
print("---------------------------------------")
print("Thanks for playing the game")
print("Credits: ARCHIT JAIN ,SIDDHARTH GAUR")
print("Stay tuned for more games")
print("---------------------------------------")
u=True
while u==True:
    feedback=int(input('Please rate the game between 1-10'))
    if feedback<=0 or feedback>10:
        print('Please Enter value between 1-10')
    else:
        break
        
