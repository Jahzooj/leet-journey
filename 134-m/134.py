class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        currgas = 0
        greedy = (10e5, -1)

        for i, g in enumerate(gas):
            c = cost[i]
            step = (g - c)

            currgas += step
            greedy = (currgas, i) if currgas < greedy[0] else greedy

        if currgas >= 0:
            return (greedy[1] + 1) % len(gas)
        return -1
