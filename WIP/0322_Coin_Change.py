from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        """
        For a given set of coin denomations, return the smallest number of coins that can be used to add up to a given target amount.
        coins type: List[int]
        amount type: int
        rtype: int
        """
        if amount == 0:
            return 0

        levels = {1: []}
        visited = set()
        cur_level = 1
        found = False

        for c in coins:
            levels[1].append(c)
        # print(levels)

        while found == False:
            for item in levels[cur_level]:
                if item in visited:
                    continue
                if item == amount:
                    return cur_level
                elif item > amount:
                    continue
                else:
                    if (cur_level + 1) not in levels:
                        levels[cur_level+1] = []
                    for c in coins:
                        levels[cur_level+1].append(item + c)
                    print(levels)
                visited.add(item)
                print
            cur_level += 1
            if cur_level not in levels:
                return -1


s = Solution()
# print(s.coinChange([1],2)) # 2
# print(s.coinChange([2],1)) # -1
# print(s.coinChange([2],3)) # -1
# print(s.coinChange([2,3],4)) # 2
print(s.coinChange([1,2,5],11)) # 3
# print(s.coinChange([2, 5, 10, 1],27)) # 4
# print(s.coinChange([1,2,5],100))  # 20
# print(s.coinChange([431,62,88,428],9084))  # 26
# [0,0,0, 1,-1]
# [0,0,1,-1,2]
#  0 1 2  3 4
