import rrt
import numpy as np
import matplotlib.pyplot as plt



#Initialize a tree
tree = rrt.tree(50, 50, 100, 1, 0, 100, 0, 100)


#set up the first central node
iniNode = rrt.node(tree.Qx, tree.Qy, None)


#initialize the tree G with initial node
tree.nodeAll.append(iniNode)




#generate random node, find nearest node, get new Node, insert to lists
for i in range(1, tree.numK):  
    nodeRandom = rrt.genRanNode(tree)
    q_near = rrt.nearest_vertex(nodeRandom, tree)
    #define q_new
    q_new = rrt.new_vertex(q_near, nodeRandom, tree.det)
    tree.nodeAll.append(q_new)
    edge = [[q_near.xPos, q_near.yPos],[q_new.xPos, q_new.yPos]]
    tree.EdgeAll.append(edge)


ylist = [] 
xlist=[]
for node in tree.nodeAll:
    x = node.xPos
    y = node.yPos
    xlist.append(x)
    ylist.append(y)

fig, ax = plt.subplots(figsize=(1,1), constrained_layout = True)
ax.scatter(xlist,ylist)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Points')
fig.set_facecolor('lightsteelblue')
plt.show()


"""
for i in tree.EdgeAll:
    print("newSet")
    print(i[0])
    print(i[1]),

    plt.plot([[i[0][0],[i[1][0],i[1][1],i[0][1]]]], 'b-')
plt.show()
"""



