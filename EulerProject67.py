tree = []
blank = []
with open('p67tree.txt') as f:
    for line in f:
        tree.append([int(v) for v in line.split()])
        blank.append([0 for v in line.split()])

#recursive function to check tree paths
#using memoization (learning it for this)
def reader(row,col):
    if row == len(tree)-1:
        return tree[row][col]
    if blank[row][col] == 0:
        blank[row][col] = max(reader(row+1,col),reader(row+1,col+1)) + tree[row][col]
    return blank[row][col]

a = reader(0,0)
print(a)
