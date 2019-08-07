class String():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = str(input("enter the string"))

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()
