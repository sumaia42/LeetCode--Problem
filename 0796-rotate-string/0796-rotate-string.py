class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[0:i] == goal:
                print(f"new string = {s[i:] + s[0:i]}")
                return True
            print(f"new string = {s[i:] + s[0:i]}")

        return False
        
        