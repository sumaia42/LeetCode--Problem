class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'CM':900,'D':500,'M':1000}
        total = 0
        x = 0
        while x < len(s):
            if s[x:x+2] in a:
                total += a[s[x:x+2]]
                x += 2
            else:
                total = total + a[s[x]]
                x += 1
        return total
        