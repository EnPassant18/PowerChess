class pawn(object):
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

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
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
    
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
                    board[new_column][new_row]=pawn(new_column,new_row,self.color)
                #Delete this piece
                board[self.column][self.row]="empty"
    
            #If the inputted move is illegal, give an error
            else:
                return illegal_move()
            
#Will add en passant after establshing a turn order


class knight:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

    def move(self,new_column,new_row):
        #Legality check: 2 squares over, 1 across
        if not ((abs(new_column-self.column)==2 and abs(new_row-self.row)==1) or (abs(new_column-self.column)==1 and abs(new_row-self.row)==2)):
            return illegal_move()
        #Legality check: not capturing own piece
        elif board[new_column][new_row]!="empty" and board[new_column][new_row].color==self.color:
            return illegal_move()
        #If legal, make an identical piece at the target square, then delete this piece
        else:
            board[new_column][new_row]=knight(new_column,new_row,self.color)
            board[self.column][self.row]="empty"


class bishop:               
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

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
            board[new_column][new_row]=bishop(new_column,new_row,self.color)
            board[self.column][self.row]="empty"


class rook:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

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
            board[new_column][new_row]=rook(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
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
            board[new_column][new_row]=rook(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
        #If neither horizontal or vertical, the move is illegal
        else:
            return illegal_move()


class queen:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

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
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
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
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
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
            board[new_column][new_row]=queen(new_column,new_row,self.color)
            board[self.column][self.row]="empty"
        #If neither horizontal, vertical, or diagonal, the move is illegal
        else:
            return illegal_move()

class king:
    def __init__(self,column,row,color):
        #Input color and location
        self.column=column
        self.color=color
        self.row=row

    def move(self,new_column,new_row):
        #Castling:
        if self.column==4 and (self.row==new_row==0 and self.color=="white" or self.row==new_row==7 and self.color=="black") and abs(self.column-new_column)==2:
            #Castle short
            if new_column==6 and board[5][self.row]=="empty" and board[6][self.row]=="empty" and type(board[7][self.row])==rook and board[7][self.row].color=="white":
                board[4][self.row]="empty"
                board[5][self.row]=rook(5,self.row,self.color)
                board[6][self.row]=king(6,self.row,self.color)
                board[7][self.row]="empty"
            #Castle long               
            elif new_column==2 and board[3][self.row]=="empty" and board[2][self.row]=="empty" and board[1][self.row]=="empty" and type(board[0][self.row])==rook and board[0][self.row].color=="black":
                board[4][self.row]="empty"
                board[3][self.row]=rook(3,self.row,self.color)
                board[2][self.row]=king(2,self.row,self.color)
                board[0][self.row]="empty"
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
            board[new_column][new_row]=king(new_column,new_row,self.color)
            board[self.column][self.row]="empty"

def illegal_move():
    print("illegal move")
#Will update this after building GUI


#------------------
#------------------
#------------------
#------------------

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
#The turn number (integer=white's turn, fraction=black's)
turn=0
#The game log
log=[]

#The gameplay loop
while True: 
    start_col=int(input("Start square column: "))
    start_row=int(input("Start square row: "))
    finish_col=int(input("Target square column: "))
    finish_row=int(input("Target square row: "))
    #Ensure the moving piece is of the appropriate color
    if (int(turn)==turn and board[start_col][start_row].color=="white") or (int(turn)!=turn and board[start_col][start_row].color=="black"):
        board[start_col][start_row].move(finish_col,finish_row)
        #Ensure the piece moved (i.e. move was legal), and if it did, advance the turn order and record
        if board[start_col][start_row]=="empty":
            turn+=0.5
            log.append([[start_col,start_row],[finish_col,finish_row]])
    else:
        illegal_move()
