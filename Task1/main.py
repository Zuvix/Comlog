import cfg
n=cfg.n
m=cfg.m
edges=cfg.edges
f = open("Task1\output.txt", "w")
f.write("c Generated CNF for Graph with:\n")
f.write("c n = {}\n".format(n))
f.write("c m = {}\n".format(m))

#functions to generate CNF formulas
def edge_rules(edges):
    f.write("c ------------------------\n")
    f.write("c Rules to ensure we have the all the specified edges\n")
    f.write("c ------------------------\n")
    for x in edges:
        f.write("{}v{} \n".format(x[0],x[1]))

def exactly_one_color_per_node(n,m):
    f.write("c ------------------------\n")
    f.write("c Rules to ensure there is exactly one color per node.\n")
    f.write("c ------------------------\n")
    for x in range(n):
        for y in range(m):
            f.write("n{}c{} ".format(x,y))
        f.write("\n")
        for y in range(m):
            for z in range(m):
                if z!=y:
                    f.write("-n{}c{} ".format(x,z))
            f.write("\n")

def check_edges_for_same_color(edges,m):
    f.write("c ------------------------\n")
    f.write("c Rules to ensure there are no connected nodes that share a color.\n")
    f.write("c ------------------------\n")
    for x in edges:
        a=x[0]
        b=x[1]
        for y in range(m):
            f.write("-{}v{} ".format(a,b))
            f.write("-n{}c{} ".format(a,y))
            f.write("-n{}c{} ".format(b,y))
            f.write("\n")

#calling the generating functions
edge_rules(edges)
exactly_one_color_per_node(n,m)
check_edges_for_same_color(edges,m)
    
