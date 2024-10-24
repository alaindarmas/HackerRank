from itertools import groupby

if __name__ == "__main__":
    string = input()
    
    result = [(len(list(group)), int(key)) for key, group in groupby(string)]

    print(*result)
    
        
    
