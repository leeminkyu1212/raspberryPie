

b = list(map(int, input().split()))
sum = 0
for i in range(len(b)):
    if (b[i] == 7):
        print("lucky")
    else:
        sum += b[i]

print(sum)
