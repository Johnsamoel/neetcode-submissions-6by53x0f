class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_map = {}

        for word in strs:
           anagram =  "".join(sorted(word))
           if anagram in words_map:
               words_map[anagram].append(word)
           else:
               words_map[anagram] = [word]

        return list(words_map.values())