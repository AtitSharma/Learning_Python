s='dvdf'
dp = []
max_len = 0
for i in s:
    if i in dp:
        dp=dp[dp.index(i)+1:]
        dp.append(i)
        
    else:
        dp.append(i)

    if len(dp)> max_len:
        max_len=len(dp)
print(max_len)

