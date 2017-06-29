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
    def __init__(self, m=0, c1=None, c2=None, c3=None):
        self.level = m
        self.child1 =c1
        self.child2 =c2
        self.child3 =c3
        self.intervals = []
        for i in range(3):
            self.intervals.append(Interval(m))

    @staticmethod
    def upgrade(h):
        if h.level ==0:
            self.child1 = H(0)
            self.child2 = H(0)
            self.child3 = H(0)
        else:
            H.upgrade(h.child1)
            H.upgrade(h.child2)
            H.upgrade(h.child3)
            for i in range(3):
                h.intervals[i].upgrade()

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
    def graph(interval):

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
    


