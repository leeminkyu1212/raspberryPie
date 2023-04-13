# import sys
#
# a = 5
#
# b = "123"
#
# b = 5
#
# # 배열은 중괄호로
# c = [123, 456]
#
# # 자료형 에 주의해야한다
# f = 100 / 3
#
# # //는 c++의 /와 같다
# g = 100 // 3
# #
# print(f)
# # 33.333333333333336
# print(g)
# # 33
#
#
# # N**2=>n의 제곱
# N = 10 ** 2;
# # 100
#
#
# k = 3.527
# print(round(k, 2) <= (7 / 2))
# print(round(k, 2))
#
# print(1 < 5 < 10)
# print(1 > 5 < 10)
#
# j = [1, 2, 3, 1]
# j2 = (1, 2, 3, 1)
#
# print(j)
# print(j2)
# # 리스트와 튜플 차이: 요소 변경 유무
#
#
# k2 = {"123": 456, "789": 123}
#
# print(k2["123"])
# #
#
# y = list(range(5))
# print(list(y))
# y2 = [10, 5, 4, 1, 2]
# for i in y2:
#     print(i)
#
# print(type(a))
# # sys.stdin.readline()
#
#
# nums= input().split()
# print(nums)
#
#
#
# # 리스트로 입력 받자
# nums2=list(map(int,input().split()))
#
# print(nums2)
#
#
# # 1부터 10까지 숫자를 list에 등ㄺ
# a3=[]
# # for i in range(1,11):
# #     a3.append(i)
# a3=[i for i in range(1,11)]
# print(a3)

#
# a = int(input())
# b = list(map(int, input().split()))
# for _ in range(10):
#     print(7)
#
# print("test")
#
# k = int(input())
# if (k != 7):
#     print("good")
# else:
#     print("NO")
#
# for i in range(10, 0, -1):
#     print(i,end=' ')
# for i in range(1, 11, 1):
#     print(i,end=' ')

# m, l = list(map(int, input().split()))
# cmp = 1
# #
# # • 숫자 2개 입력 (a, b)
# # • a ~ b 까지 증가 방향으로 출력
# # • 만약 a가 더 크면 a ~ b까지 감소 방향 출력
# if (m < l):
#
#     cmp = 1
# else:
#     cmp = -1
# for i in range(m, l+cmp, cmp):
#     print(i)

# k = []
# k.append('A')
# k.append('B')
# k.append(150)
# k.append('D')
# for i in range(len(k) - 1, -1, -1):
#     if (i == 0):
#         print(k[i])
#     else:
#         print(k[i], end='-')
#
# print(k[-1])


for i in range(3, 11):
    print(i, end=" ")
print()
for i in range(10, 2, -1):
    print(i, end=" ")
print()

for i in range(2, 18, 2):
    print(i, end=" ")
print()

for i in range(15, 0, -3):
    print(i, end=" ")

a = [4, 2, 5, 1, 6, 3, 4]

for i in range(len(a)):
    print(a[i], end="")
print()
for i in range(len(a)):
    if (a[i] % 2 == 1):
        print(a)

a = {
    "MC": {
        "ABC": 3,
        "BBQ": 5
    },
    "kfc": [
        [5, 3, 4],
        [7, 9]
    ],
    "BTS": [53, "BT", "119"]
}
