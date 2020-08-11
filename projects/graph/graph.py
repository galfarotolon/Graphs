"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) - add this to make them
            # bi directional verteces

        else:
            raise IndexError('nonexistent vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
         # create an empty queue
        q = Queue()

        # add starting vertex id
        q.enqueue(starting_vertex)

        # create set for visited vertices
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue a vertex
            v = q.dequeue()
            # if not visited
            if v not in visited:
                # mark as visisted
                print(v)
                visited.add(v)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            value = s.pop()
            visited.add(value)

            for val in self.vertices[value]:
                if val not in visited:
                    s.push(val)
                    visited.add(val)

            print(value)
        


    def dft_recursive(self, starting_vertex_id, visited=None):

        """
         Print each vertex in depth-first order
         beginning from starting_vertex.

        This should be done using recursion.
         """

        if visited is None:
            visited = set()


        visited.add(starting_vertex_id)

        print(starting_vertex_id)

        
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:

                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
        
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:

                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                # IF SO, RETURN PATH
                    return path 
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[v]: 
                    # COPY THE PATH
                    path_2 = list(path)
                    # APPEND THE NEIGHOR TO THE BACK
                    path_2.append(neighbor)

                    q.enqueue(path_2)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            p = s.pop()
            v = p[-1]
            if v == destination_vertex:
                return p
            visited.add(v)
            for nv in self.vertices[v]:
                path_2 = list(p)
                path_2.append(nv)
                s.push(path_2)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                new_path = self.dfs_recursive(vert ,destination_vertex,visited,path)
                if new_path is not None:

                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))




## Checking example in readme file (part 1)
# (it passes correctly as the example shown)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# print(graph.vertices)


'''
Should print: 

{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
} 
'''