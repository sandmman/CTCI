
def isAnagram(str1, str2):
    dct = {}

    for ch in str1:
        if ch not in dct:
            dct[ch] = 0
        dct[ch] += 1

    for ch in str2:
        if ch not in dct:
            return False
        dct[ch] -= 1
        if dct[ch] < 0:
            return False
    return True

class Test:

    cases = [("",""),("abc","accb"),("abc","bca")]

    def execute(self, func):
        for case in self.cases:
            print(func(case[0],case[1]))


test = Test()

test.execute(isAnagram)
