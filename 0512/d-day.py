# d-day
def d_date():
    year = int(input())
    month = int(input())
    day = int(input())
    a = []
    a.append(year)
    a.append(month)
    a.append(day)
    return a


def cal(a):
    y = a[0]
    x= a[1]
    w=a[2]
    while True:
        w=w+1
        if w=30:
            break



    return a


print()
date = d_date()

cal(date)
print(date[0], date[1], date[2])
