class Solution:
    def isValid(self, s: str) -> bool:
        
        # Dict mapping the correct open and close brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Valid if string is empty as no chance for mismatch
        if len(s) == 0:
            return True
        
        # Invalid if string length is not even (not possible to match 1 to 1)
        if len(s) % 2 == 1:
            return False
        
        # Create a stack to store single or continuous left brackets
        stack = []
        
        # Loop through each character 
        for char in s:

            
            # Add left bracket to stack
            if char in mapping.values():
                stack.append(char)
            # Check right bracket with valid left bracket
            # Empty stack means no left match
            # Check if right bracket match last left bracket in stack
            else:
                if stack == [] or mapping[char] != stack.pop():
                    return False
        
        # Check if final stack is empty
        # If it contains a left bracket means no possible right match
        return stack == []