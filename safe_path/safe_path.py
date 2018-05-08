import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import collections as mc
from pqueue import PriorityQueue


fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100), aspect='equal')

N = 400
circle_x = np.random.rand(N)*100
circle_y = np.random.rand(N)*100
colors = np.random.rand(N)
radii = np.random.rand(N)*4

for x,y,r in zip(circle_x, circle_y, radii):
    ax.add_artist(plt.Circle((x,y),r,lw=1,fill = False))


d = 1

def sq_dist(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def in_circle(p):
    for x,y,r in zip(circle_x, circle_y, radii):
        if sq_dist(p, (x,y)) < r**2:
            return True
    
    return False


def is_bounded(x):
    return x[0] >= 0 and x[0] <= 100 and x[1] >= 0 and x[1] <= 100


path = []
start = (0,50)

while in_circle(start):
    start = (0,np.random.randint(101))

frontier = PriorityQueue()
frontier.insert(start,0)

visited = set()
while frontier.heap:
    dist,node = frontier.pop()
    path.append(node)

    if node[0] == 100:
        break
    
    visited.add(node)
    
    up = (node[0], node[1] + d)
    up_right = (node[0] + d, node[1] + d)
    right = (node[0] + d + 1, node[1])
    down_right = (node[0] + d, node[1] - d)
    down = (node[0], node[1] - d)

    for n in [up,up_right,right,down_right,down]:
        if n not in visited and not in_circle(n) and is_bounded(n):
            frontier.insert(n, -n[0])

    
path = list(zip(path,path[1:]))



iter_path = []
line_seg = mc.LineCollection(iter_path, linewidths=2)
ax.add_artist(line_seg)

def animate(i):
    iter_path.append(path[i])
    line_seg.set_segments(iter_path)
    return line_seg,

anim = animation.FuncAnimation(fig, animate, frames = len(path), interval=20, repeat=False, blit=True)
plt.show()