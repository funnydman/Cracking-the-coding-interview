"""
Task:
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""


graph = {
    1: [],
    2: [1],
    4: [2, 3],
    3: []
}


def search(graph, start, end, visited):
    if start == end:
        return True
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            return search(graph, node, end, visited)
    return False


print(search(graph, 1, 2, [])) # False
print(search(graph, 4, 1, [])) # True
