class Solution:
    def __init__(self):
        self.delimiter = '"'
        self.escape_char = "@"

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for i, string in enumerate(strs):
            encoded_list.append(self.delimiter)
            for char in string:
                if char == self.delimiter or char == self.escape_char:
                    encoded_list.append(self.escape_char)
                encoded_list.append(char)

            encoded_list.append(self.delimiter)

        # print("".join(encoded_list))
        return "".join(encoded_list)
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        idx = 0
        while idx < len(s):
            curr_char = s[idx]
            if curr_char != self.delimiter:
                raise ValueError("Wrong string passed")

            curr_word = []
            idx += 1
            while s[idx] != self.delimiter:
                curr_char = s[idx]
                if curr_char == self.escape_char:
                    idx += 1
                    curr_char = s[idx]
                curr_word.append(curr_char)
                idx += 1

            decoded_list.append("".join(curr_word))
            idx += 1

        return decoded_list
        
                



