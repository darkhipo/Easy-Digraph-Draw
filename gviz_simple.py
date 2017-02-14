#!/usr/bin/env python3

import pygraphviz  as pgv
import collections as coll
import os

Node = coll.namedtuple('Node', ['id','datum'])
Arc  = coll.namedtuple('Arc', ['in_node','out_node','datum'])

def arc_to_id(arc):
    #if(arc.datum):
    #    label =  '['+str(arc.in_node.id)+']'+'['+str(arc.out_node.id)+']'+'{'+str(arc.datum)+'}'
    #else:
    #    label =  '['+str(arc.in_node.id)+']'+'['+str(arc.out_node.id)+']'+'{}'
    label =  '['+str(arc.in_node.id)+']'+'['+str(arc.out_node.id)+']'
    return label

def node_to_label(node):
    label = str(node.id)+'{'+str(node.datum)+'}' if node.datum else str(node.id)
    return label

def arc_to_label(arc):
    label = str(arc.datum) if arc.datum else ''
    return label

def color_path(path,dot_G,color='red'):
    dot_G = dot_G.copy()
    color = str(color)
    miter = iter(path)
    done  = False
    try:
        n = next(miter)
        while(not done):
            node = dot_G.get_node(n.id)
            node.attr['color']     = color
            node.attr['fontcolor'] = color
            p = n
            n = next(miter)
            arc_name = arc_to_id(Arc(p,n,None))
            for a in dot_G.edges(nbunch=node):
                in_id, out_id = a
                if( out_id == arc_name ): #(in_id == node.name) and (out_id == n.id) ):
                    dot_G.get_edge(p.id,arc_name).attr['color'] = color
                    dot_G.get_node(arc_name).attr['fontcolor']  = color
                    dot_G.get_edge(arc_name,n.id).attr['color'] = color
    except StopIteration as e:
        done = True
    return dot_G

def color_nodes(nodes,dot_G,color='red'):
    dot_G = dot_G.copy()
    nodes = set(nodes)
    idz = [n.id for n in nodes]
    for n in idz:
        node = dot_G.get_node(n)
        node.attr['color']     = color
        node.attr['fontcolor'] = color
    return dot_G
 
def color_arcs(arcs,dot_G,color='red'):
    dot_G = dot_G.copy()
    arcs = set(arcs)
    for a in arcs:
        for e in dot_G.edges(nbunch=a.in_node.id):
            in_id, out_id = e
            if(a.in_node.id == in_id):
                arc_name = arc_to_id(a)
                dot_G.get_edge(in_id,arc_name).attr['color']  = color
                dot_G.get_node(arc_name).attr['fontcolor']    = color
                dot_G.get_edge(arc_name,a.out_node.id).attr['color'] = color
    return dot_G

def example_gdict():
    A = Node('A',None)
    B = Node('B',None)
    C = Node('C',None)
    
    AB = Arc(A,B,'A,B,C, \nit\'s as easy as')
    BC = Arc(B,C,'1,2,3!')
    
    g = {}
    g[A] = frozenset([AB])
    g[B] = frozenset([BC])
    g[C] = frozenset([])

    return g


def example_gdict_1():
    s = Node('s',None)
    a = Node('a',None)
    b = Node('b',None)
    c = Node('c',None)
    d = Node('d',None)
    t = Node('t',None)
    
    sa = Arc(s,a,'0:3')
    sd = Arc(s,d,'0:3')
    ab = Arc(a,b,'0:2')
    ad = Arc(a,d,'0:2')
    bc = Arc(b,c,'0:4')
    bt = Arc(b,t,'0:2')
    ct = Arc(c,t,'0:2')
    dc = Arc(d,c,'0:3')
    
    g = {}
    g[s] = frozenset([sa,sd]) 
    g[a] = frozenset([ab,ad])
    g[b] = frozenset([bc,bt])
    g[c] = frozenset([ct])
    g[d] = frozenset([dc])
    g[t] = frozenset([])

    return g,[s,a,b,c,t],[a,b,c],[sa,ad,bt]

'''
https://www.python.org/doc/essays/graphs/
http://www.graphviz.org/doc/info/lang.html
http://pygraphviz.github.io/documentation/latest/pygraphviz.pdf
'''
def dict_to_dot(dict_G, name=''):
    dict_G    = dict(dict_G)
    name      = str(name)

    nodes = dict_G.keys()
    G = pgv.AGraph(name=name, label=name, strict=False, directed=True, rankdir="LR")
    
    x_dim, y_dim         = 0.1, 0.1
    tail,adir,ahlen      = 'dot','both',0.62
    arc_descriptor_shape = 'plain'
    node_shape           = 'egg'
    arc_shape            = 'plain'
    arc_arrow_head       = 'normal'
    arc_arrow_tail       = 'dot'
    arc_mid              = 'none'
    arc_dir              = 'both'
    
    for node in nodes:
        G.add_node(node.id,label=node_to_label(node))
        arcs = dict_G[node]
        for arc in arcs:
            arc_id = arc_to_id(arc)
            G.add_node(arc_id,shape=arc_descriptor_shape,label=arc_to_label(arc),width=x_dim,height=y_dim)
            G.add_edge(node.id,arc_id,len=ahlen,dir=arc_dir,arrowtail=arc_arrow_tail,arrowhead=arc_mid)
            G.add_edge(arc_id,arc.out_node.id,shape=arc_shape,arrowtail=arc_mid,arrowhead=arc_arrow_head)

    return G

def dot_to_file(dot_G, name='out', env='./env'):
    G           = dot_G.copy()
    env         = os.path.abspath(env)
    layout_prog = 'dot'
    dot_suffix  = 'dot'
    img_suffix  = 'png'

    dot_G.graph_attr.update(name = name)
    dot_G.graph_attr.update(label = name)

    # print to screen
    print(G.string()) 
    
    if not os.path.exists(env):
        os.makedirs(env)

    G.layout(prog=layout_prog)
    dot_fname = os.path.join(env,name +'.' + str(dot_suffix))
    img_fname = os.path.join(env,name + '.' + str(img_suffix))
    G.write(dot_fname)
    print("Wrote " + str(dot_fname))

    # create a new graph from file
    G = pgv.AGraph(dot_fname)  
    G.layout(prog=layout_prog)
    G.draw(img_fname)       
    print("Wrote " + str(img_fname))

def test_1():
    g_dict, g_path, nodes, arcs = example_gdict_1()
    g_dot       = dict_to_dot(g_dict)
    color_pathz = color_path(g_path, g_dot) 
    color_nodez = color_nodes(nodes, g_dot) 
    color_arcz  = color_arcs(arcs, g_dot)

    dot_to_file(g_dot,name='1')
    dot_to_file(color_pathz,name='2')
    dot_to_file(color_nodez,name='3')
    dot_to_file(color_arcz,name='4')

    g_dict = example_gdict()
    g_dot  = dict_to_dot(g_dict)
    dot_to_file(g_dot,name='ABC')

if __name__ == '__main__':
    progz = ['neato','dot','twopi','circo','fdp','nop']
    #Seems that dot and neato work, the others don't look good, or break.
    test_1()
