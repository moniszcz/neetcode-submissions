class Solution:

    def create_dict_from_string(self, string: str) -> dict:
        letters_dict = {}

        for letter in string:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
        
        return letters_dict

    def isAnagram(self, s: str, t: str) -> bool:
        first_string_dict = self.create_dict_from_string(s)
        second_string_dict = self.create_dict_from_string(t)

        return first_string_dict == second_string_dict



        