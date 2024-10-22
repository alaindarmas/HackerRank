#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    
    char_array = list(s)
    
    char_dict = dict()
    
    for item in char_array:
        
        if item in char_dict:
            char_dict[item] += 1
        else:
            char_dict[item] = 1
            
    sorted_dict_desc = dict(sorted(char_dict.items(), key=lambda item: (-item[1], item[0])))
    
    first_three_items = list(sorted_dict_desc.items())[:3]
    
    for key, value in first_three_items:
        print(f"{key} {value}")
    
    
    
        

    
    