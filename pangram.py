class pangram:
    def __init__(self):
        self.inp=[]
        self.input()
        super().__init__()
    
    def input(self):
        self.string=str(input("Enter any string\t--->\t"))
        self.check()
    
    def check(self):
        self.alpha="abcdefghijklmnopqrstuvwxyz"
        for i in self.alpha:
            if i not in self.string.lower():
                print("Not a pangram")
                return
        print("Pangram")

pangram()     
