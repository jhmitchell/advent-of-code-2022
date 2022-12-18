fin = 'day1.in'
cur = 0
maxcals = [0]*3

with open(fin, 'r') as f:
    for line in f.readlines():
        if line == '\n':
            mincal = min(maxcals)
            mincalidx = maxcals.index(mincal)
            newcal = max(mincal, cur)
            maxcals[mincalidx] = newcal
            cur = 0
        else:
            cur += int(line)

result = 0
for cals in maxcals:
    result += cals

print(result)