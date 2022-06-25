real = "1 1 2 2 2 8"
given_data = input().split()
result = []

for i in range(len(given_data)):
    result.append(int(real.split()[i]) - int(given_data[i]))

print(' '.join(map(str, result)))
