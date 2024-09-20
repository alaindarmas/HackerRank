def mutate_string(string, position, character):
    string1 = string
    l = list(string1)
    l[position] = character
    string1 = ''.join(l)

    return string1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)