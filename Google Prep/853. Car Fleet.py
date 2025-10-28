class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        d = dict()
        for i in range(n):
            d[position[i]] = speed[i]
        sorted_d = sorted(d.items(), reverse = True)
        fleets = []
        for pos, spe in sorted_d:
            time = (target - pos) / spe
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)