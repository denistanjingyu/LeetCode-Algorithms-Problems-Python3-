class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Return 0 if needle is an empty string
        if not needle:
            return 0

        # Return -1 if length of needle is longer than haystack (not possible to match)
        if len(needle) > len(haystack):
            return -1

        return next(
            (
                i
                for i in range(len(haystack) - len(needle) + 1)
                if haystack[i : i + len(needle)] == needle
            ),
            -1,
        )