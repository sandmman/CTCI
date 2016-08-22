def reverse(str):
    newStr = ""

    for i in range(len(str)-1,-1,-1):
        newStr += str[i]
    
    return newStr

# Have to create an array to do an 'in place' reversal since strings are immutable
def inPlaceReverse(str):
    arr = list(str)
    arr.append("\n")
    for i in range(0,(len(arr)-1)//2):
        tmp = arr[i]
        arr[i] = str[len(arr) - 2 - i]
        arr[len(arr) - 2 - i] = tmp

    return "".join(arr)


class Tests:

    cases = ["", "a", "ab", "asdf","asdfg"]

    def execute(self, func):
        for case in self.cases:
            print(func(case))

tests = Tests()

tests.execute(reverse)
tests.execute(inPlaceReverse)
