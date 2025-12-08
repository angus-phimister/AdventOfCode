from collections import defaultdict, deque
import math

with open("2025/day8/input.txt") as f:
    input = [[int(c) for c in x.split(",")] for x in f.read().split('\n')]

def dist(A:list, B:list): 
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2 + (A[2]-B[2])**2)**(1/2)

mp = defaultdict(int)

for i,x in enumerate(input):
    for j, y in enumerate(input):
        if i == j:
            continue
        if (j,i) in mp.keys():
            continue
        mp[(i,j)] = dist(x,y)


print("distances calculated")
connections = []
for _ in range(1000):
    min_connection = min(mp, key=mp.get)
    connections.append(min_connection)
    del mp[min_connection]
    print(_)


print("connections calculated")

# Build adjacency list (undirected)
adj = defaultdict(set)
for a, b in connections:
    adj[a].add(b)
    adj[b].add(a)

visited = set()
circuits = []
print("starting BFS calculated")

for node in adj:
    if node not in visited:
        comp = []
        q = deque([node])
        visited.add(node)

        while q:
            cur = q.popleft()
            comp.append(cur)
            for nxt in adj[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        circuits.append(sorted(comp))


t = sorted([len(x) for x in circuits], reverse=True)[:3]
print(math.prod(t))

breakpoint()