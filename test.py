def solution(grid):
    a = "@"*(len(grid[0])+2)
    grid.insert(0, a)
    grid.append(a)
    for i in range(1, len(grid)-1):
        grid[i] = "@" + grid[i] + "@"
    
    for i in range(1, len(grid)-1):
        temp = list(grid[i])
        for j in range(1, len(temp)-1):
            if temp[j] == "#":
                if temp
        
grid = [".#.", "#..", ".#."]

# 1번 문제 : 당첨 확률이 제일 높은 복권 고르기 (확률이 같다면 당첨금액이 높은 것으로 산다.)
print(solution(grid))
def solution(lotteries):
    max_p = lotteries[0][0] / (lotteries[0][1]+1)
    max_p_index = 0
    if max_p >= 1:
        max_p = 1
    for i in range(1, len(lotteries)):
        temp = lotteries[i][0] / (lotteries[i][1]+1)
        if temp > max_p:
            max_p = temp
            max_p_index = i
        elif temp == max_p:
            if lotteries[i][2] > lotteries[max_p_index][2]:
                max_p = temp
                max_p_index = i


    answer = (max_p_index+1)
    return answer

[[1,0,3,1,1], [1,0,1]] 
[1, 0]