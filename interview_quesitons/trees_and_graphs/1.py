"""
Task:
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
from typing import List, Dict

graph = {
    1: [],
    2: [1],
    4: [2, 3],
    3: []
}


def search_recursively(
        graph: Dict[int, List[int]],
        start: int,
        end: int,
        visited: set
):
    if start == end:
        return True
    if start not in visited:
        visited.add(start)
        for node in graph[start]:
            return search_recursively(graph, node, end, visited)
    return False


def search_iteratively(
        graph: Dict[int, List[int]],
        start: int,
        end: int
):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node == end:
            return True
        for n in graph[node]:
            if n not in visited:
                stack.append(n)
                visited.add(n)
    return False


assert search_recursively(graph, 1, 2, set()) is False
assert search_recursively(graph, 4, 1, set()) is True

assert search_iteratively(graph, 1, 2) is False
assert search_iteratively(graph, 4, 1) is True
