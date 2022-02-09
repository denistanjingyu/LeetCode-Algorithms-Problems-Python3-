class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Define a variable to check number of matched characters
        check = 0
        # Convert integer to string to access each character
        str_x = str(x)
        # Reverse the original string
        str_x_reverse = str_x[::-1]
        
        # Loop through and compare each corresponding character of both strings
        # Add 1 to check variable for each match
        for i in range(len(str_x)):
            if str_x[i] == str_x_reverse[i]:
                check += 1
        
        # If all characters match, value of check should equal length of string
        if check == len(str_x):
            return True
        else: 
            return False