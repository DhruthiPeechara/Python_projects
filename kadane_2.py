def kadane(a):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
         return max_so_far
    
def maxCircularSum(a):
    n = len(a)
    max_kadane = kadane(a)
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
        a[i] = -a[i]
     max_wrap = total_sum + kadane(a)

    if max_wrap == 0:
        return max_kadane
    else:
        return max(max_wrap, max_kadane)
    
a = [8, -1, 3, 4]
print("Maximum circular subarray sum is:", maxCircularSum(a))