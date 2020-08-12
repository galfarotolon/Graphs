from utils import Stack, Queue, Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    
    q = Queue()

    q.enqueue([starting_node])
    
    visited = set()
    result = []

    while q.size() > 0:
        path = q.dequeue()
        last_vert = path[-1]

        if last_vert not in visited:
            visited.add(last_vert)


        for neighbor in graph.get_neighbors(last_vert):
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
            result.append(path_copy[-1])
        
        if result == []:
            return -1
        


    return result[-1]

