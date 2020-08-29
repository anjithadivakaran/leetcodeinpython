class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0 
        left = 0 # Left index of array
        seen = {}  # Maintain a dictionary seen which has the latest index of a elem that has appeared before
        right = 0  # Right index of the array
        while right < len(s) and left < len(s):
            if s[right] not in seen:  # Add new elems to the seen dictionary
                seen[s[right]] = right
            else:
                if seen[s[right]] >= left: # Move the left pointer if a seen elem is in our window
                    left = seen[s[right]] + 1
                    
            result = max(result, right-left+1)
            seen[s[right]] = right        
            right += 1

        return result