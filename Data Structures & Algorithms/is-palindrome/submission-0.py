class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned = cleaned + ch.lower()
        return cleaned == cleaned[::-1]