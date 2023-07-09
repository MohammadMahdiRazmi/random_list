import random

my_list = [random.randint(1, 100) for _ in range(10)]

print("list not sorted:", my_list)


n = len(my_list)
for i in range(n - 1):
    max_idx = i
    for j in range(i + 1, n):
        if my_list[j] < my_list[max_idx]:
            max_idx = j
    my_list[i], my_list[max_idx] = my_list[max_idx], my_list[i]


print("list sorted:", my_list)
