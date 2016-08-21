def isUnique(str):
    dict = {}

    for ch in str:
        if ch in dict:
            return False
        dict[ch] = 1

    return True

def isUnique2(str):
    ordered = sorted(str)

    for i in range(len(ordered)-1):
        if ordered[i] == ordered[i+1]:
            return False

    return True

class Test:
    
    cases = ["", "a", "fadsf", "asdfgh"]

    def execute(self, func):
        print("---------")
        for test in self.cases:
            print(func(test))


tests = Test()

tests.execute(isUnique)
tests.execute(isUnique2)
