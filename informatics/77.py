n = int(input())

tree = {}

for _ in range(1, n):
    line = input()
    c, pt = line.split()
    tree[c] = p

all_man = set(tree.keys()) | set(tree.values())

h = {}


def f(name):
    if name not in tree:
        h[name] = 0
        return 0
    p = tree[name]
    if p in h:
        value = h[p] + 1
    else:
        value = f(p) + 1
    h[name] = value
    return value


for name in all_man:
    if name not in h:
        f(name)

for name in sorted(h):
    print(name, h[name])