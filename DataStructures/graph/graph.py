class Vertex():
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value}"

class Edge():
    def __init__(self, vertex , weight):
        self.vertex = vertex
        self.weight = weight

class Graph():
    
    def __init__(self):
        #we represent the graph as a dictionary
        self.adjacency_list = {}

    def add_node(self,value):

        """
        this method will adds value to a node and adds the node to a graph
        """
        add_value = Vertex(value)
        # Add to the adjacency_list
        self.adjacency_list[add_value] = [] 
        return add_value

    
    
    def add_edge(self,start_node,end_node,weight=0):

        """
        this method will adds a new edge between two nodes in the graph

        """
        # TODO: Check if both are in the graph
        # We want to prevent  function to continuing if the start and end does not  in the graph
        if end_node not in self.adjacency_list:
            raise KeyError('end node  not in graph')
        if start_node not in self.adjacency_list:
            raise KeyError('start node not in graph')
        
        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)


    def size(self):

        """
        this method will returns the size of our graph`dictionary`

        """
        return len(self.adjacency_list)

    def get_nodes(self):

        """
        this method will gets all of the nodes in the graph

        """

        # if len(self._adjacency_list) == 0 :
        #     return 
        return self.adjacency_list.keys()


    def get_neighbors(self,vertex):

        """
        this method will get all of the neighbors of a vertex
        
        """
        return self.adjacency_list[vertex]


    def __str__(self) -> str:
        return self.adjacency_list



