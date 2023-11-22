def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        middle = [pivot] * arr.count(pivot)
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + middle + quick_sort(greater)

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l = quick_sort(l)
hashtag = input()
n = int(input())

for _ in range(n):
    print(l[int(input())-1])

