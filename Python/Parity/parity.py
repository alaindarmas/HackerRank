import time
import threading

class TimeoutException(Exception):
    pass

def timeout_handler():
    raise TimeoutException("Function timed out after 10 seconds")

def getLargestNumber(num):
    # Start the timer
    timer = threading.Timer(10, timeout_handler)
    timer.start()
    
    try:
        # Convert the string to a list of characters and reverse it
        str_array = list(num)[::-1]
        
        # Iterate through the array and swap adjacent elements if needed
        n = len(str_array)
        
        # Keep track of the last seen largest odd and even digits
        last_odd_index = -1
        last_even_index = -1
        
        for i in range(n - 1):
            current_digit = int(str_array[i])
            next_digit = int(str_array[i + 1])
            
            current_parity = current_digit % 2
            next_parity = next_digit % 2
            
            if current_parity == next_parity and current_digit < next_digit:
                # Perform the swap
                str_array[i], str_array[i + 1] = str_array[i + 1], str_array[i]
                
                # Update the last seen largest indices
                if current_parity == 0:  # even
                    last_even_index = i + 1
                else:  # odd
                    last_odd_index = i + 1
            
            # Update the last seen largest indices if necessary
            if current_parity == 0 and (last_even_index == -1 or current_digit > int(str_array[last_even_index])):
                last_even_index = i
            elif current_parity == 1 and (last_odd_index == -1 or current_digit > int(str_array[last_odd_index])):
                last_odd_index = i
        
        # Reverse the array back to its original order
        str_array = str_array[::-1]
        
        # Convert the list of characters back to a string
        final_string = ''.join(str_array)
        
    finally:
        timer.cancel()
    
    return final_string

if __name__ == "__main__":
    num = input()
    try:
        result = getLargestNumber(num)
        print("Largest number possible:", result)
    except TimeoutException as e:
        print(e)
