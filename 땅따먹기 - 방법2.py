def solution(land):
    for i in range(1, len(land)):
        prev = land[i-1]
        
        # 최댓값과 두 번째 최댓값 찾기
        max1 = max(prev)
        idx = prev.index(max1)
        
        # 두 번째 최대값
        max2 = max(prev[:idx] + prev[idx+1:])
        
        for j in range(4):
            if j == idx:
                land[i][j] += max2
            else:
                land[i][j] += max1
    
    return max(land[-1])
