def print_set(set):
    print(len(set))
    print(*[str(item) for item in sorted(set)])


N, M = [int(s) for s in input().split()]
a_colors, b_colors = set(), set()
for i in range(N):
    a_colors.add(int(input()))
for i in range(M):
    b_colors.add(int(input()))

print_set(a_colors & b_colors)
print_set(a_colors - b_colors)
print_set(b_colors - a_colors)
