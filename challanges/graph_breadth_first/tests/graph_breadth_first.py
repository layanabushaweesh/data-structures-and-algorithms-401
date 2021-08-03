from challanges.graph_breadth_first.graph_breadth_first import * 
from challanges.graph_breadth_first.graph_breadth_first import breadth_first

# from DataStructures.graph.graph import Graph ,Vertex ,Edge

def test_happy_path():
    graph2 = Graph()
    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
   
    manstropolis= graph2.add_node('manstropolis')
    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
   

    actual=breadth_first(pandora,pandora)
    expected=[pandora,arendelle,metroville,manstropolis]
    assert actual==expected