graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}


# Add node
def add_node(node):
    if node not in graph:
        graph[node] = []
    else:
        print(f"Node {node} already exists in graph.")


# add edge
def add_edge(node1, node2):
    if node1 in graph and node2 in graph:
        if node2 not in graph[node1]:
            graph[node1].append(node2)
        if node1 not in graph[node2]:
            graph[node2].append(node1)
    else:
        print("One or both nodes not found")


# deleting a Node


def delete_node(node):
    if node in graph:
        for other in graph:
            if node in graph[other]:
                graph[other].remove(node)
        del graph[node]
    else:
        print(f"Node {node} doesn't exist.")


# deleting edge


def delete_edge(node1, node2):
    if node1 in graph and node2 in graph:
        if node2 in graph[node1]:
            graph[node1].remove(node2)
        if node1 in graph[node2]:
            graph[node2].remove(node1)
    else:
        print("One or both nodes not found in dic")


# List = ["Vansh","Hima","Rishi","yogit","Sehej","kalra","Natya"]

# for i in List:
#     add_node(i)

# add_edge("Vansh","Hima")
# add_edge("Sehej","kalra")

print(graph)


# DPS : Depth first Search
# - Goes deep in one path before back tracking


def dfs(node, visited=None):
    if visited is None:
        visited = set()  # initializes visited node
    visited.add(node)  # marking current node as visited
    print(node, end=" ")

    for neighbor in graph[node]:  # Checking neighbour for the current node
        if neighbor not in visited:
            dfs(neighbor, visited)


dfs("A")
print(end="\n")


def bfs(node):
    visited = set()
    queue = []  # Order of nodes

    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.pop(0)  # Removing from the start
        print(current, end=" ")

    for neighbour in graph[current]:
        if neighbour not in visited:
            queue.append(neighbour)
            visited.add(neighbour)


for i in graph:
    bfs(i)
