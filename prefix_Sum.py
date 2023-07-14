#Prefix Sum
lst = list(map(int, input().split()))
prefix_sum = lst
def prefix_Sum(lst):
    prefix_sum = lst
    prefix_sum[0] = lst[0]
    for i in range(1, len(lst)):
        prefix_sum[i] = prefix_sum[i - 1] + lst[i]
    return prefix_sum
print(prefix_Sum([3, 6, 9, 2, 7]))
print(prefix_Sum([1, 2, 3, 4, 5]))
print(prefix_Sum([-1, -2, -3, 6, 9]))
print(prefix_Sum([4, 3, 2]))
print(prefix_Sum(lst))
