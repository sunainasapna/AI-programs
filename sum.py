class lis:
    def __init__(self):
        self.input()
    
    def input(self):
        self.length=int(input("Enter number of elements in list\t--->\t"))
        self.arr=[]
        for i in range (self.length):
            print("Enter element",i+1,"\t:\t",end='')
            temp=int(input())
            self.arr.append(temp)
        self.add()

    def add(self):
        for i in range(len(self.arr)):
            if i==0:
                print(self.arr[i],end='')
            else:
                print(" + ",self.arr[i],end='')
        print(" = ",sum(self.arr))

lis()