class puzzle:
    def __init__(self):
        self.board
        self.position
        self.cont_move = 0
    def verify_move(self, curr_position, movement):
        if (self.movement=='up'or self.movement=='down'):
            return True
    def increase_move(self,movement):
        if self.verify_move(self.position, movement):
            self.cont_move+=1
    def is_solved(self):
        solvedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        
        currentArray = [cell for row in self.board for cell in row]

        return currentArray == solvedArray
    
        




