class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary to store roman numerals and their respective values
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Define a variable to store the integer
        integer = 0

        # Loop through s till second last character
        # For each character, compare to next character (minus if less, add if more)
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                integer -= roman[s[i]]
            else:
                integer += roman[s[i]]

        # Last character is always added as it can never be less than non-existent "next"
        return integer + roman[s[-1]]