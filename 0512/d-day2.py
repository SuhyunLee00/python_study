# d-day
import datetime


#
# today = datetime.date.today()
#
# christmas = datetime.date(2022, 12, 25)
#
# d_day = christmas - today
# print(d_day)


class d_day:
    def __init__(self, y, m, d):
        self.today = datetime.date.today()
        self.day = datetime.date(y, m, d)

    def Cal(self):
        return self.day - self.today


y = int(input('y'))
m = int(input('m'))
d = int(input('d'))
day = d_day(y, m, d)

print(day.Cal())
