# items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
# maxWeight = 5
# knapsack(items, maxWeight) = 22

class Solution:
    def knapsack(self, items, max_weight):
        """
        items type: List[tuple()]
        maxWeight type: int
        rtype: int

        returns the maxValue possible from putting items into knapsack without going over the maxWeight
        """
        max_value = 0
        cur_value = 0
        cur_weight = 0
        cur_bag = []
        for item in items:
            cur_weight += item[0]
            cur_value += item[1]
            cur_bag.append(item)
        print(cur_value)
        print(cur_weight)
        print(cur_bag)

        if cur_weight > max_weight:
            for idx in range(len(items)):
                self.elimination(items, max_weight, cur_weight, cur_value, cur_bag, idx)
        max_value = cur_weight
        return cur_weight

    def elimination(self, items, max_weight, cur_weight, cur_value, cur_bag, idx):
        if items[idx] in cur_bag:
            cur_bag.remove(items[idx])
            cur_weight -= items[idx][0]
            cur_value -= items[idx][1]
        else: 
            cur_value = float('-inf')
            return cur_value 


s = Solution()
items = [(1,6),(2,10),(3,12)]
print(s.knapsack(items,5))
