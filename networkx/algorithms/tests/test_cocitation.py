import pytest
numpy = pytest.importorskip('numpy')



from networkx import cocite
import networkx as nx


import random
rng = float(random.randint(4, 100))



def test_cocite():
    '''
    Using a complete graph, cocitation edge number follow the pattern
    (n-1)(n/2).
    '''

    G = nx.complete_graph(int(rng)).to_directed()
    CC = cocite(G,min_citations = 1)
    assert len(CC.edges()) == int((rng-1)*(rng/2))
