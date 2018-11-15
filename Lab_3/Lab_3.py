from collections import defaultdict


def topologic_sort(graph, start):
    seen = set()
    stack = []
    order = []
    que = [start]
    while que:
        v = que.pop()
        if v not in seen:
            seen.add(v)
            que.extend(graph[v])

            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)
    print(order[::-1])
    return stack + order[::-1]


if __name__ == "__main__":
    graph = defaultdict(list)
    for line in open("GO.txt"):
        vertexes = line.split()
        if len(vertexes)!= 2:
            break
        graph[vertexes[0]].append(vertexes[1])
    result = topologic_sort(graph, 'visa')
    result.reverse()
    Go_out = open("GO_out.txt", 'w')
    for r in result:
        Go_out.write(r + "\n")
    print(result)






