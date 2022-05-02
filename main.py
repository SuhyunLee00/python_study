# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import random

    # total money
    M = 1000000

    # beginning price of the stock
    S = 10000

    # total stock that I have
    TS = 0

    hour = 9
    minute = 30

    while hour < 16:
        E = random.uniform(1.1, 0.9)
        S = round(S * E)

        print(hour, " : ", minute)
        print(f'현재가격{S}')

        choice = input('buy or sell or skip ')

        if choice == 'buy':
            count = int(input('how many? '))
            # 사려고 하는게 총 얼만지 계산
            Totalprice = S * count
            # 그 가격이 지갑에 있는지 확인
            # 있다면 구매를 하고 없으면 다시 선택하게
            # 구매를 했다면 보유한 주식량이 변화
            if Totalprice <= M:
                M = M - Totalprice
                TS = TS + count
            else:
                continue


        elif choice == 'sell':
            count = int(input('how many? '))
            # 파려고한 총갯수가 지갑에 있는지
            # 있다면 몇 주를 팔건지
            # 없으면 패스
            # 팔고난 후의 주식 보유량
            # 지갑의 변화
            # 시세차이익*
            if TS >= count:
                TS = TS - count
                M = M + S * count
            else:
                continue


        elif choice == 'skip':
            pass
        else:

            pass

        minute += 30
        if minute == 60:
            hour += 1
            minute = 0

        print(f'총자산:{M}')
        print(f'보유주식량:{TS}')
        print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# mod2.py
def multi(a, b):
    return a * b


def div(a, b):
    return a / b
