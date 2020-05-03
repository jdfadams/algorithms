from collections import defaultdict
import csv
import json


def get_components(graph):
    '''Return the strongly connected components of a directed graph.

    This is an implementation of Kosaraju's algorithm.

    '''

    def assign(v, root):
        if v in assigned:
            return
        assigned.append(v)
        components[root].append(v)
        for n in get_in_neighbors(v, graph):
            assign(n, root)

    def visit(v):
        if v in visited:
            return
        visited.append(v)
        for n in get_out_neighbors(v, graph):
            visit(n)
        L.append(v)

    L = []
    visited = []
    for v in get_vertices(graph):
        visit(v)

    assigned = []
    components = defaultdict(list)
    for v in reversed(L):
        assign(v, v)

    components = components.values()
    components = sorted(sorted(component) for component in components)
    return components


def get_in_neighbors(v, graph):
    return set(a for a, b in graph if b == v)


def get_out_neighbors(v, graph):
    return set(b for a, b in graph if a == v)


def get_vertices(graph):
    return set(v for edge in graph for v in edge)


def load_graph(fp):

    def infer_type(value):
        try:
            return int(value)
        except TypeError:
            return value

    reader = csv.reader(fp)
    return [tuple(infer_type(value) for value in row) for row in reader]


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    return parser.parse_args()


def main():
    args = parse_args()
    graph = load_graph(args.file)
    components = get_components(graph)
    print(json.dumps(components))


if __name__ == '__main__':
    main()
