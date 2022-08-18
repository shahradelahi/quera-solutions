n, k = map(int, input().split())

a = list(map(int, input().split()))

print(((len(a) * k) - sum(a)) // k)
