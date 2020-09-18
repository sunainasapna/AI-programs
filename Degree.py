class convert:
    def __init__(self):
        self.input()

    def input(self):
        self.deg = float(input("Enter the input\t--->\t"))
        self.choice = float(input(
            "Enter 1 to convert to degree celsius\t Enter 2 to convert on degree fahrenheit\t--->\t"))
        if self.choice == 1:
            self.celsius()
        elif self.choice == 2:
            self.fahrenheit()
        else:
            self.input()

    def celsius(self):
        self.cel = float((self.deg-32)*5/9)
        print(self.deg, "deg. F = ", self.cel, " deg. C")

    def fahrenheit(self):
        self.fah = float((self.deg*9/5)+32)
        print(self.deg, "deg. C = ", self.fah, "deg. F")


convert()
