a = list(input().split())
a = [int(i) for i in a]
for i in range(int(len(a)/2)):
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
for i in a:
    print(i, end = " ")