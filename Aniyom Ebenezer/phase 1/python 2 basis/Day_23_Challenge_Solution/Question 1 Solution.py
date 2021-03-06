"""
Write a Python program that compute the maximum value of the sum of the passing integers according to the 
the rules.
"""
import sys
print("Input the numbers (ctr+d to exit): ")
x = [list(map(int, l.split(","))) for l in sys.stdin]
dp = x[0]

for i in range (1, (len(x)+1)//2):
    _dp = [0]*(i+1)
    for j in range(i):
        _dp[j] = max(_dp[j], dp[j]+x[i][j])
        _dp[j+1] = max(_dp[j+1], dp[j]+x[i][j+1])
    dp = _dp
for i in range((len(x)+1)//2, len(x)):
    _dp = [0]*(len(dp)-1)
    for j in range(len(_dp)):
        _dp[j] = max(dp[j], dp[j+1]) + x[i][j]
        dp = _dp
        print("Maximum value of the sumof integers passing according to the rule on one line.")
        print(dp[0])

#reference: w3resource
