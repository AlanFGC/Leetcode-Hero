class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        res = s.split()
        res = " ".join(reversed(res))
        return res