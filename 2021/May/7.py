class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        max_phrase_length = 0
        for i in range(len(word1)):
            for j in range(len(word1)-i+1):
                phrase = word1[i:i+j]
                if phrase in word2 and len(phrase) > max_phrase_length:
                    max_phrase_length = len(phrase)

        return (len(word1) - max_phrase_length) + (len(word2) - max_phrase_length)





s = Solution()
print(s.minDistance("abc", "abc")) # same
print(s.minDistance("abc", "abcdef")) # delete from word2
print(s.minDistance("abcdef", "abc")) # delete from word1
print(s.minDistance("abcdef", "cdefgh")) # delete from both
print(s.minDistance("aaaaaa", "aa")) # same phrase include
print(s.minDistance("abcabcdefabcdefgh", "jjjabcdefghiii"))
