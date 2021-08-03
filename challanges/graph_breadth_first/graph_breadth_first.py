from DataStructures.graph.graph import Graph ,Edge ,Vertex
def breadth_first(self,node):
        
            if not node in self.adjacency_list.keys():
                return "error"

            all_out = []
            breadth = []

            all_out.append(node)
            breadth.append(node)
            while(len(all_out)):
                edges = self.get_neighbors(node)
                if len(edges):
                    for edge in edges:
                        if not edge.node in all_out:
                            all_out.append(edge.node)
            # breadth.pop(0)
            return breadth
     