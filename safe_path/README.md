# Safe Path
Given points and radii of mines and their blast zones on a field, determine if there is a safe path across such field.

### Setup
Create a bunch of circles whose centers and radii are randomly chosen. Aim is to find a path that connects the the leftmost edge to the rightmost.

### Solution
Using a variant of UCS that has the x-distance of a point as a priority metric.

Usage: `$ python3 safe_path.py`

![Alt Text](https://media.giphy.com/media/ddnzFx3r0W9tjXsKDc/giphy.gif)
