hour, minute = map(int, input().split())
print("%02d:%02d" % ((12 - hour) % 12, (60 - minute) % 60))
