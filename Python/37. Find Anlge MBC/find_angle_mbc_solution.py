from math import degrees, atan2

if __name__ == "__main__":
    ab = float(input())
    bc = float(input())

    mbc = round(degrees(atan2(ab, bc)))
    print((str(mbc)), chr(176), sep='')
