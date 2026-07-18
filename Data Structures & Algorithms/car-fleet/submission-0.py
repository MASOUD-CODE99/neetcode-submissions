class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        q = [[position[i], speed[i]] for i in range(len(speed))]
        q.sort(key=lambda x: x[0], reverse=True)  
        res = []

        for i in range(len(speed)):
            res.append((target - q[i][0]) / q[i][1])

        f = res[0]
        fleets = 1

        for t in res[1:]:
            if t > f:
                fleets += 1
                f = t

        return fleets
