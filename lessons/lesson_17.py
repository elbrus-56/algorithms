# Задача о рюкзаке ( NP полная задача - класс задач)


F = [[0]*(N+1) for i in range(M+1)]

for i in range(1, N+1):
    for k in range(1, M+1):
        if m[i] <= k:
            F[k][i] = max(F[k][i-1], v[i] + F[k-m[i]][i-1])
        else:
            F[k][i] = F[k][i-1]

F[M][N]


# Задача о рюкзаке и предметами с массой

dp[0][0] = True
for i in range(1, n + 1):
    for j in range(0, W + 1):
        dp[i][j] = dp[i - 1][j]
        if a[i] <= j and dp[i - 1][j - a[i]]:
            dp[i][j] = True


# Задача о рюкзаке и предматами с массой и стоимостью

