a, b, c = map(int, input().split())

if (a == b == c):
    print("모두 같다")
elif (a != b and b != c and a != c):
    print("모두 다르다")
else:
    print("일부 같다")
