class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            if dp[i] != float('inf'):
                for coin in coins:
                    if i + coin <= amount:
                        dp[i+coin] = min(dp[i+coin], dp[i] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
