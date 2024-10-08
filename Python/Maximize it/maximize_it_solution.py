import itertools

def main():
    k, m = map(int, input().split())

    list_nest = []
    for _ in range(k):
           
        data = list(map(int, input().strip().split()))
          
        list_a = [x**2 for x in data[1:]]  
        
        list_nest.append(list_a)
        
    max_value = 0
    
    combinations = list(itertools.product(*list_nest))
    
    for combination in combinations:
        total_sum = sum(combination) % m
        if total_sum > max_value:
            max_value = total_sum
            
    print (max_value)
    
    
    
if __name__ == "__main__":
    main()
            
    
