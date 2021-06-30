a = list(input().split())
a = [int(i) for i in a]
for i in range(len(a)):
    if a[i] != 0:
        print(a[i], end=" ")
for i in range(a.count(0)):
    print(0, end=" ")