from collections import deque

if __name__ == "__main__":
    n = int(input())
    
    d = deque() 
    for _ in range(n):
        command = input()
        command = command.split()
        function_name = command[0]
        
        function = getattr(d, function_name)
        
        if len(command) > 1:
            arg = int(command[1])
            function(arg)
        else:
            function()
        
    print(" ".join(map(str, d)))
        
