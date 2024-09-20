def main():
    test_cases = int(input())

    for _ in range(test_cases):
        try:

            a, b = input().split()
            
            div_result = int(a) // int(b)
            print(div_result)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)

if __name__ == "__main__":
    main()