from collections import Counter


def main():
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())

    inventory = Counter(shoe_sizes)

    earnings = 0

    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        if inventory[size] > 0:
            earnings = earnings + price
            inventory[size] -= 1

    print(earnings)
    
if __name__ == "__main__":
    main()
