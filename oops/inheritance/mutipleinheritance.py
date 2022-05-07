#  Multiple Inheritance:- When the child class inherits from multiple parent classes

class king:
    throne = None 
    def king(self):
        print("King owns the throne")

class queen:
    def queen(self):
        print("Queen controls the throne through the king")

class prince(king, queen):
    throne = True
    def prince(self):
        print("prince is ladla bcha of king and queen")


K = king()
Q = queen()
P = prince()

P.king()
P.queen()
P.prince()
print(P.throne)
