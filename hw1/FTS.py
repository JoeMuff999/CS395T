'''
Joseph Muffoletto
jrm7925
CS 395T, Prof. Topcu
HW1, Exercise 4 Part B 

Accepts any FTS that has a set of states, a set of transition triples, and a set of initial states 
Generates all N length paths, where N is programmer provided
exercise_4_test() builds the FTS shown in figure 4
'''

from queue import Queue
from typing import List
import copy


'''
Each node contains the following information:
    -state name/id
    -possible transitions (neighbors)
    -initial state boolean (True if its an initial state, false otherwise)
'''
class Node:
    def __init__(self, name : str, is_initial : bool):
        self.name = name
        self.is_initial = is_initial
        self.neighbors = []
    
    def add_neighbor(self, neighbor_state):
        self.neighbors.append(neighbor_state)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name
    
    

'''
Constructs the FTS using the Node data structure
returns a List of Nodes
'''
def generate_fts_nodes(states : set, initial_states : set, transitions : set) -> List[Node]:
    nodes: List[Node] = [] 
    for state in states:
        node = Node(state, state in initial_states)
        nodes.append(node)
    for t in transitions:
        # print(t)
        s1, a, s2 = t
        # kinda janky
        n1 = None
        n2 = None
        # I really do not like this.
        for node in nodes:
            if node.name == s1:
                n1 = node
            if node.name == s2:
                n2 = node
        assert(n1 != None)
        assert(n2 != None)
        n1.add_neighbor(n2)
    return nodes
        
'''
Constructs all n-length paths possible from the provided FTS
Only builds paths from initial states
returns the list of paths (each path is a list)
'''
def generate_paths(nodes : List[Node], length):
    paths = []
    for state in nodes:
        if not state.is_initial:
            continue
        #run a BF tree search from each state:
        q = Queue()
        q.put((state, [state]))
        while not q.empty():
            curr_state, curr_path = q.get()
            if len(curr_path) == length:
                paths.append(curr_path)
            else:
                for neighbor in curr_state.neighbors:
                    new_path = copy.copy(curr_path)
                    new_path.append(neighbor)
                    q.put((neighbor, new_path))
    return paths

'''
wrapper function which combines FTS generation and path generation
'''
def generate_n_length_paths(states : set, initial_states : set, transitions : set, length : int):
    nodes = generate_fts_nodes(states, initial_states, transitions)
    # print(generate_paths(nodes, length))
    return generate_paths(nodes, length)

'''
example use of library
generates the paths for the FTS provided in figure 4 of the homework.
'''
def exercise_4_test():
    example_states = {'s1', 's2', 's3', 's4', 's5'}
    transitions = {('s1', '', 's3'), ('s1', '', 's4'), ('s3', '','s4'), ('s4', '','s3'), ('s4', '','s5'), ('s5', '','s4'), ('s5','', 's5'), ('s4','', 's2'), ('s2','', 's4')}
    initial_states = {'s1', 's2'}
    length = 10
    paths = generate_n_length_paths(example_states, initial_states, transitions, length)
    print(paths)

exercise_4_test()


