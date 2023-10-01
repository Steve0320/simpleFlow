# Holds stuff for running workflow
import networkx as nx

NODE_LIBRARY = {}


def register_node(name, inputs=None, outputs=None):
    def inner(func):
        NODE_LIBRARY[name] = {
            'fn': func,
            'inputs': inputs or {},
            'outputs': outputs or {}
        }
        return func
    return inner


# Example nodes - eventually split these into separate directory
@register_node('test_process', inputs={"a": "string"}, outputs={"b": "string"})
def test_process(input_dict):
    output_dict = {"b": input_dict["a"].capitalize()}
    return output_dict


# Main function - load the given workflow and pass the given args into it
# def run_workflow(filename, args):
#
#     print(f"NODES IS {NODE_LIBRARY}")
#
#     # Load graph definition
#     G = nx.read_gexf(filename)
#
#     nodes = {}
#     for v, d in G.nodes(data=True):
#
#         nodefn_name = d["fn"]
#
#         # All the info we need to run this node in the graph
#         thing = {}
#
#         if nodefn_name == "input":
#             thing["fn"] = lambda _:
#
#         # node_def = NODE_LIBRARY[nodefn_name]
#         #
#         # nodes[v] = {}
#         # nodes[v]["fn"] = node_def["fn"]
#
#     # First, sanity check that all degree 0 nodes have all arg data present
#     # TODO
#
#     # Starting with all nodes that have no unmet arguments (e.g. deg 0), run functions
#
#     # Add the outputs to the data set, and keep iterating
