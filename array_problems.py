def reverse(a, a_size, n):
    temp = 0

    while temp < a_size:
        start = temp
        end = min(temp + n - 1, a_size - 1)

        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
            temp += n

            a = [5, 23, 5, 23, 1, 23, 5, 136, 7, 56]
a_size = len(a)
n = 2

reverse(a, a_size, n)
print("Array after reversing in groups of", n, ":", a)

