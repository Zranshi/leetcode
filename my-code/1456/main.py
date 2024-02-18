class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aoeiu"
        left, right, idx_num = 0, k, 0
        for ch in s[left:right]:
            if ch in vowel:
                idx_num += 1
        max_num = idx_num
        while right < len(s):
            if s[left] in vowel:
                idx_num -= 1
            if s[right] in vowel:
                idx_num += 1
            left, right = left + 1, right + 1
            max_num = max(max_num, idx_num)
        return max_num


print(Solution().maxVowels(s="aeiou", k=2))
