if __name__ == "__main__":
    
    n = int(input()) 
    inputSet = {int(item) for item in input().split()}
    commands = int(input())
    
    for _ in range(commands):
        command = input().split()
        textCommand = command[0] 
        
        if textCommand == 'pop':
            if inputSet:  
                
                sorted_list = sorted(inputSet)
                first_element = sorted_list[0]
                inputSet.remove(first_element)  
        elif len(command) > 1: 
            byWhat = int(command[1]) 
            
            
            if textCommand == 'remove':
                try:
                    inputSet.remove(byWhat)  
                except KeyError:
                    pass  
            elif textCommand == 'discard':
                inputSet.discard(byWhat)  
    
    print(sum(inputSet))
