class student:
    def __init__(self):
        self.urn = []
        self.name = []
        self.mobile = []
        self.year = []
        self.input()

    def input(self):
        self.choice1 = int(input(
            "Enter 1 to add data\tEnter 2 to view data\tEnter 3 to delete data\tEnter 4 to quit\t--->\t"))
        if self.choice1 == 1:
            self.add()
        elif self.choice1 == 2:
            self.view()
        elif self.choice1 == 3:
            self.delete()
        elif self.choice1 == 4:
            exit()
        else:
            self.input()

    def add(self):
        temp = int(input("Enter URN of student\t--->\t"))
        self.urn.append(temp)
        temp = str(input("Enter Name of student\t--->\t"))
        self.name.append(temp)
        temp = int(input("Enter Mobile Number of student\t--->\t"))
        self.mobile.append(temp)
        temp = int(input("Enter Year of student\t--->\t"))
        self.year.append(temp)
        self.input()

    def view(self):
        self.choice2 = int(
            input("Enter 1 to view all data\tEnter 2 to search with URN\t--->\t"))
        if self.choice2 == 1:
            for i in range(len(self.urn)):
                print(self.urn[i], self.name[i], self.mobile[i], self.year[i])
            self.input()
        elif self.choice2 == 2:
            roll = int(input("Enter URN of the student\t--->\t"))
            for i in range(len(self.urn)):
                if self.urn[i] == roll:
                    print(self.urn[i], self.name[i],
                          self.mobile[i], self.year[i])
                    self.input()
            print("No student with URN = ", roll)
            self.input()
        else:
            self.view()

    def delete(self):
        roll = int(input("Enter URN of student to delete data\t--->\t"))
        for i in range(len(self.urn)):
            if self.urn[i] == roll:
                self.urn.pop(i)
                self.name.pop(i)
                self.mobile.pop(i)
                self.year.pop(i)
                self.input()
                break
            else:
                pass
        self.input()


student()
