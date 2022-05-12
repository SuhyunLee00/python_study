# 1
a = 'a:b:c:d'
a = a.split(':')
a = "#".join(a)
print(a)

# 2
a = {'A': 90, 'b': 80}
a['C'] = 70
print(a)

# 3
a = [1, 2, 3]
# a.extend([4,5])
a = a + [4, 5]
print(a)
# 차이점 없다

# 4

A = [20, 50, 67, 82, 45, 33, 90, 87, 100, 25]
Sum = 0
for a in A:
    if a >= 50:
        Sum = Sum + a

print(Sum)

print(A[1] + A[2] + A[3] + A[6] + A[7] + A[8])
# 간단하게 하는 방법이 뭐가 있었죠?

# 5피보나치 함수??
# n=int(input())
first = 0
second = 1
third = first + second
print(first)
print(second)
n = 100
while n > third:
    print(third)
    first = second
    second = third
    third = first + second

# 6
# a = input()
# # a = 65, 45, 2, 3, 45, 8
# a = a.split(",")
# sumA = 0
# for b in a:
#     sumA = sumA + int(b)
# print(sumA)

# 7
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end='')
    print()
# 8
# AAA
# BBB
# CCC
# DDD
# EEE
f = open("새파일1.txt", 'r')
lines = f.readlines()
lines.reverse()
f.close()

f = open("새파일1.txt", 'w')
for line in lines:
    f.write(line)
f.close()
# reverse??

# 9
# 70 60 55 75 95 80 80 85 100
f = open("sample.txt", 'r')
lines = f.readlines()
f.close()

f = open("result.txt", 'w')
SumB = 0
for line in lines:
    SumB = SumB + int(line)

print(SumB)
f.write(str(SumB / len(lines)))
f.close()


class cal:
    def __init__(self, args):
        self.list = args

    def sum(self):
        return sum(self.list)

    def avg(self):
        return self.sum() / len(self.list)


cal1 = cal([1, 2, 3])
print(cal1.sum())
print(cal1.avg())
