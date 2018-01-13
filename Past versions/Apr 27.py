#IMPORTANT NOTE: the ROW each piece is displayed in is INVERTED horizontally with respect to the row it's stored in
class pawn:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row
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

#Will update this after building GUI
def illegal_move():
    print("illegal move")

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



#------------------
#------------------
#------------------
#------------------


import pygame
import os
from math import floor

#Set up display
os.chdir("/Users/Thymathgeek/Dropbox/Senior Project")
pygame.init()
screen=pygame.display.set_mode((768, 768))
pygame.display.set_caption("PowerChess")
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
#Load the images
images={
    "white":{
        "king":pygame.image.load("Graphics/WhiteKing.png"),
        "queen":pygame.image.load("Graphics/WhiteQueen.png"),
        "rook":pygame.image.load("Graphics/WhiteRook.png"),
        "bishop":pygame.image.load("Graphics/WhiteBishop.png"),
        "knight":pygame.image.load("Graphics/WhiteKnight.png"),
        "pawn":pygame.image.load("Graphics/WhitePawn.png")},
    "black":{
        "king":pygame.image.load("Graphics/BlackKing.png"),
        "queen":pygame.image.load("Graphics/BlackQueen.png"),
        "rook":pygame.image.load("Graphics/BlackRook.png"),
        "bishop":pygame.image.load("Graphics/BlackBishop.png"),
        "knight":pygame.image.load("Graphics/BlackKnight.png"),
        "pawn":pygame.image.load("Graphics/BlackPawn.png")}}
#Set up game board
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
pygame.display.update()
#The turn number (integer=white's turn, fraction=black's)
turn=0
#The game log
log=[]

#The gameplay loop
Continue=True #This variable can be turned off to end the game
grabbed=False
while Continue:
    for event in pygame.event.get():
        #Close button is pressed
        if event.type == pygame.QUIT:
            Continue=False
        #Piece is picked up
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Figure out what square is pressed on
            col=floor(pygame.mouse.get_pos()[0]/96)
            row=7-floor(pygame.mouse.get_pos()[1]/96)
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
        #Piece is put down
        if event.type == pygame.MOUSEBUTTONUP:
            #If a piece was being moved:
            if grabbed:
                #Figure out what square the piece is placed on
                finish_col=floor(pygame.mouse.get_pos()[0]/96)
                finish_row=7-floor(pygame.mouse.get_pos()[1]/96)
                #Release the piece
                grabbed=False
                screen.blit(background,(0,0))
                #Attempt to move (functionally)
                board[col][row].move(finish_col,finish_row)
                #If the move was successful:
                if board[col][row]=="empty":
                    #Advance the turn order and log the move
                    turn+=0.5
                    log.append([[col,row],[finish_col,finish_row]])
                    #Ensure both kings are present
                    if king_verify()!="continue":
                        #End of game sequence
                        Continue=False
                #Otherwise, put the piece back
                else:
                    screen.blit(moving,(col*96,(7-row)*96))
    #If a piece is being moved:
    if grabbed:
        screen.blit(background,(0,0))
        screen.blit(moving,(pygame.mouse.get_pos()[0]-48,pygame.mouse.get_pos()[1]-48))
    #Update the display accordingly
    pygame.display.update()
pygame.quit()
