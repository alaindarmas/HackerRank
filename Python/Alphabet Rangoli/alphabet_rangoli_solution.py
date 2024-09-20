def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    rows = []
    
    for i in range(size):    
        
        left = '-'.join(alpha[size-1:i:-1]) 
        right = '-'.join(alpha[i:size])
        row = left + '-' + right if left else right
        rows.append(row.center(4*size-3, '-'))
   
    print('\n'.join(rows[::-1] + rows[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)