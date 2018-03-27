from collections import Counter

while True:
    try:
        s = input().strip()
    except:
        break
    tmp = iter(s)

    print(next(tmp))
    print(next(tmp))
    print(next(tmp))

    tmp = zip(iter(s), tmp)

    counts = Counter(s)
    print(counts)
    killedMissionaries = 0
    skip = False
    for x, y in tmp:
        if x != y and not skip:
            killedMissionaries += 1
            skip = True
            continue
        skip = False

    counts['m'] -= killedMissionaries
    m, b = counts['m'], counts['c']
    if m == b:
        print('tie')
    elif m > b:
        print('missionaries')
    else:
        print('cannibals')