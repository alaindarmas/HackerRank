from itertools import permutations

s,k = input().split()
k = int(k)

for i in sorted(list(permutations(s,k))):
    print("".join(i))

