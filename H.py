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
    def __init__(self, bdy, m=0):
        self.level = 0
        self.bdy = np.array(bdy) ##3*2 matrix with coords as rows.
        self.children =[] ##each c is a new H object.
        self.intervals = []
        if (m!=0): 
            while self.level<m:
                self.up()

    def up(self):
        H.upgrade(self)

    @staticmethod
    def upgrade(h):
        if h.level ==0:
            h.children.append(H([h.bdy[0], 2*h.bdy[0]/3.0+h.bdy[1]/3.0, 2*h.bdy[0]/3.0+h.bdy[2]/3.0]))
            h.children.append(H([h.bdy[1], 2*h.bdy[1]/3.0+h.bdy[2]/3.0, 2*h.bdy[1]/3.0+h.bdy[0]/3.0]))
            h.children.append(H([h.bdy[2], 2*h.bdy[2]/3.0+h.bdy[0]/3.0, 2*h.bdy[2]/3.0+h.bdy[1]/3.0]))
            for i in range(3):
                h.intervals.append(Interval(0, 2*h.bdy[i]/3.0+h.bdy[(i+1)//3]/3.0, 2*h.bdy[i]/3.0+h.bdy[(i+1)//3]/3.0))
        else:
            for child in h.children:
                H.upgrade(child)
            for i in h.intervals:
                Interval.upgrade(i)
        h.level=h.level+1
    @staticmethod
    def plot(h, ax):
        if h.level ==0:
            pos = np.transpose(h.bdy)
            ax.scatter(pos[0], pos[1])   
        else:
            for c in h.children: H.plot(c, ax)
            for i in h.intervals: Interval.plot(i, ax)
            


class Interval:
    def __init__(self, m, p1, p2):
        self.level = m
        self.p1 =p1
        self.p2 = p2
    @staticmethod
    def upgrade(interval):
        interval.level=interval.level+1
    @staticmethod
    def plot(interval, ax):
        ax.plot([interval.p1[0], interval.p2[0]], [interval.p1[1], interval.p2[1]])
        if (interval.level!=0):
            l=np.zeros((np.power(2, interval.level-1), 2))
            for k in range(np.power(2, interval.level-1)):
                l.itemset((k,0), lincomb(interval.p1, interval.p2, k/float(np.power(2, interval.level-1)))[0])
                l.itemset((k,1), lincomb(interval.p1, interval.p2, k/float(np.power(2, interval.level-1)))[1])
            l=l.transpose()
            print(l[1])
            ax.scatter(l[0], l[1])
            

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

pos = np.matrix([[0, 0], [1, 0], [1.0/2.0, np.sqrt(3)/2.0]])
h=H(pos, 4)
H.plot(h, ax)
plt.show()
    


