if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b +     c != n ])

    # abc one for each index in what you are putting, , then loop x to put it in a
    # loop y to put it in b
    # loop z to put it in c
