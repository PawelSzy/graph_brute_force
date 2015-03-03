"""
Algorithmic Thinking
Project 1 - Degree distributions for graphs
"""
EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}




def make_complete_graph(num_nodes):
    """
     Takes the number of nodes num_nodes 
     and returns a dictionary corresponding 
     to a complete directed graph 
     with the specified number of nodes
    """
    graph = {}
    for node in range(num_nodes):
        num = set(range(num_nodes))
        num.remove(node)
        graph[node] = num

    return graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph 
    (represented as a dictionary)
    and computes the in-degrees for the nodes
    eturn a dictionary with the same set of keys (nodes)
    as digraph whose corresponding values
    are the number of edges 
    whose head matches a particular node.
    """
    return_dict = {}
    for node in digraph:
        #find how many nodes go to computed "node"
        in_degree = 0
        for node2 in digraph:
            if node in digraph[node2]:
                in_degree+=1
        return_dict[node] = in_degree
    return return_dict

def in_degree_distribution(digraph):
    """
    unnormalized distribution of the in-degrees 
    of the graph
    eturn a dictionary 
    whose keys correspond to in-degrees of nodes 
    in the graph
    """
    in_degrees = compute_in_degrees(digraph)
    degree_graph = {}
    for node in in_degrees:
        number =  in_degrees[node]
        if number in degree_graph:
            degree_graph[number]+=1
        else:
            degree_graph[number]=1
    return degree_graph             
def test_run():	
    """
    test the program
    """
#    print EX_GRAPH0
#    print EX_GRAPH1
#    print EX_GRAPH2
#    print make_complete_graph(7)    
    
    #print "in_degrees", compute_in_degrees(EX_GRAPH2)
    
    print in_degree_distribution(EX_GRAPH2)
    
#test_run()	