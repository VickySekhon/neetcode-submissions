class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        longest = 0
        l, r = 0, 0
        
        while r < len(s):
              c = s[r]
              if c in window:
                while c in window:
                  window.pop(s[l])
                  l += 1
              else:
                window[c] = None
                if r-l+1 > longest: longest = r-l+1
                r += 1
        return longest
      