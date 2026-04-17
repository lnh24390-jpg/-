def solution(strs, t):
    # 매우 큰 값 (불가능 상태 표현)
    INF = float('inf')
    
    # dp[i] : t의 앞 i글자를 만들기 위한 최소 단어 개수
    dp = [INF] * (len(t) + 1)
    
    # 초기 상태 (아무 것도 사용하지 않음)
    dp[0] = 0

    # 빠른 탐색을 위해 set으로 변환
    word_set = set(strs)

    # 문자열 길이만큼 순회
    for i in range(1, len(t) + 1):
        
        # 단어 최대 길이가 5이므로 1~5만 확인
        for l in range(1, 6):
            if i - l < 0:
                continue
            
            # 현재 위치에서 끝나는 substring
            sub = t[i - l:i]
            
            # 해당 substring이 존재하면
            if sub in word_set:
                dp[i] = min(dp[i], dp[i - l] + 1)

    # 끝까지 만들 수 없는 경우
    return dp[len(t)] if dp[len(t)] != INF else -1
