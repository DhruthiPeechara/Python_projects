def arrayMean(arr, arr_size):
    total_sum = 0
    for i in range(0, arr_size):
         total_sum += arr[i]
    return float(total_sum / arr_size)

def arrayMedian(arr, arr_size):
     arr.sort()

    if arr_size % 2 != 0:
        return float(arr[arr_size // 2])
    else:
       mid1 = arr[(arr_size - 1) // 2]
        mid2 = arr[arr_size // 2]
        return float((mid1 + mid2) / 2.0)

arr = [1, 4, 5.2, 5.8, 5.2, 6, 8]
arr_size = len(arr)

print("Mean =", arrayMean(arr, arr_size))
print("Median =", arrayMedian(arr, arr_size))

     
            

