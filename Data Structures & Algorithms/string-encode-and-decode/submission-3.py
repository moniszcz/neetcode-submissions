class Solution:

    def encode(self, strs: List[str]) -> str:
        special_char = "#"
        output_string = ""
        for s in strs:
            s_len = str(len(s))
            output_string += special_char + s_len + special_char + s

        return output_string

    def decode(self, s: str) -> List[str]:
        special_token = "#"
        output_list = []
        i = 0
        while(i <= len(s) - 1):
            curr_char = s[i]
            next_char = s[i+1]
            if curr_char == special_token:
                for j in range(i + 2, len(s)):
                    if s[j] == special_token:
                        string_length = int(s[i+1: j])
                        break
                curr_string_first_index = i + 2 + len(s[i+1: j])
                last_index = curr_string_first_index + string_length
                output_list.append(s[curr_string_first_index:last_index])
                i = last_index
            else:
                return output_list
        return output_list



