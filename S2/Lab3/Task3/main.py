import datastructures as ds

graph = ds.OrientedGraph("input")
print(graph.is_cycled())

print(graph.topological_sort())
