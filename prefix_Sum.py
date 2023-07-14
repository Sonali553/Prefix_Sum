#Prefix Sum
lst = list(map(int, input().split()))
def prefix_Sum(lst):
    for i in range(1, len(lst)):
        lst[i] = lst[i - 1] + lst[i]
    return lst
print(prefix_Sum([3, 6, 9, 2, 7]))
print(prefix_Sum([1, 2, 3, 4, 5]))
print(prefix_Sum([4, 3, 2]))
print(prefix_Sum([-1, -2, -3, 6, 9]))
print(prefix_Sum(lst))
