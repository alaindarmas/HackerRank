def count_substring(string, sub_string):
    counter = 0
    
    while(string.find(sub_string) != -1):
        counter = counter + 1
        x = string.find(sub_string)
        string = string[x + 1:]
    return counter



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)