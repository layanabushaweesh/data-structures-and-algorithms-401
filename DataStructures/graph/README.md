# Graphs
<!-- Short summary or background information -->
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
1. add node
2. get nodes
3. get neighbors
4. size
5.  add edge 

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
1. add node 
* time : O(1)
* space : O(1)
2. add edge 
* time : O(n)
* space : O(n)
3. get nodes
* time: O(n)
* space: O(n)
4. get neighbors
time: O(n)
space: O(n)
5. size
* time: O(1)
* space: O(1)

## API
<!-- Description of each method publicly available in your Graph -->
1. add node: add node to the graph with value of the input and return node.

2. add edge: add edge between  two input nodes.

3. get neighbors: return  edges and the weight to the input node.

4. get nodes: returns all of the nodes in the graph.

5. size: returns  total numbers of nodes in the graph.