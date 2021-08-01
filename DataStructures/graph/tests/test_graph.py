from DataStructures.graph.graph import Graph 
from DataStructures.graph.graph import  Vertex ,Edge
import pytest

def test_size_1():
    graph = Graph()
    graph.add_node('liyan')
    actuall = graph.size()
    expected = 1
    assert expected == actuall


def test_size_2():  
    graph = Graph()
    actuall = graph.size()
    expected = 0
    assert expected == actuall


def test_add_node_3():  
    graph = Graph()
    expected = 'jesy'
    actuall = graph.add_node('jesy').value
    assert expected == actuall


def test_addedge_start_4():
    graph = Graph()
    start_node = Vertex('L')
    end_node = graph.add_node('I')
    with pytest.raises(KeyError):
        graph.add_edge(start_node, end_node)


def test_addedge_end_5():
    graph = Graph()
    end_node = Vertex('L')
    staet_node = graph.add_node('I')
    with pytest.raises(KeyError):
        graph.add_edge(staet_node, end_node)


def test_add_edge_other_case_6():
    graph = Graph()
    end = graph.add_node('b')
    start = graph.add_node('a')
    graph.add_edge(start, end)
    #  actuall =graph.add_edge(start, end)

def test_getnode_7():
    graph = Graph()
    l = graph.add_node('l')
    m = graph.add_node('m')
    s = Vertex('s')
    actuall = len(graph.get_nodes())
    expected = 2
    assert actuall == expected




