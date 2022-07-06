count_of_states, count_of_trips = map(int, input().split())
costs, trips = [], []

for i in range(count_of_states):
    costs.append(list(map(int, input().split())))

for i in range(count_of_trips):
    trips.append(list(map(int, input().split())))

print(sum(costs[trip[0] - 1][trip[1] - 1] for trip in trips))
