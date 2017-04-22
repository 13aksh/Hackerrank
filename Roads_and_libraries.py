#!/usr/bin/python

q = int(raw_input())

for _ in range(q):
    n,m,lib,road = map(int, raw_input().split())
    degree = [0 for _ in range(n+1)]
    adjacency_list = {x:[] for x in range(1,n+1)}
    # Do it with iteration.
    def DFS(index):
        val = 0
        node = adjacency_list[index]
        for i in xrange(len(node)):
            if degree[node[i]] != -1:
                degree[node[i]] = -1
                if node[i] in adjacency_list:
                    val += road + DFS(node[i])
                else:
                    val += road
        del node
        return val

    for i in range(m):
        a,b = [int(x) for x in raw_input().split()]
        degree[a] += 1
        degree[b] += 1
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    if road >= lib:
        print n*lib
    else:
        ans = 0
        for i in range(1,n+1):
            if adjacency_list[i] == []:
                del adjacency_list[i]
                ans += lib
        while True:
            large = max(degree)
            large_index = degree.index(large)
            degree[large_index] = -1
            # print large
            if large == 0:
                break
            # print adjacency_list
            ans += lib + DFS(large_index)
        print ans
    # print degree
    # print adjacency_list
