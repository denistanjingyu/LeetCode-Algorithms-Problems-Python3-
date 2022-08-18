class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert integer to string to access each character
        str_x = str(x)
        # Reverse the original string
        str_x_reverse = str_x[::-1]

        check = sum(str_x[i] == str_x_reverse[i] for i in range(len(str_x)))
        # If all characters match, value of check should equal length of string
        return check == len(str_x)