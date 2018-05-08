# Safe Path
Given points and radii of mines and their blast zones on a field, determine if there is a safe path across such field.

### Setup
Create a bunch of circles whose centers and radii are randomly chosen. Aim is to find a path that connects the the leftmost edge to the rightmost.

### Solution
The `safe_path.py` solution uses a variant of UCS that has the x-distance of a point as a priority metric.
![Alt Text](https://media.giphy.com/media/ddnzFx3r0W9tjXsKDc/giphy.gif)


While `faster_safe_path.py` actually attempts to find a path, using only the mines, which can traverse from top to bottom. If such a path exsists, then that must mean there is no way to cross the field safely.
![Alt Text](https://media.giphy.com/media/2zZOjNOAkmC2pZfoU3/giphy.gif)

### Usage
`python3 safe_path.py` or `python3 faster_safe_path.py`
