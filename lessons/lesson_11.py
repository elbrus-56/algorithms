# Наибольшая общая подпоследовательность

"""
A,B - массивы чисел
Подпоследовательность - это массив С, содержащий элементы А в исходном
 порядке, но, возможно, не все.
len(A) == N
len(B) == M

F(i,j) - длина наибольшей возможной подпоследовательнсоти частей A и B
A[0:i] и B[0:j]
"""


def lcs(A, B):
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]


print(lcs([1, 3, 4, 7, 6, 7, 7, 5], [2, 3, 4, 5, 6, 8, 9, 0]))


# Наибольшая возрастающая подпоследовательность


def gis(A):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        m = 0
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]


print(gis([1, 2, 3, 4, 5, 6]))

# def gis_1(A):
#     F = [0] * (len(A))
#     for i in range(0, len(A)):
#         F[i] = 1
#         for j in range(0, i):
#             if A[j] < A[i] and F[j] + 1 > F[i]:
#                 F[i] = F[j] + 1
#     ans = 0
#     for i in range(0, len(A)):
#         ans = max(ans, F[i])
#     return ans

# print(gis_1([0,1,1,2,3,4,3,2]))
