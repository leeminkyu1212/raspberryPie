# print(f"#{t} {max}")
# print("#"+str(t)+" "+str(max))
# 둘은 같다

T=int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    for i in range(len(matrix)):
        matrix[i] = list(map(int, input().split()))
    dir = [[0, 0], [0, 1], [1, 0], [1, 1]]
    max = -10000
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            num = 0
            for i in range(M):
                for j in range(M):
                    num+=matrix[row+i][col+j]
            if (num > max): max = num

    print(f"#{t} {max}")