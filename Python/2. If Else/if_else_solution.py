def main():

    N = int(input())

    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")
        
if __name__ == "__main__":
    main()
