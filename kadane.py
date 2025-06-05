def maxSubArraySum(a, a_size):
    max_sum = -99999999999
    current_max = 0 

    for i in range(0, a_size):
        current_max = current_max + a[i]
        if max_sum < current_max:
            max_sum = current_max
        if current_max < 0:
            current_max = 0
        return max_sum

a = [1, 2, 3, -4, 5, -22, 4, 25, 2, -9]
print(maxSubArraySum(a, len(a)))
         