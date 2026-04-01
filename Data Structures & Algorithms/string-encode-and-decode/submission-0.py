class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for item in strs:
            encoded_str += str(len(item)) + "#" + item

        return encoded_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i: j])
            res.append(s[ j+1 : j + 1 + word_len])
            i = j + 1 + word_len
        return res

                
