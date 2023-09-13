import math
import numpy as np


class tree:

    def __init__(self, Qx, Qy, numK, det, D_xl, D_xh, D_yl, D_yh):
        self.Qx = Qx 
        self.Qy = Qy
        self.numK = numK
        self.det = det
        self.D_xl = D_xl
        self.D_xh = D_xh
        self.D_yl = D_yl
        self.D_yh = D_yh

    def inputInitialCond(self):
        self.numK = input("Input values of number of vertices in RRT")
        self.Qx = input("Input values for Qx")
        self.Qy = input("Input values for Qy")
        self.det = input("Input values of incremental distance")
        self.D_xl = input("Input values of lowerbound x for D")
        self.D_xh = input("Input values of upperbound x for D")
        self.D_yl = input("Input values of lowerbound y for D")
        self.D_yh = input("Input values of upperbound y for D")
    
    #define variables
    #a list to store all nodes
    #a list to store all edge
    nodeAll = []
    EdgeAll = []



    

class node():
    def __init__(self, xPos, yPos, parent):
        self.xPos = xPos
        self.yPos = yPos
        self.parent = parent


#Take two nodes, return the distance between them
def getDistance(nodeA, nodeB):
    dis = math.sqrt((nodeA.xPos - nodeB.xPos)**2 + (nodeA.yPos - nodeB.yPos)**2)
    return dis

def getAngle(nodeA, nodeB):
    sinVal= abs(nodeA.xPos - nodeB.xPos) / getDistance(nodeA, nodeB)
    arcsine = math.asin(sinVal)

    # Convert the result to degrees if needed
    degrees = math.degrees(arcsine)

    return degrees

def new_vertex(q_near, q_rand, stepSize):
    v = [q_rand.xPos - q_near.xPos, q_rand.yPos - q_near.yPos]
    unitV = v/np.linalg.norm(v)
    new_vert_var= unitV
    newVertNode_vec = [q_near.xPos + new_vert_var[0], q_near.yPos + new_vert_var[1]]
    newVertNode = node(newVertNode_vec[0], newVertNode_vec[1], q_near)
    
    return newVertNode

#return the nearest vertex for random nodes in the tree
def nearest_vertex(qrand, t):
    distance_min = 5000000 #any other methods?
    nearest_vertex = t.nodeAll[0]
    for node in t.nodeAll:
        dis = getDistance(node, qrand)
        if dis < distance_min:
            nearest_vertex = node
    
    return nearest_vertex

#generate a random note inside the D range
def genRanNode(tree):
    #np.random.seed(1)
    random_x= np.random.uniform(tree.D_xl, tree.D_xh + 1)
    random_y= np.random.uniform(tree.D_yl, tree.D_yh + 1)
    nodeRand = node(random_x, random_y, None) 
    #when create a random node, we are not going to use it, so should i put none in the parent?
    #would it mess up other things like tree head
    return nodeRand

