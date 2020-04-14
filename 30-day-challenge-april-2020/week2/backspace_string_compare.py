"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

"""

class Solution:
    def modify_str(self, S: str) -> str:
        new_s = ''
        for c in S:
            if c == '#':
                new_s = new_s[:-1]
            else:
                new_s += c
        return new_s

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.modify_str(S) == self.modify_str(T)
