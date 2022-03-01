class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic programming (bottom up approach)
        # Start from the (n-1)th step
        two_steps_before, one_step_before = 2, 1
        
        # Edge case: if 1 step only then only 1 way (climb 1 step)
        if n == 1:
            return 1
        
        # No. of choices at n = no. of choices at (n-1) + no. of choices at (n-2)
        for i in range(n-2):
            two_steps_before, one_step_before = two_steps_before + one_step_before, two_steps_before

        return two_steps_before
