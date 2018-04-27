import pygraphviz as pgv
from parse import get_edges

graph = pgv.AGraph(directed=True)
# nodes = ['a','b','c']
# undir_edges = [('a','b')]
# dir_edges = [('a','c'), ('b','c')]
courses_list, course_prereq_list, course_overlap_list = get_edges()
graph.add_nodes_from(courses_list)
graph.add_edges_from(course_overlap_list, color='red', dir='none')
graph.add_edges_from(course_prereq_list, color='blue')
print(graph)
graph.write('cos_graph.dot')