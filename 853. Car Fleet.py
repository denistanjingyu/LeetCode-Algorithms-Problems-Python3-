class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        counter = 0
        sorted_pair = sorted([[p, s] for p, s in zip(position, speed)])[::-1]
        curr_fastest_time = 0

        for p, s in sorted_pair:
            if (target - p) / s > curr_fastest_time:
                counter += 1
                curr_fastest_time = (target - p) / s
        
        return counter