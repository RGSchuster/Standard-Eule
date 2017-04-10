tree = []
with open('p18tree.txt') as f:
    for line in f:
        tree.append([int(v) for v in line.split()])

#program enter here
def reader(row,col):
    if row == len(tree)-1:
        return tree[row][col]
    return max(reader(row+1,col),reader(row+1,col+1)) + tree[row][col]

a = reader(0,0)
print(a)
