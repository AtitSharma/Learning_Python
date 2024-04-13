s = "leetcode"

for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
# return -1 if not valid
    