def average(array):
    
    unique_list = list(set(array))
    item_sum = 0
    arr_size = len(unique_list)
    for item in unique_list:
        item_sum = item + item_sum
        
    mean = item_sum / arr_size
    mean = round(mean, 3)
    
    return mean



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)