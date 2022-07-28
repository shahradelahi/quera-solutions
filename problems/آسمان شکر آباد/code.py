count_of_lines, each_line_length = map(int, input().split())
stars = 0

for i in range(count_of_lines):
    line = input()
    stars += line.count('*')

print(stars)
