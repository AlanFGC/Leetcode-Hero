def recursive(string:str) -> int:
        if string == "1":
            print(11)
            return 11
        
        i = 0
        subs = []
        while i < len(string):
            j = i
            while j < len(string):
                if i == j:
                    subs.append(string[j])
                    j += 1
                elif string[j] == string[i]:
                    subs[-1] += string[j]
                    j+=1
                else:
                    break
            i = j
        result = []
        for each in subs:
            result.append(str(len(each)) + each[0])
        print(result)
        return int("".join(result))


class Solution:
    def countAndSay(self, n: int) -> str:
        r = 1
        if n == 1:
            return "1"
        
        for i in range(n-1):
            r = str(recursive(str(r)))
        return r
            