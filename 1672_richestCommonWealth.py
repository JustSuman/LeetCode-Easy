class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth = 0
        maxWealth = 0
        for i in accounts:
            for j in i:
                wealth += j
            if maxWealth<wealth:
                maxWealth = wealth
                wealth = 0
            else:
                maxWealth = maxWealth
                wealth = 0
        return maxWealth