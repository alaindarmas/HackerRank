def print_formatted(number):
    max_width = len(bin(n)[2:])
    
    for i in range(1, n + 1):
        dec_num = i
        oct_num = oct(i)[2:]
        hex_num = hex(i)[2:].upper()
        bin_num = bin(i)[2:]
        
        print(f"{dec_num:>{max_width}} {oct_num:>{max_width}} {hex_num:>{max_width}} {bin_num:>{max_width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)