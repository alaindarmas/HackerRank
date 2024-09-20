import re

def main():
    card_amt = int(input())
    pattern = r'^(?!.*(\d)\1{3})[456]\d{3}(-?\d{4}){3}$'
    
    for _ in range(card_amt):
        card_num = input()
        
        consecutive_flag = consecutive_nums(card_num)
        if consecutive_flag == True:
            print("Invalid")
            continue
    
        valid = bool(re.match(pattern, card_num))
        
        if valid == True:
            print("Valid")
        else:
            print("Invalid") 
            
def consecutive_nums(card_num):
    
    cleaned_string = ''.join(filter(str.isdigit, card_num))
    char_array = list(cleaned_string)
    
    for i in range(len(char_array) - 3):  # Subtract 3 to prevent index out of range
        if char_array[i] == char_array[i + 1] == char_array[i + 2] == char_array[i + 3]:
            return True
    return False
        
if __name__ == "__main__":
    main()
        
        
