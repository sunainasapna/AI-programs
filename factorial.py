class factorial:
    def __init__(self):
        self.input()
    
    def input(self):
        self.number=int(input("Enter a positive integer to find factorial\t:\t"))
        if self.number<=1:
            print(self.number,"! = ",1)
        else:
            print(self.number,"! = ",self.fact(self.number))
    
    def fact(self,a):
        if a==1:
            return a
        else:
            return a*self.fact(a-1)
        

factorial()