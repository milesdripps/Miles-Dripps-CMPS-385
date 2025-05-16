from stack import Stack
from queue import Queue

class Graph:
    def __init__(self):
        """
        Directed matrix, one key maps to a value
        """
        self.adjacency_matrix = {}

    def add_directed_edge(self, a: str, b: str):
        key = a.lower()
        value = b.lower()

        if key in self.adjacency_matrix:
            if value in self.adjacency_matrix[key]:
                print(f"{value} already in")
                return
            else:
                self.adjacency_matrix[key].append(b)
        else:
            self.adjacency_matrix[key] = [value] #append as a list

    def print_adjacency(self):
        print(next(iter(self.adjacency_matrix)))
        for key,value in self.adjacency_matrix.items():
            print(f"{key}->{value}")

    def bfs(self, start, end):
        queue = Queue()
        previous_vertices = {}
        visited_vertices = []

        queue.enqueue(start)
        visited_vertices.append(start)
        while not queue.empty():
            current = queue.dequeue()
            queue.display()
            if current not in self.adjacency_matrix:
                break

            for neighbor in self.adjacency_matrix[current]:
                    if neighbor not in visited_vertices:
                        queue.enqueue(neighbor)
                        visited_vertices.append(neighbor)
                        #Make the neighbors previous vertice the current one
                        previous_vertices[neighbor] = current


        shortest_path, shortest_path_len = self.get_shortest_path(start, end, previous_vertices)
        return shortest_path, shortest_path_len

    def dfs(self, start, end):
        stack = Stack()
        previous_vertices = {}
        visited_vertices = []

        stack.insert(start)
        visited_vertices.append(start)
        while not stack.isempty():
            current = stack.top_and_pop()
            visited_vertices.append(current)
            if current not in self.adjacency_matrix:
                break

            for neighbor in self.adjacency_matrix[current]:
                if neighbor not in visited_vertices:
                    stack.insert(neighbor)
                    visited_vertices.append(neighbor)

                    previous_vertices[neighbor] = current

        shortest_path, shortest_path_len = self.get_shortest_path(start, end, previous_vertices)
        return shortest_path, shortest_path_len

    def get_shortest_path(self, start, end, path):
        shortest_path = []

        #Iterate starting from 'end' until we get to 'start'
        prev = path[end]
        shortest_path.append(end)
        shortest_path.append(prev)
        while prev in path:
            if prev not in path:
                break
            else:
                key = path[prev]
                shortest_path.append(key)
                prev = key

        shortest_path = list(reversed(shortest_path))
        if shortest_path[0] == start:
            return shortest_path, len(shortest_path) - 1
        else:
            print(f"Could not construct path: {shortest_path}")
            return

def main1():
    new_graph = Graph()
    new_graph.add_directed_edge("a","b")
    new_graph.add_directed_edge("a","c")
    new_graph.add_directed_edge("b","e")
    new_graph.add_directed_edge("c","d")
    new_graph.add_directed_edge("c","e")
    new_graph.add_directed_edge("c","f")
    new_graph.add_directed_edge("c","g")
    new_graph.add_directed_edge("d","a")
    new_graph.add_directed_edge("e","c")
    new_graph.add_directed_edge("e","f")
    new_graph.add_directed_edge("f","d")
    new_graph.add_directed_edge("f","g")
    new_graph.add_directed_edge("g","h")
    path, path_len = new_graph.bfs("a","h")
    print(f"BFS: Shortest Path from a to h: {path} of length {path_len}")
    path, path_len = new_graph.dfs("a", "h")
    print(f"DFS: Shortest Path from a to g: {path} of length {path_len}")

main1()
