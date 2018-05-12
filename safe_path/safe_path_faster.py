import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import collections as mc
from pqueue import PriorityQueue


fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100), aspect='equal')

N = 700
circle_x = np.random.rand(N)*100
circle_y = np.random.rand(N)*100
colors = np.random.rand(N)
radii = np.random.rand(N)*4

circles = list(zip(circle_x, circle_y, radii))

top = []
artist = {}

for circle in circles:
    x, y, r = circle

    circle_artist = plt.Circle((x,y),r,lw=1,fill=False)
    ax.add_artist(circle_artist)
    artist[circle] = circle_artist

    if y + r >= 100:
        top.append(circle)



graph = {}

def sq_dist(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def intersect(c1,c2):
    return sq_dist(c1,c2) <= (c1[2] + c2[2])**2

path = []
stack = []
discovered = set()

dfs_tree = {}

def search():
    for circle in top:
        stack.append(circle)

        while stack:
            c = stack.pop()
            
            if c in discovered:
                continue

            if c in dfs_tree:
                path.append(dfs_tree[c])

            discovered.add(c)

            if c[1] - c[2] <= 0:
                return

            for c1 in circles:
                if intersect(c, c1):

                    stack.append(c1)

                    dfs_tree[c1] = [c[:2],c1[:2]]

search()


iter_path = []
line_seg = mc.LineCollection(iter_path, linewidths=1,colors='r')
ax.add_artist(line_seg)

def animate(i):
    iter_path.append(path[i])
    line_seg.set_segments(iter_path)

    return line_seg,

anim = animation.FuncAnimation(fig, animate, frames = len(path), interval=30, repeat=False, blit=True)
plt.show()
