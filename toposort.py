#Uses python3

# Problem Introduction
# Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
# find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
# of the corresponding directed graph.
# Problem Description
# Task. Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.
# Input Format. A graph is given in the standard format.
# Constraints. 1 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105. The given graph is guaranteed to be acyclic.
# Output Format. Output any topological ordering of its vertices. (Many DAGs have more than just one
# topological ordering. You may output any of them.)

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

