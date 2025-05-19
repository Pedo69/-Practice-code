n1, n2, n3 = map(int, input('enter your numbers: ').split())
count_even = 0
count_odd = 0

for n in [n1, n2, n3]:
    if n % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f'Even count: {count_even}')
print(f'Odd count: {count_odd}')