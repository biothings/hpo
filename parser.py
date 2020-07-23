import networkx as nx
import obonet

def load_data(data_folder):
    url = "https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo"
    graph = obonet.read_obo(url)
    for item in graph.nodes():
        rec = graph.nodes[item]
        if rec.get("is_a"):
            rec["parents"] = rec.pop("is_a")
        if rec.get("xrefs"):
            rec["xrefs"] = rec.pop('xref')
        rec["children"] = list(graph.predecessors(item))
        rec["ancestors"] = list(nx.descendants(graph, item))
        rec["descendants"] = list(nx.ancestors(graph,item))
        if rec.get("created_by"):
            rec.pop("created_by")
        if rec.get("creation_date"):
            rec.pop("creation_date")
        yield rec