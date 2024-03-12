
cs = [1, 2, 3, 4, 5, 6]

# cs = cs[0:int(len(cs)/2)] + cs[int(len(cs)/2):][::-1]

# print(cs)

# print('2. ford')

print()
print()
print()


print(cs)

round_numbers = len(cs)-1

for i in range(1, round_numbers+1):
    print(f'{i}. forduló')

    if i == 1:
        print(cs)
        
    else:
        cs = cs[0:int(len(cs)/2)] + cs[int(len(cs)/2):][::-1]
        cs.insert(1, cs[-1])
        cs=cs[0:len(cs)-1]
        print(cs)

    print()