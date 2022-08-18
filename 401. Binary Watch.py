class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for h in range(12):
            res.extend(
                "%d:%02d" % (h, m)
                for m in range(60)
                if (bin(h) + bin(m)).count('1') == turnedOn
            )

        return res