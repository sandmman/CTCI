def removeDups(str):
    mp = {}
    
    i = 0
    while i < len(str):
        if str[i] in mp:
            str = str[:i] + str[i+1:]
            continue
        mp[str[i]] = 1
        i += 1
    return str

def removeDups2(str):
    str = sorted(str)

    i = 0
    while i < len(str) - 1:
        if str[i] == str[i+1]:
            str = str[:i] + str[i+1:]
            continue
        i += 1
    return "".join(str)
class Tests:
    
    def __init__(self):
        self.tests = ["","baabb","aab","zasxasasdfvgar"]
    
    def execute(self, func):
        for test in self.tests:
            print(func(test))

t = Tests()
t.execute(removeDups)
t.execute(removeDups2)
