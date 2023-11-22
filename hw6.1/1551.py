def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    
    return merge(left_list, right_list)


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list

n = int(input())

players = 2**n
prefectures = {}

for i in range(players):
    _, prefecture = input().split()
    prefectures[prefecture] = prefectures.get(prefecture, 0) + 1 #количество игроков из каждой префектуры

prefectures = merge_sort(list(prefectures.values()))

m = prefectures[-1] #максимальное число игроков из одной префектуры

for i in range(n):
    players //= 2
    #если в следующем раунде начальное число игроков из одной префектуры превышает
    #максимальное число игроков из одной префектуры, то возможен такой исход, 
    #что нельзя будет разделить игроков по разным префектурам
    if m  > players:
        print(i)
        break
else:
    print(n)
