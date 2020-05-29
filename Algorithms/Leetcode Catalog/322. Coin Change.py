"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

Accepted
"""

[1,5], 7

[1,5]

minCoins = 7
numCoins = 1 + recMC([1,5],6)  -> return: 2 // numCoins = 3 // minCoins = 3
    numCoins = 1 + recMC([1,5], 5) -> return: 1 // numCoins = 2 // minCoins = 2
        5 is in coinValuelist: return 1


class Solution:
    def coinChange(self, coinValueList, change, knownResults):

class Solution:
    def coinChange(self, coins, amount):
        self.minCoins = float('inf')
        self.memo = [float('inf')]*amount
        self.brute(coins,0,0,amount)
        if self.minCoins == float('inf'):
            return -1
        return self.minCoins

    def brute(self,coins,curAmount,numCoins,target):
        if curAmount >= target:
            if curAmount == target:
                self.minCoins = min(self.minCoins, numCoins)
                return numCoins
            return float('inf')

        if self.memo[curAmount] <= numCoins:
            return self.memo[curAmount]
        
        smallest = float('inf')
        for coin in coins:
            smallest = min(smallest, self.brute(coins, curAmount, numCoins+1, target))

        memo[curAmount] = smallest
        return smallests

s = Solution()
print(s.coinChange([1,2,5],11))
