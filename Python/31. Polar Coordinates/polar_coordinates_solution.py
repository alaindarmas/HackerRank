# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase

complex_num = complex(input().strip())

print(abs(complex_num))
print(phase(complex_num))
