# Write python programm that convert given a roman numeral to an integer


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        result = 0
        for char in s:
            value = roman_dict[char]
            result += value

            if value>prev_value:
                result -= 2*prev_value
            prev_value=value
            
        return result