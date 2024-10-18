from collections import OrderedDict


if __name__ == "__main__":
    n = int(input())
    items_dict = OrderedDict()
    
    for x in range(n):
        input_str = input()
        parts = input_str.rsplit(' ', 1)

        item_name = parts[0]
        item_quantity = int(parts[1])
        
        if item_name in items_dict:
            items_dict[item_name] += item_quantity
        else:
            items_dict[item_name] = item_quantity
    
    for key, value in items_dict.items():
        print(f"{key} {value}")
        
        
        
        
    
