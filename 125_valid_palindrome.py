class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        print(s)
        n = len(s)
        i=0
        j = n -1

        while(i < n/2):
            if(s[i]!=s[j]):
                return False
            i = i + 1
            j = j - 1

        return True   



s1 = Solution 
print(s1.isPalindrome(s1,"0P"))
