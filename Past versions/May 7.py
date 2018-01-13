#IMPORTANT NOTE: the ROW each piece is displayed in is INVERTED horizontally with respect to the row it's stored in
class pawn:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.row=row
        self.color=color
        screen.blit(images[color]["pawn"],(column*96,(7-row)*96))

    def move(self,new_column,new_row):
    #For white pawns       
        if self.color=="white":           
            #Check if it's a regular move
            if new_column==self.column and (new_row==self.row+1 or new_row==3 and self.row==1) and board[new_column][new_row]=="empty":
                #Handle a potential promotion
                if new_row==7:
                    new_piece=input("Promote to which piece? ")
                    if new_piece=="queen":
                        board[new_column][new_row]=queen(new_column,new_row,self.color)
                    if new_piece=="rook":
                        board[new_column][new_row]=rook(new_column,new_row,self.color)
                    if new_piece=="bishop":
                        board[new_column][new_row]=bishop(new_column,new_row,self.color)
                    if new_piece=="knight":
                        board[new_column][new_row]=knight(new_column,new_row,self.color)
                #Otherwise, make an identical piece at the target square
                else:
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)
                
            #Check if it's a capture (pawns capture differently from moving)
            elif abs(new_column-self.column)==1 and new_row==self.row+1 and board[new_column][new_row]!="empty" and board[new_column][new_row].color!=self.color:
                #Handle a potential promotion
                if new_row==7:
                    new_piece=input("Promote to which piece? ")
                    if new_piece=="queen":
                        board[new_column][new_row]=queen(new_column,new_row,self.color)
                    if new_piece=="rook":
                        board[new_column][new_row]=rook(new_column,new_row,self.color)
                    if new_piece=="bishop":
                        board[new_column][new_row]=bishop(new_column,new_row,self.color)
                    if new_piece=="knight":
                        board[new_column][new_row]=knight(new_column,new_row,self.color)
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
                    new_piece=input("Promote to which piece? ")
                    if new_piece=="queen":
                        board[new_column][new_row]=queen(new_column,new_row,self.color)
                    if new_piece=="rook":
                        board[new_column][new_row]=rook(new_column,new_row,self.color)
                    if new_piece=="bishop":
                        board[new_column][new_row]=bishop(new_column,new_row,self.color)
                    if new_piece=="knight":
                        board[new_column][new_row]=knight(new_column,new_row,self.color)
                #Otherwise, make an identical piece at the target square
                else:
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
                erase(self.column,self.row)                
                
            #Check if it's a capture (pawns capture differently from moving)
            elif abs(new_column-self.column)==1 and new_row==self.row-1 and board[new_column][new_row]!="empty" and board[new_column][new_row].color!=self.color:
                #Handle a potential promotion
                if new_row==0:
                    new_piece=input("Promote to which piece? ")
                    if new_piece=="queen":
                        board[new_column][new_row]=queen(new_column,new_row,self.color)
                    if new_piece=="rook":
                        board[new_column][new_row]=rook(new_column,new_row,self.color)
                    if new_piece=="bishop":
                        board[new_column][new_row]=bishop(new_column,new_row,self.color)
                    if new_piece=="knight":
                        board[new_column][new_row]=knight(new_column,new_row,self.color)
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
            

class knight:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
        screen.blit(images[color]["knight"],(column*96,(7-row)*96))

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
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
        screen.blit(images[color]["bishop"],(column*96,(7-row)*96))
        
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
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
        screen.blit(images[color]["rook"],(column*96,(7-row)*96))

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
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
        screen.blit(images[color]["queen"],(column*96,(7-row)*96))

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

class king:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
        screen.blit(images[color]["king"],(column*96,(7-row)*96))

    def move(self,new_column,new_row):
        #Castling:
        if self.column==4 and (self.row==new_row==0 and self.color=="white" or self.row==new_row==7 and self.color=="black") and abs(self.column-new_column)==2:
            #Castle short
            if new_column==6 and board[5][self.row]=="empty" and board[6][self.row]=="empty" and type(board[7][self.row])==rook and board[7][self.row].color=="white":
                board[4][self.row]="empty"
                board[5][self.row]=rook(5,self.row,self.color)
                board[6][self.row]=king(6,self.row,self.color)
                board[7][self.row]="empty"
                erase(4,self.row)
                erase(7,self.row)
            #Castle long               
            elif new_column==2 and board[3][self.row]=="empty" and board[2][self.row]=="empty" and board[1][self.row]=="empty" and type(board[0][self.row])==rook and board[0][self.row].color=="black":
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



#------------------
#------------------
#------------------
#------------------



#Will update this after building GUI
def illegal_move():
    pass

#Function that clears a square when a piece leaves it
def erase(col,row):
    #For light square
    if (col+row)/2==int((col+row)/2):
        pygame.draw.rect(screen,(0,68,178),(col*96,(7-row)*96,96,96))
    #For dark square
    else:
        pygame.draw.rect(screen,(140,184,255),(col*96,(7-row)*96,96,96))
        
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
    if not white:
        return "black wins"
    elif not black:
        return "white wins"
    else:
        return "continue"

def Pause():
    global paused
    paused=True
    screen.blit(images["buttons"]["continue"],(800,480))

def Restart():
    init()

def Help():
    print("#------------PowerChess Rules-------------#")
    print("#                                         #")
    print("#  It's just like regular chess, except:  #")
    print("#                                         #")
    print("#   1. There is no check or checkmate.    #")
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
    print("#   and activated by either player.       #")
    print("#   However, pieces can move over         #")
    print("#   PowerBoxes like over vacant squares.  #")
    print("#   PowerBoxes come in three rarities:    #")
    print("#   Regular (grey), Rare (green), and     #")
    print("#   Legendary (yellow and purple). Upon   #")
    print("#   activation, players choose one of two #")
    print("#   special effects corresponding to the  #")
    print("#   Box's rarity. Less common Boxes       #")
    print("#   contain more powerful effects.        #")

def Quit():
    global Continue
    Continue=False

#The initiation function
def init():
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
    pygame.draw.rect(screen,(100,50,0),(768,0,1120,768))
    #Set up game board
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
    pygame.display.update()

#A function that updates a player's clock on the screen
def displayTime(time,color):
    if color=="white":
        pygame.draw.rect(screen,(100,50,0),(800,580,1100,700))
        screen.blit(font.render(str(floor(time/6000))+str(floor((time-6000*floor(time/6000))/600))+":"+str(floor((time-600*floor(time/600))/100))+str(floor((time-100*floor(time/100))/10)),False,(255,255,255)),(800,580))
    elif color=="black":
        pygame.draw.rect(screen,(100,50,0),(800,0,1100,150))
        screen.blit(font.render(str(floor(time/6000))+str(floor((time-6000*floor(time/6000))/600))+":"+str(floor((time-600*floor(time/600))/100))+str(floor((time-100*floor(time/100))/10)),False,(255,255,255)),(800,0))


#------------------
#------------------
#------------------
#------------------


import pygame
import os
from math import floor
os.chdir("/Users/Thymathgeek/Dropbox/Senior Project")
pygame.init()
screen=pygame.display.set_mode((1120, 768))
pygame.display.set_caption("PowerChess")
#Load the game font
font=pygame.font.Font("/Library/Fonts/SukhumvitSet.ttc",123)
#An event that updates the clock 10 times per second
TICK=pygame.USEREVENT+1
pygame.time.set_timer(TICK,100)

#Load the images
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
        "continue":pygame.image.load("Graphics/Buttons/Pressed/Continue*.png"),
        "back":pygame.image.load("Graphics/Buttons/Pressed/GoBack*.png"),
        "help":pygame.image.load("Graphics/Buttons/Pressed/Help*.png"),
        "pause":pygame.image.load("Graphics/Buttons/Pressed/Pause*.png"),
        "quit":pygame.image.load("Graphics/Buttons/Pressed/Quit*.png"),
        "restart":pygame.image.load("Graphics/Buttons/Pressed/Restart*.png")}
#    "powers":{
#        "regular":{
#            "box":pygame.image.load("Graphics/Powers/Regular/RegularBox.png"),
#            "adjust":pygame.image.load("Graphics/Powers/Regular/Regular-Adjust.png"),
#            "rewind":pygame.image.load("Graphics/Powers/Regular/Regular-Rewind.png"),
#            "2ndeffort":pygame.image.load("Graphics/Powers/Regular/Regular-SecondEffort.png"),
#            "shield":pygame.image.load("Graphics/Powers/Regular/Regular-Shield.png"),
#            "swap":pygame.image.load("Graphics/Powers/Regular/Regular-Swap.png")},
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
}

init()

#The gameplay loop
Continue=True #This variable can be turned off to end the game
grabbed=False #Whether or not a piece is being moved
paused=False #Whether or not the game is paused
while Continue:
    for event in pygame.event.get():
        #Close button is pressed
        if event.type == pygame.QUIT:
            Quit()
        #Mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_col=pygame.mouse.get_pos()[0]
            mouse_row=pygame.mouse.get_pos()[1]
            #Piece is grabbed
            if mouse_col<768 and not paused:
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
            #Button is pressed
            if 800<mouse_col<1088 and 480<mouse_row<576:
                if 800<mouse_col<944:
                    if 480<mouse_row<528:
                        if not paused:
                            Pause()
                        else:
                            paused=False
                            screen.blit(images["buttons"]["pause"],(800,480))
                    else:
                        Help()
                else:
                    if 480<mouse_row<528:
                        paused=False
                        Restart()
                    else:
                        Quit()
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
                #Attempt to move (functionally)
                board[col][row].move(finish_col,finish_row)
                #If the move was successful:
                if board[col][row]=="empty":
                    #Give the moving player 15 seconds
                    if turn==int(turn):
                        whiteTime+=150
                        displayTime(whiteTime,"white")
                    else:
                        blackTime+=150
                        displayTime(blackTime,"black")
                    #Advance the turn order and log the move
                    turn+=0.5
                    log.append([[col,row],[finish_col,finish_row]])
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
                    turn+=0.5
                    whiteTime+=150
                displayTime(whiteTime,"white")
            else:
                blackTime-=1
                #If you run out of time you lose your move
                if blackTime==0:
                    turn+=0.5
                    blackTime+=150
                displayTime(blackTime,"black")
    #If a piece is being moved:
    if grabbed:
        screen.blit(background,(0,0),(0,0,810,810))
        screen.blit(moving,(min(720,pygame.mouse.get_pos()[0]-48),pygame.mouse.get_pos()[1]-48))
    #Update the display accordingly
    pygame.display.update()
pygame.quit()
