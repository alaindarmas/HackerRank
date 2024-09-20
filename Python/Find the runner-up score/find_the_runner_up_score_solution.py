if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    c = []
    b=sorted(arr)
    for x in b:
        if x not in c:
            c.append(x)
    print(c[len(c)-2])