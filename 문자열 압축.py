
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
def solution(s):
    # 문자열 길이가 1이면 압축 불가능 → 그대로 반환
    if len(s) == 1:
        return 1

    answer = len(s)  # 최악의 경우 (압축 안 되는 경우)

    # -----------------------------------
    # 1. 자르는 단위 (1 ~ len(s)//2)
    # -----------------------------------
    for step in range(1, len(s)//2 + 1):

        compressed = ""  # 압축 결과 문자열
        prev = s[0:step]  # 이전 문자열 블록
        count = 1  # 반복 횟수

        # -----------------------------------
        # 2. step 단위로 문자열 순회
        # -----------------------------------
        for i in range(step, len(s), step):
            current = s[i:i+step]

            # 이전 블록과 같으면 카운트 증가
            if prev == current:
                count += 1

            else:
                # 다르면 지금까지 결과 압축
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev

                # 새로운 블록 시작
                prev = current
                count = 1

        # -----------------------------------
        # 3. 마지막 블록 처리
        # -----------------------------------
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        # -----------------------------------
        # 4. 최소 길이 갱신
        # -----------------------------------
        answer = min(answer, len(compressed))

    return answer
