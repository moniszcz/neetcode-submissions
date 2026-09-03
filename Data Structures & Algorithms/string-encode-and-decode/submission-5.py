class Solution:
    

    def encode(self, strs: List[str]) -> str:
        special_char = "#"
        output_string = ""
        for s in strs:
            s_len = str(len(s))
            output_string += s_len + special_char + s

        return output_string

    def decode(self, s: str) -> List[str]:
        special_char = "#"
        output_list = []
        i = 0
        while(i < len(s)):
            for j in range(i + 1, len(s)):
                if s[j] == special_char:
                    curr_string_length = int(s[i: j])
                    break
            curr_string_first_index = i + 1 + len(s[i: j])
            curr_last_index = curr_string_first_index + curr_string_length
            output_list.append(s[curr_string_first_index:curr_last_index])
            i = curr_last_index
        return output_list