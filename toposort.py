#Uses python3

import sys
import numpy

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    # used = [0] * len(adj)
    order = []
    #write your code here

    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v, order)

    # print(post.sort())
    # print(post)
    order.reverse()

    return order


def explore(v, order):
    # print('v: ', v)
    # print('clock: ', clock)
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w,order)
    order.append(v)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = numpy.zeros((n, 1))
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

