board=[["empty" for i in range(8)] for j in range(8)]

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
            if new_column==self.column and new_row==self.row+1 and board[new_column][new_row]=="empty":
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
            if new_column==self.column and new_row==self.row-1 and board[new_column][new_row]=="empty":
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
        #Legality check: one square over
        if not (abs(new_column-self.column)<=1 and abs(new_row-self.row)<=1):
            return illegal_move()
        #Legality check: not staying in same place
        elif new_column==self.column and new_row==self.row:
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
