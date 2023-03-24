A = [1, 2, 3, 1, 1, 1, 2, 3, 4, 0, 4, 4, 0, 5,
     5, 2, 1, 5, 6, 6, 7, 8, 8, 8, 9, 9, 9, 9, 9]

count = [0] * len(range(10))

for i in A:
    count[i] += 1
print(count)

# for i in range(10):
#     if count[i] > 0:
#         print((str(i) + " ") * count[i], end="")  # Сортировка
