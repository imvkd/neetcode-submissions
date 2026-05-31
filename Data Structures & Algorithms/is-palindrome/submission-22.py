class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        neutralised_string = ''
        for ch in s:
            if ch in an:
                neutralised_string += ch

        print(neutralised_string)
        neutralised_string = neutralised_string.lower()

        length = len(neutralised_string)
        i = 0
        j = length-1

        print(neutralised_string, i, j)

        while i<j:
            if neutralised_string[i] != neutralised_string[j]:
                return False
            i += 1
            j -= 1

        return True 