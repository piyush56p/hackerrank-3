def plusMinus(arr):
    # Write your code here
    n = len(arr)
    count_zero = 0
    count_positive = 0
    count_negative = 0
    for i in range(n):
        if arr[i] > 0:
            count_positive +=1
        elif arr[i] < 0:
            count_negative += 1
        else:
            count_zero += 1
    a = ("{:.6f}".format(count_positive/n))
    b = ("{:.6f}".format(count_negative/n))
    c = ("{:.6f}".format(count_zero/n))
    print(a)
    print(b)
    print(c)
