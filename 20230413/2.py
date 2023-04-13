

a = int(input())

b = list(map(int, input().split()))

b[a] = "change"

for i in range(len(b)):
    print(b[i], end=" ")
