import networkx as nx


def find_cycle_in_consumption_graph(allocation:list[list[float]]):
    # use nx and creat new graph
    grapgG = nx.DiGraph()
    # size of players and object
    listsize = (len(allocation[:]) + len(allocation[:][0]))
    # set all object and player in list
    t = [item for item in range(listsize)]
    # all object in the list input in the graph graphG
    grapgG.add_nodes_from(t)
    # for loop if have connection bettwen player and object
    for i in range(len(allocation[:])):
        for j in range(len(allocation[:][0])):
            if allocation[i][j] > 0:
                #if have connection bettwen player and object , we add the edge of player and object in graph graphG
                grapgG.add_edge(i, len(allocation[:]) + j)
    #if have cycle with function find cucle of nx print the cycle and prine yes cycle and
    # if not cycle in the graphG chake with nxNoCycle
    # print not cycle
    try:
        c = list(nx.find_cycle(grapgG, orientation="ignore"))
        print("Cycle Yes", c)

    except nx.NetworkXNoCycle:
        print("Cycle No")


c0 = [[0.0, 0.0, 0.0 , 0.1 , 0.0],
      [0.25, 0.0, 0.0 , 0.3 , 0.0],
      [1.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.5, 0.3 , 0.4 , 0.0]]
find_cycle_in_consumption_graph(c0)
c0two = [[0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.25, 0.0, 0.0 , 0.3 , 0.0],
      [0.0, 1.0, 0.0 , 0.0 , 1.0],
      [1.0, 0.0, 0.0 , 0.0 , 1.0],
      [0.0, 0.0, 0.3 , 0.0 , 0.0]]
find_cycle_in_consumption_graph(c0two)
c2 = [[0.75, 0.0, 0.0 , 0.0 , 0.0],
      [0.25, 0.0, 0.0 , 0.0 ,0.0],
      [0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.2, 0.42 , 0.1 , 0.0],
      [0.0, 0.3, 0.67 , 0.13 , 0.0]]
find_cycle_in_consumption_graph(c2)
c1 = [[0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.0, 0.0 , 0.0 ,0.0],
      [0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.0, 0.42 , 0.1 , 0.0],
      [0.0, 0.0, 0.67 , 0.13 , 0.0]]
find_cycle_in_consumption_graph(c1)
c2two = [[0.0, 0.0, 0.0 , 0.0 , 0.0],
      [0.25, 1.0, 0.0 , 0.0 , 0.0],
      [1.0, 1.0, 0.0 , 0.0 , 0.0],
      [0.0, 0.0, 0.0 , 0.1 , 0.2],
      [0.0, 0.0, 0.0 , 0.4 , 0.3]]
find_cycle_in_consumption_graph(c2two)
