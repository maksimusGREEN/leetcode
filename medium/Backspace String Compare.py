# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_char_index(string: str, index):
            skip = 0
            while index>=0:
                if string[index]=='#':
                    skip+=1
                elif skip>0:
                    skip-=1
                else:
                    return index
                index-=1
            return index

        pointer_s = len(s)-1
        pointer_t = len(t)-1
        while pointer_s>=0 or pointer_t>=0:
            pointer_s = get_next_char_index(s, pointer_s)
            pointer_t = get_next_char_index(t, pointer_t)
            if pointer_s<0 and pointer_t<0:
                return True
            if pointer_s<0 or pointer_t<0 or s[pointer_s]!=t[pointer_t]:
                return False
            pointer_s-=1
            pointer_t-=1
        
        return True
