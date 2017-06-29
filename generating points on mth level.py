import numpy as np
import scipy
print("OK")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax =fig.add_subplot(111, projection ='3d')

m2 = np.zeros((27, 2))
def lincomb(p1, p2, k=1):
    return p1*k+p2*(1-k)
def testf(x, y):
    return x+y


class H:
    def __init__(self, m=0, bdy, c0=None, c1=None, c2=None):
        self.level = m
        self.bdy = bdy ##3*2 matrix with coords as rows.
        self.children =[c0, c1, c2] ##each c is a new H object.
        
        self.intervals = []
        for i in range(3):
            self.intervals.append(Interval(m, [2*bdy[i]/3.0+bdy[(i+1)//3]/3.0, 2*bdy[i]/3.0+bdy[(i+1)//3]/3.0]))

    @staticmethod
    def upgrade(h):
        if h.level ==0:
            self.children.append(H(0, [b0, 2*b0/3.0+b1/3.0, 2*b0/3.0+b2/3.0]))
            self.children.append(H(0, [b1, 2*b1/3.0+b2/3.0, 2*b0/3.0+b0/3.0]))
            self.children.append(H(0, [b2, 2*b2/3.0+b0/3.0, 2*b2/3.0+b1/3.0]))
        else:
            for child in h.children:
                H.upgrade(child)
            for i in self.intervals:
                Interval.upgrade(i)
    @staticmethod
    def plot(h, fig):
        ###for i in h.intervals:
        ###        Interval.plot(i, fig)
        ###if h.level == 0: 
        ###    fig.plot(h.bdy)
        ###else:
        ###    H.plot(h.child1, fig)
        ###    H.plot(h.child2, fig)
        ###    H.plot(h.child3, fig)
            


class Interval:
    def __init__(self, m=0, p1=None, p2=None):
        self.level = m
        self.p1 =p1
        self.p2 = p2
        self.pts = np.matrix([p1, p2])
    @staticmethod
    def upgrade(interval):
        self.level++
    @staticmethod
    def plot(interval):
        ###if interval.level ==0:
            

    @staticmethod
    def getpts(self):
        ##should return a (2^(m-1)+2)*2 matrix with rows as xy coords for points from p0 to p1
        ##@todo
        return
        
class Point:
##maybe we don't need it
    def __init__(self):
        self.type = ''
        self.born = 0
        self.pos= np.matrix([[0, 0]])
    


