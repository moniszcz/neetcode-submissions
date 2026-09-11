class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output

    def decode(self, s: str) -> List[str]:
        outputs = []
        following_str_len = ""

        i = 0
        while i < len(s):
            if s[i] != "#":
                following_str_len += s[i]
                i += 1
            else:
                following_str_len_int = int(following_str_len)
                str_start_idx = i + 1
                str_end_idx = str_start_idx + following_str_len_int
                outputs.append(s[str_start_idx : str_end_idx])
                following_str_len = ""
                i = str_end_idx

        return outputs
