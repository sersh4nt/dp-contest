n = int(input())
l = [input().strip() for i in range(n)]
dp = []
for i in range(26):
    dp.append([-999999999] * 26)
ans = 0
for i in range(26):
    dp[i][i] = 0
    for j in range(n):
        first = ord(l[j][0]) - 97
        ln = len(l[j])
        last = ord(l[j][ln - 1]) - 97
        dp[i][last] = max(dp[i][last], dp[i][first] + ln)
    ans = max(ans, dp[i][i])
print(ans)