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


# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

