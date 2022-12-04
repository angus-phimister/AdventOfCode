with open("2022/Day4/input.txt") as f:
    input = f.read().split('\n')
    input = [pair.split(',') for pair in input]


nsubs = 0
for pair in input:
    elf1 = [int(num) for num in pair[0].split('-')]
    elf2 = [int(num) for num in pair[1].split('-')]

    print(f'Elf 1: {elf1}')
    print(f'Elf 2: {elf2}')

    if (elf1[0] >= elf2[0]) & (elf1[1] <= elf2[1]):
        nsubs += 1
        print('im in')
        continue

    if (elf2[0] >= elf1[0]) & (elf2[1] <= elf1[1]):
        nsubs += 1
        print('im in')
        continue

print(nsubs)
