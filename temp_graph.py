# Make a dummy graph
import networkx as nx
import uuid

# Very simple graph, just INPUT ("in") -> PROCESS ("a"/"b") -> OUTPUT ("out")
G = nx.MultiDiGraph()

input_id = uuid.uuid4()
process_id = uuid.uuid4()
output_id = uuid.uuid4()

G.add_node(input_id, fn="input", input_types="string,int", input_labels="inputA,inputB", outputs={"in": "string"})
G.add_node(process_id, fn="test_process", inputs={"a": "string"}, outputs={"b": "string"})
G.add_node(output_id, fn="output", inputs={"out": "string"}, outputs={})

G.add_edge(input_id, process_id, from_pin="in", to_pin="a")
G.add_edge(process_id, input_id, from_pin="b", to_pin="out")

nx.write_gexf(G, "testgraph.gexf")