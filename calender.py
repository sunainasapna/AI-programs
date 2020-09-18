import calendar
class Cal:
    def __init__(self):
        self.input()
        super().__init__()
    
    def input(self):
        self.yea=int(input("Enter an year to print calender\t:\t"))
        self.calen()
    
    def calen(self):
        print(calendar.calendar(self.yea))

Cal()