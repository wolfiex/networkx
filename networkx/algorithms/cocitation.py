"""Functions for creating a co-citation graph.

A co-citation graph is a semantic similarity measure which ranks documents commonly cited together by other documents [1]_. It provides a forward looking assesment on how similar two documents are, as opposed to the retrospective approach of the citation network.


References
----------
.. [1] Henry Small, 1973 "Co-citation in the scientific literature: a new measure of the relationship between two documents"

"""
import networkx as nx
from networkx.utils import not_implemented_for

__all__ = ['cocite']


@not_implemented_for('undirected')
@not_implemented_for('multigraph')
def cocite(G,min_citations = 2):
    """Compute a the co-citation graph using a citation network

    Parameters
    ----------
    G : graph
        A directed graph of citations between nodes.

    min_citation : integer (optional, default=2)
        The minimum number of co-citations required to keep an edge in the cocitation graph.

    Returns
    -------
    G : graph
        An undirected cocitation graph

    Notes
    -----
    The implementation is written by Daniel Ellis (2019) [1]_.

    References
    ----------
    .. [1] .
    """


    if not G.is_directed():
        msg = "The cocitation algorithm requires a directed citation graph as an input."
        raise nx.NetworkXError(msg)

    #assert type(G) == nx.classes.digraph.DiGraph

    edges = {}
    #for each node
    for n in G.nodes():
        # for each outward edge (citing)
        out = G.out_edges(n)
        for i in out:
            for j in out:
                if i==j: break

                pair = tuple(set([i[1],j[1]]))
                try: edges[pair] = edges[pair] + 1
                except: edges[pair] = 1

    CC = G.to_undirected() # this returns a deepcopy
    CC = nx.create_empty_copy(CC, with_data=True)

    edgelist = [(i[0][0],i[0][1],i[1]) for i in edges.viewitems() if i[1]>min_citations]

    CC.add_weighted_edges_from(edgelist)

    return CC
