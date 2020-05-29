# 0053. Maximum Subarray

## 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray\(containing at least one number\) which has the largest sum and return its sum.

```text
Example:

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
Follow up:
```

> If you have figured out the O\(n\) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## One Pointer Approach - @shichunyu on May 29, 2020

**Runtime:** O\(N\) because we traverse the array once only. **Space:** O\(1\) because we only use a pointer and store values in variables.

### Intuition

* The contiguous subarray cannot start with a negative number, or end with a negative number
* When the subarray includes more than one element, the value of the subarray is the same as if those elements are "merged". For example, \[-2,1,-3\] has same value as \[-1,-3\]
* Based on above insights, we can think of our subarray as starting from the left, and expanding toward the right. We must follow the following rules to get the largest possible value:
  * Keep track of the max\_val, with max\_val initialized as -inf
  * Initialize a start and an end pointer to start traversing the array, starting at index = 0.
  * Initialize a cur\_val variable to keep track of the value of our subarray
  * Note we do not actually need to initialize an array to store the subarray. This helps reduce our space complexity from O\(N\) -&gt; O\(1\)
  * If the start is a negative number, then the subarray can only be of size one.
    * update cur\_val = element value
    * choose max\_val = max\(cur\_val, max\_val\)
    * move start & end pointer over by 1
  * If the start is a positive number, add the value to our cur\_val. Update max\_val = max\(cur\_val, max\_val\)
  * Move end pointer to the next element, do we include it in the subarray?
    * If element is positive, include it. Update cur\_val += element value
    * If element is negative:
      * If element is smaller than the sum of previous values in subarray \(which is effectively cur\_val\), include it. Update cur\_val += element value
      * But if the element is larger than the sum of the previous values in subarray, do NOT include it, and end or "close" the subarray there.
        * Example: \[2,5,-1\] Include -1 in the subarray. This subarray is same value as: \[7,-1\] and \[6\]
        * Example: \[3,1,-10\] Do NOT include -10 in the subarray, as the result will be negative. This subarrayis the same value as \[4,-10\] or \[-6\]
  * When the subarray has "closed" then it's time to start a new subarray, and we clear cur\_val.
  * Do this until we reach the end of the array
  * Return max\_val

```python
class Solution:
    def maxSubArray(self, array):
        """
        Finds the largest sum possible for a contingous subarray of input array
        array type: list[]
        rtype: int
        """
        max_val = float('-inf')
        cur_val = 0
        for element in array:
            # current element is neg
            if element <= 0:
                # previous subarray was negative, so start a new subarray by clearing cur_val to 0
                if cur_val <= 0:
                    cur_val = 0
                # since cur element is negative, we need to check if adding it to the subarray will result in a negative number. If yes, is the value value at least greater than our max_val?
                # "element + cur_val <= 0" checks whether we are adding the negative number to subarray will keep subarray positivie. 
                # Ex 1: [8,-3] Yes - the net result is positive, so skip this and do NOT start a new subarray.
                # Ex 2: [-3] No - the net result is negative. So we want to consider whether looking at this element by itself is still greater than the max_val. In this case -3 > -inf
                if element + cur_val <= 0 and element + cur_val < max_val:
                    # In this case it is not, so start a new subarray by clearing cur_val
                    cur_val = 0
                    continue
                else:
                    cur_val += element
                    max_val = max(cur_val,max_val)
            # current element is positive
            else:
                # If the previous subarray was a single negative number, so start a new subarray by clearing cur_val to 0
                if cur_val > 0:
                    cur_val += element
                else:
                    cur_val = element
                max_val = max(cur_val, max_val)
        return max_val

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(s.maxSubArray([-4])) # -4
print(s.maxSubArray([0])) # 0
print(s.maxSubArray([0,3])) # 3
print(s.maxSubArray([10,3])) # 13
print(s.maxSubArray([-10,-3,0,-5])) # -0
print(s.maxSubArray([-10,-3,-5])) # -3
print(s.maxSubArray([-2,1])) # 1
print(s.maxSubArray([])) # -inf
```

