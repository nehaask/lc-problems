def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        countS, countT = dict(), dict()
        for i in range(len(s)):
            if not s[i] in countS.keys():
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1

        for i in range(len(t)):
            if not t[i] in countT.keys():
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1

        if countS == countT:
            return True
        return False


print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))
