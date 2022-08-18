class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # To store decimal values of a and b
        a_dec, b_dec = 0, 0

        # To store current binary multiplication value
        bin_mul_factor_a, bin_mul_factor_b  = 1, 1

        # To store binary result in string
        result = ""

        # Start from the last digit
        # Convert char digit to integer digit
        # Add decimal value to a_dec by converting the smallest binary digit on the right
        # Multiply bin_mul_factor_a by 2 for the next bigger bin to dec conversion
        for digit in a[::-1]:
            digit = int(digit)
            a_dec += (digit * bin_mul_factor_a)
            bin_mul_factor_a *= 2

        # Same as above for loop but for b
        for digit in b[::-1]:
            digit = int(digit)
            b_dec += (digit * bin_mul_factor_b)
            bin_mul_factor_b *= 2

        # Add both decimals together
        sum = a_dec + b_dec

        # Return a ("0") if sum is 0
        # As there are no leading zeros, sum can't be negative
        # Both a and b must be "0" for sum to be 0
        # Thus, can return either a or b
        if sum == 0:
            return a

        # Repeatedly divide sum by 2 and add the modulus to result string
        # Start adding the modulus from the back and move to the left
        while sum > 0:
            bin_digit = sum % 2
            result = str(bin_digit) + result
            sum = sum // 2

        return result