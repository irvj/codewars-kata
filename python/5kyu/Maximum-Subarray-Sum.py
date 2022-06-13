"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""


def max_sequence(arr):
    if not len(arr):
        return 0
    elif len(arr):
        count = 0
        for i in arr:
            if i < 0:
                count += 1
        if len(arr) == count:
            return 0
    dummy_array = [0 for i in range(len(arr))]
    dummy_array[0] = arr[0]
    for i in range(1, len(arr)):
        dummy_array[i] = max(dummy_array[i-1] + arr[i], arr[i])
    return max(dummy_array)


"""
Better version of Kadane's Algo


https://www.codingninjas.com/blog/2020/09/17/a-quick-look-at-kadanes-algorithm/
Run in visualizer: http://www.pythontutor.com/visualize.html#mode=edit


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans
    
maxSequence(arr)


"""
