emo_list=[2,1,2,1,2]

n=5

# 动态规划
dp=[0]*n
dp[0]=emo_list[0]
dp[1]=emo_list[1]
dp[2]=emo_list[0]+emo_list[2]
for index in range(3,n):
    dp[index]=max(dp[index-2]+emo_list[index],dp[index-3]+emo_list[index])

print(max(dp))