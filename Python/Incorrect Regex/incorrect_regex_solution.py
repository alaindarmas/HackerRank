import re

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        regexPattern = input()
        regexValid = True
        
        try: 
            re.compile(regexPattern)
            print(regexValid)
        except re.error:
            regexValid = False
            print(regexValid)
            
        
