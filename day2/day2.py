fin = 'day2.in'
op = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

score = 0
with open(fin, 'r') as f:
    for line in f.readlines():
        left = line.split(' ')[0]
        right = line.split(' ')[1].strip()
        score += me.index(right)
        result = (me.index(right) - op.index(left)) % 3
        if result == 1:
            # You win
            score += 6
        elif result == 0:
            # Draw
            score += 3

print(score)