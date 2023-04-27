# Given a string only containing round brackets ' ( ) ' and lowercase characters,
# remove the least amount of brackets so the string is valid
# A string is considered valid if it's empty or if all the brackets close

# Sample input "a)bc(d)" Removing the one closing bracket creates a valid string
# "))((" we have to remove all brackets (emtpy or all brackets should close
# "(ab(c)d" can be ab(c)d or (abc)d

# No spaces, only lowercase characters. No brackets is also a solution

class Min_Brackets:
    def __init__(self):
        self.stack = []
        self.new_string: []

    def parse_string(self, string):
        self.new_string = list(string)
        for index, char in enumerate(string):
            if char == "(":
                self.stack.append(index)
            elif char == ")":
                # If the stack is not empty, pop. Else, append the index to remove it from the string
                if len(self.stack) >= 1:
                    self.stack.pop()
                else:
                    self.stack.append(index)

        self.remove_extras(string)

    def remove_extras(self, string):
        extra_brackets = len(self.stack)
        if len(self.stack) > 0:
            print(self.stack)
            while len(self.stack) > 0:
                temp = self.stack.pop()
                del self.new_string[temp]
            trimmed_string = "".join(self.new_string)
            print(f"String {string} had {extra_brackets} brackets removed. The new string is {trimmed_string}")
        else:
            print("The string does not need to be modified")


__name__ = "__main__"

string = "a(bcde)fghi)((test)"

min_brackets = Min_Brackets()
min_brackets.parse_string(string)
