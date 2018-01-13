#IMPORTANT NOTE: the ROW each piece is displayed in is INVERTED horizontally with respect to the row it's stored in

class piece:
    #General initiation procedure for all pieces
    def __init__(self,column,row,color,Type):
        #Input color and location
        self.column=column
        self.row=row
        self.color=color
        #Display piece on screen
        screen.blit(images[color][Type],(column*96,(7-row)*96))


class pawn(piece):
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"pawn")

    def move(self,new_column,new_row):
        #For white pawns       
        if self.color=="white":           
            #Check if it's a regular move
            if new_column==self.column and (new_row==self.row+1 or new_row==3 and self.row==1) and board[new_column][new_row]=="empty":
                #Handle a potential promotion
                if new_row==7:
                    promote_prompt(new_column,self.column,"white")
                #Otherwise, make an identical piece at the target square
                else:
                    erase(new_column,new_row)
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)
                
            #Check if it's a capture (pawns capture differently from moving)
            elif abs(new_column-self.column)==1 and new_row==self.row+1 and board[new_column][new_row]!="empty" and board[new_column][new_row].color!=self.color:
                #Handle a potential promotion
                if new_row==7:
                    promote_prompt(new_column,self.column,"white")
                #Otherwise, make an identical piece at the target square (this erases the existing piece there)
                else:
                    erase(new_column,new_row)
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)
    
            #If the inputted move is illegal, give an error
            else:
                return illegal_move()

        #For black pawns
        if self.color=="black":    
            #Check if it's a regular move
            if new_column==self.column and (new_row==self.row-1 or new_row==4 and self.row==6) and board[new_column][new_row]=="empty":
                #Handle a potential promotion
                if new_row==0:
                    promote_prompt(new_column,self.column,"black")
                #Otherwise, make an identical piece at the target square
                else:
                    erase(new_column,new_row)
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)                
                
            #Check if it's a capture (pawns capture differently from moving)
            elif abs(new_column-self.column)==1 and new_row==self.row-1 and board[new_column][new_row]!="empty" and board[new_column][new_row].color!=self.color:
                #Handle a potential promotion
                if new_row==0:
                    promote_prompt(new_column,self.column,"black")
                #Otherwise, make an identical piece at the target square (this erases the existing piece there)
                else:
                    erase(new_column,new_row)
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)
    
            #If the inputted move is illegal, give an error
            else:
                return illegal_move()
            

class knight(piece):
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"knight")

    def move(self,new_column,new_row):
        #Legality check: 2 squares over, 1 across
        if not ((abs(new_column-self.column)==2 and abs(new_row-self.row)==1) or (abs(new_column-self.column)==1 and abs(new_row-self.row)==2)):
            return illegal_move()
        #Legality check: not capturing own piece
        elif board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
            return illegal_move()
        #If legal, make an identical piece at the target square, then delete this piece
        else:
            erase(new_column,new_row)
            board[new_column][new_row]=knight(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)


class bishop:               
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"bishop")
        
    def move(self,new_column,new_row):
        #Legality check: diagonal move
        if not (new_column+new_row==self.column+self.row or new_column-self.column==new_row-self.row):
            return illegal_move()
        #Legality check: not staying in same place
        elif new_column==self.column and new_row==self.row:
            return illegal_move()
        #Legality check: not capturing own piece
        elif board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
            return illegal_move()
        #Legality check: not moving over occupied squares
        row_sign=(self.row-new_row)/abs(self.row-new_row)
        column_sign=(self.column-new_column)/abs(self.column-new_column)
        if len(["illegal" for square in range(1,abs(self.column-new_column)) if board[int(new_column+square*column_sign)][int(new_row+square*row_sign)]!="empty"])>0:
            return illegal_move()
        #If legal, make an identical piece at the target square, then delete this piece
        else:
            erase(new_column,new_row)
            board[new_column][new_row]=bishop(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)


class rook:
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"rook")

    def move(self,new_column,new_row):
        #Check if it's a horizontal move
        if new_row==self.row:
            #Legality check: not staying in same place
            if new_column==self.column:
                return illegal_move()
            #Legality check: not capturing own piece
            if board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
                return illegal_move()
            #Legality check: not moving over occupied squares
            column_sign=(self.column-new_column)/abs(self.column-new_column)
            if len(["illegal" for square in range(1,abs(self.column-new_column)) if board[int(new_column+square*column_sign)][new_row]!="empty"])>0:
                return illegal_move()
            #If legal, make an identical piece at the target square, then delete this piece
            erase(new_column,new_row)
            board[new_column][new_row]=rook(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)
        #Check if it's a vertical move
        elif new_column==self.column:
            #Legality check: not staying in same place
            if new_row==self.row:
                return illegal_move()
            #Legality check: not capturing own piece
            if board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
                return illegal_move()
            #Legality check: not moving over occupied squares
            row_sign=(self.row-new_row)/abs(self.row-new_row)
            if len(["illegal" for square in range(1,abs(self.row-new_row)) if board[new_column][int(new_row+square*row_sign)]!="empty"])>0:
                return illegal_move()
            #If legal, make an identical piece at the target square, then delete this piece
            erase(new_column,new_row)
            board[new_column][new_row]=rook(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)

        #If neither horizontal or vertical, the move is illegal
        else:
            return illegal_move()


class queen:
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"queen")

    def move(self,new_column,new_row):
        #Check if it's a horizontal move
        if new_row==self.row:
            #Legality check: not staying in same place
            if new_column==self.column:
                return illegal_move()
            #Legality check: not capturing own piece
            if board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
                return illegal_move()
            #Legality check: not moving over occupied squares
            column_sign=(self.column-new_column)/abs(self.column-new_column)
            if len(["illegal" for square in range(1,abs(self.column-new_column)) if board[int(new_column+square*column_sign)][new_row]!="empty"])>0:
                return illegal_move()
            #If legal, make an identical piece at the target square, then delete this piece
            erase(new_column,new_row)
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)
        #Check if it's a vertical move
        elif new_column==self.column:
            #Legality check: not staying in same place
            if new_row==self.row:
                return illegal_move()
            #Legality check: not capturing own piece
            if board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
                return illegal_move()
            #Legality check: not moving over occupied squares
            row_sign=(self.row-new_row)/abs(self.row-new_row)
            if len(["illegal" for square in range(1,abs(self.row-new_row)) if board[new_column][int(new_row+square*row_sign)]!="empty"])>0:
                return illegal_move()
            #If legal, make an identical piece at the target square, then delete this piece
            erase(new_column,new_row)
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)                           
        #Check if it's a diagonal move
        elif new_column+new_row==self.column+self.row or new_column-self.column==new_row-self.row:
            #Legality check: not staying in same place
            if new_column==self.column and new_row==self.row:
                return illegal_move()
            #Legality check: not capturing own piece
            if board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
                return illegal_move()
            #Legality check: not moving over occupied squares
            row_sign=(self.row-new_row)/abs(self.row-new_row)
            column_sign=(self.column-new_column)/abs(self.column-new_column)
            if len(["illegal" for square in range(1,abs(self.column-new_column)) if board[int(new_column+square*column_sign)][int(new_row+square*row_sign)]!="empty"])>0:
                return illegal_move()
            #If legal, make an identical piece at the target square, then delete this piece
            erase(new_column,new_row)
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)
        #If neither horizontal, vertical, or diagonal, the move is illegal
        else:
            return illegal_move()


class king(piece):
    def __init__(self,column,row,color):
        piece.__init__(self,column,row,color,"king")

    def move(self,new_column,new_row):
        #Castling:
        if self.column==4 and (self.row==new_row==0 and self.color=="white" or self.row==new_row==7 and self.color=="black") and abs(self.column-new_column)==2:
            #Castle short
            if new_column==6 and board[5][self.row]=="empty" and board[6][self.row]=="empty" and type(board[7][self.row]).__name__=="rook":
                board[4][self.row]="empty"
                board[5][self.row]=rook(5,self.row,self.color)
                board[6][self.row]=king(6,self.row,self.color)
                board[7][self.row]="empty"
                erase(4,self.row)
                erase(7,self.row)
            #Castle long               
            elif new_column==2 and board[3][self.row]=="empty" and board[2][self.row]=="empty" and board[1][self.row]=="empty" and type(board[0][self.row]).__name__=="rook":
                board[4][self.row]="empty"
                board[3][self.row]=rook(3,self.row,self.color)
                board[2][self.row]=king(2,self.row,self.color)
                board[0][self.row]="empty"
                erase(4,self.row)
                erase(0,self.row)
            else:
                illegal_move()
        #Legality check: one square over
        elif not (abs(new_column-self.column)+abs(new_row-self.row)==1):
            return illegal_move()
        #Legality check: not capturing own piece
        elif board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
            return illegal_move()
        #If legal, make an identical piece at the target square, then delete this piece
        else:
            erase(new_column,new_row)
            board[new_column][new_row]=king(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
            erase(self.column,self.row)


#Clears a square when a piece leaves it
def erase(col,row):
    #For light square
    if (col+row)/2==int((col+row)/2):
        pygame.draw.rect(screen,(0,68,178),(col*96,(7-row)*96,96,96))
    #For dark square
    else:
        pygame.draw.rect(screen,(140,184,255),(col*96,(7-row)*96,96,96))


#When a pawn promotes
def promote_prompt(new_column,start_column,color):
    if color=="white":
        erase(new_column,7)
        erase(start_column,6)
        #Temporarily place a pawn at the promotion square
        board[new_column][7]=pawn(new_column,7,"white")
        #Prompt the player to select the new piece
        screen.blit(images["buttons"]["promoteWhite"],(847,186))
    elif color=="black":
        erase(new_column,0)
        erase(start_column,1)
        #Temporarily place a pawn at the promotion square
        board[new_column][0]=pawn(new_column,0,"black")
        #Prompt the player to select the new piece
        screen.blit(images["buttons"]["promoteBlack"],(847,186))
    #Activate the promotion button
    buttons["promote"][2]=True
    #Freeze the game until the moving player selects a promotion piece
    global freezed
    freezed=True

#When a player chooses (clicks) on what piece they're promoting to
def Promote():
    #Figure out who promoted and to what square. Clear that square.
    if turn==int(turn):
        color="white"
        for column in range(8):
            if type(board[column][7]).__name__=="pawn":
                square=column
                erase(column,7)
                break
    else:
        color="black"
        for column in range(8):
            if type(board[column][0]).__name__=="pawn":
                square=column
                erase(column,0)
                break
    #Figure out what piece was selected. Place it there and log
    global mouse_col
    global mouse_row
    #The left column
    if mouse_col<944:
        #The top row
        if mouse_row<331.8:
            #Queen
            if color=="white":
                board[square][7]=queen(square,7,"white")
            else:
                board[square][0]=queen(square,0,"black")
            log[len(log)-1].append("queen")
        #The bottom row
        else:
            #Bishop
            if color=="white":
                board[square][7]=bishop(square,7,"white")
            else:
                board[square][0]=bishop(square,0,"black")
            log[len(log)-1].append("bishop")
    #The right column
    else:
        #The top row
        if mouse_row<331.8:
            #Rook
            if color=="white":
                board[square][7]=rook(square,7,"white")
            else:
                board[square][0]=rook(square,0,"black")
            log[len(log)-1].append("rook")
        #The bottom row
        else:
            #Knight
            if color=="white":
                board[square][7]=knight(square,7,"white")
            else:
                board[square][0]=knight(square,0,"black")
            log[len(log)-1].append("knight")
    #Now that the move is finished, advance the turn
    Turn()
    #Erase the promotion menu
    pygame.draw.rect(screen,(100,50,0),(847,186,194,243))
    #Turn off the promotion button
    buttons["promote"][2]=False
    #Resume the game
    global freezed
    freezed=False


#Reaction to illegal move (may change this later)
def illegal_move():
    pass







#---------------------------------------------------------------------------------------------------








#Function that spawns PowerBoxes
def spawn():
    #2/3 of the time:
    if random.randint(0,2)<2:
        #Pick a random square
        column=random.randint(0,7)
        row=random.randint(0,7)
        #If that square is vacant:
        if board[column][row]=="empty":
            #Place a Box (only Regular for now)
            boxes[column][row]="regular"
            screen.blit(images["powers"]["regular"]["box"],(column*96+6,(7-row)*96+6))


#When a regular box is activated, pick two power options
#def reg_activate():
#    choices=["adjust","rewind","2ndeffort","shield","swap"]
#    selected=[]
#    s1=random.choice(choices)
#    selected.append(s1)
#    choices.remove(s1)
#    s2=random.choice(choices)
#    selected.append(s2)
#    choices.remove(s2)


#Function that makes sure each side has a king
def king_verify():
    white=False
    black=False
    #Scans the entire board
    for column in board:
        for piece in column:
            #Records all kings
            if type(piece)==king:
                if piece.color=="white":
                    white=True
                if piece.color=="black":
                    black=True
    #Reports if anyone won
    if not white:
        return "black wins"
    elif not black:
        return "white wins"
    else:
        return "continue"

#When pause button is clicked
def Pause():
    #Tell the game it's paused
    global paused
    paused=True
    global freezed
    freezed=True
    #Display the "continue" button instead
    screen.blit(images["buttons"]["continue"],(800,480))
    #Disactivate the "pause" button and activate "continue"
    buttons["pause"][2]=False
    buttons["continue"][2]=True

def Continue():
    #Unpause
    global paused
    paused=False
    global freezed
    freezed=False
    #Display the "pause" button instead
    screen.blit(images["buttons"]["pause"],(800,480))
    #Disactivate the "continue" button and activate "pause"
    buttons["pause"][2]=True
    buttons["continue"][2]=False

#When restart button is clicked
def Restart():
    #Reset the time and pieces
    reset()

#When help button is clicked
def Help():
    print("#------------PowerChess Rules-------------#")
    print("#                                         #")
    print("#  It's just like regular chess, except:  #")
    print("#                                         #")
    print("#   1. There's no checkmate or stalemate. #")
    print("#   Instead, the game ends whenever one   #")
    print("#   side's king is captured. Yes, that    #")
    print("#   means you can blunder your king.      #")
    print("#                                         #")
    print("#   2. There is no capturing en passant.  #")
    print("#                                         #")
    print("#   3. Each player receives 10 minutes    #")
    print("#   for the entire game, plus 15 seconds  #")
    print("#   after each move. If a player's time   #")
    print("#   expires, they do no lose the game,    #")
    print("#   they simply forfeit their move.       #")
    print("#                                         #")
    print("#   4. PowerBoxes periodically spawn in   #")
    print("#   random squares. They can be captured  #")
    print("#   and activated by either player,       #")
    print("#   allowing that player to move again.   #")
    print("#   Pieces can move over PowerBoxes       #")
    print("#   like over vacant squares.             #")
#    print("#   PowerBoxes come in three rarities:    #")
#    print("#   Regular (grey), Rare (green), and     #")
#    print("#   Legendary (yellow and purple). Upon   #")
#    print("#   activation, players choose one of two #")
#    print("#   special effects corresponding to the  #")
#    print("#   Box's rarity. Less common Boxes       #")
#    print("#   contain more powerful effects.        #")
    print("#-----------------------------------------#")

#When quit button is clicked
def Quit():
    #Tell the game to stop
    global running
    running=False

#Function that sets the board and clock
def reset():
    #Display the board tiles
    for col in range(0,768,192):
        for row in range(0,768,192):
            pygame.draw.rect(screen,(140,184,255),(col,row,96,96))
    for col in range(96,864,192):
        for row in range(96,864,192):
            pygame.draw.rect(screen,(140,184,255),(col,row,96,96))
    for col in range(0,768,192):
        for row in range(96,864,192):
            pygame.draw.rect(screen,(0,68,178),(col,row,96,96))
    for col in range(96,864,192):
        for row in range(0,768,192):
            pygame.draw.rect(screen,(0,68,178),(col,row,96,96))
    pygame.draw.rect(screen,(100,50,0),(768,0,352,768))
    #Set up pieces
    global board
    board=[
        [rook(0,0,"white"),pawn(0,1,"white"),"empty","empty","empty","empty",pawn(0,6,"black"),rook(0,7,"black")],
        [knight(1,0,"white"),pawn(1,1,"white"),"empty","empty","empty","empty",pawn(1,6,"black"),knight(1,7,"black")],
        [bishop(2,0,"white"),pawn(2,1,"white"),"empty","empty","empty","empty",pawn(2,6,"black"),bishop(2,7,"black")],
        [queen(3,0,"white"),pawn(3,1,"white"),"empty","empty","empty","empty",pawn(3,6,"black"),queen(3,7,"black")],
        [king(4,0,"white"),pawn(4,1,"white"),"empty","empty","empty","empty",pawn(4,6,"black"),king(4,7,"black")],
        [bishop(5,0,"white"),pawn(5,1,"white"),"empty","empty","empty","empty",pawn(5,6,"black"),bishop(5,7,"black")],
        [knight(6,0,"white"),pawn(6,1,"white"),"empty","empty","empty","empty",pawn(6,6,"black"),knight(6,7,"black")],
        [rook(7,0,"white"),pawn(7,1,"white"),"empty","empty","empty","empty",pawn(7,6,"black"),rook(7,7,"black")],
    ]
    #Clear all powerBoxes (note that a separate array is used to track boxes)
    global boxes
    boxes=[["empty" for i in range(8)] for j in range(8)]
    #The turn number (integer=white's turn, fraction=black's)
    global turn
    turn=0
    #The game log
    global log
    log=[]
    #The clock (in 1/10 of seconds)
    global whiteTime
    global blackTime
    whiteTime=6000
    blackTime=6000
    displayTime(whiteTime,"white")
    displayTime(blackTime,"black")
    #Control buttons
    screen.blit(images["buttons"]["pause"],(800,480))
    screen.blit(images["buttons"]["restart"],(944,480))
    screen.blit(images["buttons"]["help"],(800,528))
    screen.blit(images["buttons"]["quit"],(944,528))
    #Control variables
    global grabbed
    global freezed
    global paused
    grabbed=False #Whether or not a piece is being moved
    freezed=False #True when a special event is occuring (e.g. promotion) and a player must respond before the next move
    paused=False #Whether or not the clock is paused
    pygame.display.update()

#A function that updates a player's clock on the screen
def displayTime(time,color):
    if color=="white":
        pygame.draw.rect(screen,(100,50,0),(800,580,1100,700))
        screen.blit(font.render(str(floor(time/6000))+str(floor((time-6000*floor(time/6000))/600))+":"+str(floor((time-600*floor(time/600))/100))+str(floor((time-100*floor(time/100))/10)),False,(255,255,255)),(800,580))
    elif color=="black":
        pygame.draw.rect(screen,(100,50,0),(800,0,1100,150))
        screen.blit(font.render(str(floor(time/6000))+str(floor((time-6000*floor(time/6000))/600))+":"+str(floor((time-600*floor(time/600))/100))+str(floor((time-100*floor(time/100))/10)),False,(255,255,255)),(800,0))

#Function that initiates the program
def init():
    #Set up pygame
    pygame.init()
    global screen
    screen=pygame.display.set_mode((1120, 768))
    pygame.display.set_caption("PowerChess")
    #Load the game font
    global font
    font=pygame.font.Font("/Library/Fonts/SukhumvitSet.ttc",123)
    #Create an event that updates the clock 10 times per second'
    global TICK
    TICK=pygame.USEREVENT+1
    pygame.time.set_timer(TICK,100)

#Function called after every turn
def Turn():
    global turn
    global whiteTime
    global blackTime
    #Give the moving player 15 seconds
    if turn==int(turn):
        whiteTime+=150
        displayTime(whiteTime,"white")
    else:
        blackTime+=150
        displayTime(blackTime,"black")
    #Advance the turn
    turn+=0.5
    #Spawn new PowerBoxes
    spawn()








#---------------------------------------------------------------------------------------------------







import pygame
import os
from math import floor
import random
os.chdir("/Users/Thymathgeek/Dropbox/Senior Project")

#Dictionary that stores images
images={
    "white":{
        "king":pygame.image.load("Graphics/Pieces/White/WhiteKing.png"),
        "queen":pygame.image.load("Graphics/Pieces/White/WhiteQueen.png"),
        "rook":pygame.image.load("Graphics/Pieces/White/WhiteRook.png"),
        "bishop":pygame.image.load("Graphics/Pieces/White/WhiteBishop.png"),
        "knight":pygame.image.load("Graphics/Pieces/White/WhiteKnight.png"),
        "pawn":pygame.image.load("Graphics/Pieces/White/WhitePawn.png")},
    "black":{
        "king":pygame.image.load("Graphics/Pieces/Black/BlackKing.png"),
        "queen":pygame.image.load("Graphics/Pieces/Black/BlackQueen.png"),
        "rook":pygame.image.load("Graphics/Pieces/Black/BlackRook.png"),
        "bishop":pygame.image.load("Graphics/Pieces/Black/BlackBishop.png"),
        "knight":pygame.image.load("Graphics/Pieces/Black/BlackKnight.png"),
        "pawn":pygame.image.load("Graphics/Pieces/Black/BlackPawn.png")},
    "buttons":{
        "continue":pygame.image.load("Graphics/Buttons/Unpressed/Continue.png"),
        "back":pygame.image.load("Graphics/Buttons/Unpressed/GoBack.png"),
        "help":pygame.image.load("Graphics/Buttons/Unpressed/Help.png"),
        "pause":pygame.image.load("Graphics/Buttons/Unpressed/Pause.png"),
        "quit":pygame.image.load("Graphics/Buttons/Unpressed/Quit.png"),
        "restart":pygame.image.load("Graphics/Buttons/Unpressed/Restart.png"),
        "promoteWhite":pygame.image.load("Graphics/Buttons/Unpressed/PromoteWhite.png"),
        "promoteBlack":pygame.image.load("Graphics/Buttons/Unpressed/PromoteBlack.png")},
    "powers":{
        "regular":{
            "box":pygame.image.load("Graphics/Powers/Regular/RegularBox.png"),
            "adjust":pygame.image.load("Graphics/Powers/Regular/Regular-Adjust.png"),
            "rewind":pygame.image.load("Graphics/Powers/Regular/Regular-Rewind.png"),
            "2ndeffort":pygame.image.load("Graphics/Powers/Regular/Regular-SecondEffort.png"),
            "shield":pygame.image.load("Graphics/Powers/Regular/Regular-Shield.png"),
            "swap":pygame.image.load("Graphics/Powers/Regular/Regular-Swap.png")}#,
#        "rare":{
#            "box":pygame.image.load("Graphics/Powers/Rare/RareBox.png"),
#            "blackhole":pygame.image.load("Graphics/Powers/Rare/Rare-BlackHole*.png"),
#            "energize":pygame.image.load("Graphics/Powers/Rare/Rare-Energize*.png"),
#            "eye4Neye":pygame.image.load("Graphics/Powers/Rare/Rare-EyeForAnEye*.png"),
#            "safetynet":pygame.image.load("Graphics/Powers/Rare/Rare-SafetyNet*.png"),
#            "sendaway":pygame.image.load("Graphics/Powers/Rare/Rare-SendAway*.png")},
#        "legendary":{
#            "box":pygame.image.load("Graphics/Powers/Legendary/LegendaryBox.png"),
#            "armageddon":pygame.image.load("Graphics/Powers/Legendary/Legendary-Armageddon.png"),
#            "awaken"::pygame.image.load("Graphics/Powers/Legendary/Legendary-Awaken.png"),
#            "clone":pygame.image.load("Graphics/Powers/Legendary/Legendary-Clone.png"),
#            "cloneking":pygame.image.load("Graphics/Powers/Legendary/Legendary-CloneKing.png"),
#            "moat":pygame.image.load("Graphics/Powers/Legendary/Legendary-Moat.png"),
#            "reanimate":pygame.image.load("Graphics/Powers/Legendary/Legendary-Reanimate.png")}
}}

#Dictionary that inventorizes all active buttons and their locations and functions
#Format: name: [[Xmin, Xmax], [Ymin, Ymax]], function, whether activated]
buttons={
    "pause": [[[800, 944], [480, 528]], Pause, True],
    "continue": [[[800, 944], [480, 528]], Continue, False],
    "help": [[[800, 944], [528, 576]], Help, True],
    "restart": [[[944, 1088], [480, 528]], Restart, True],
    "quit": [[[944, 1088], [528, 576]], Quit, True],
    "promote": [[[847, 1041], [234.6, 429]], Promote, False]
}

init()
reset()

#The gameplay loop
running=True #This variable can be turned false to end the game
while running:
    for event in pygame.event.get():
        #Close button is pressed
        if event.type == pygame.QUIT:
            Quit()
        #Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_col=pygame.mouse.get_pos()[0]
            mouse_row=pygame.mouse.get_pos()[1]
            #Piece is grabbed
            if mouse_col<768 and not freezed:
                #Figure out what square is pressed on
                col=floor(mouse_col/96)
                row=7-floor(mouse_row/96)
                #Check if that square contains a piece of the moving side's color
                if board[col][row]!="empty":
                    if (int(turn)==turn and board[col][row].color=="white") or (int(turn)!=turn and board[col][row].color=="black"):
                        #Get a copy of the board without the moving piece
                        erase(col,row)
                        background=screen.copy()
                        #Determine the type and color of piece and get its image
                        moving=images[board[col][row].color][type(board[col][row]).__name__]
                        #Allow the piece to be dragged
                        grabbed=True
            #Button is pressed: determine which one and call the appropriate function
            else:
                #Loops through all buttons
                for button in buttons:
                    #Executes a button's code if it's active and the mouse clicked in the right place
                    if buttons[button][2] and buttons[button][0][0][0]<mouse_col<buttons[button][0][0][1] and buttons[button][0][1][0]<mouse_row<buttons[button][0][1][1]:
                        buttons[button][1]()
                        break
        #Piece is put down
        if event.type == pygame.MOUSEBUTTONUP:
            #If a piece was being moved:
            if grabbed:
                #Figure out what square the piece is placed on
                finish_col=floor(pygame.mouse.get_pos()[0]/96)
                finish_row=7-floor(pygame.mouse.get_pos()[1]/96)
                #Release the piece
                grabbed=False
                screen.blit(background,(0,0),(0,0,810,810))
                #Attempt to move
                board[col][row].move(finish_col,finish_row)
                #If the move was successful:
                if board[col][row]=="empty":
                    #Log the move
                    log.append([[col,row],[finish_col,finish_row]])
                    #Advance the turn order unless further action is required
                    if boxes[finish_col][finish_row]=="empty" and not freezed:
                        Turn()
                    #Clear any PowerBoxes that may have been activated
                    boxes[finish_col][finish_row]="empty"                       
                    #Ensure both kings are present
                    if king_verify()!="continue":
                        print(king_verify())
                        Continue=False
                #Otherwise, put the piece back
                else:
                    screen.blit(moving,(col*96,(7-row)*96))
        #Every 1/10 of a second, the clock of the player to move ticks
        if event.type == TICK and not paused:
            if turn==int(turn):
                whiteTime-=1
                #If you run out of time you lose your move
                if whiteTime==0:
                    Turn()
                    whiteTime+=150
                displayTime(whiteTime,"white")
            else:
                blackTime-=1
                #If you run out of time you lose your move
                if blackTime==0:
                    Turn()
                    blackTime+=150
                displayTime(blackTime,"black")
    #If a piece is being moved:
    if grabbed:
        screen.blit(background,(0,0),(0,0,810,810))
        screen.blit(moving,(min(720,pygame.mouse.get_pos()[0]-48),pygame.mouse.get_pos()[1]-48))
    #Update the display accordingly
    pygame.display.update()
pygame.quit()
