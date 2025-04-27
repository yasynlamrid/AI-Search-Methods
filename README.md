Introduction

This project tests and compares different search algorithms: BFS (Breadth-First Search), Random Search, Greedy Search, Beam Search, and A*.
The problem is simple: a tourist wants to walk from Rue Royale to the Grand-Place in Brussels, choosing the most interesting paths for sightseeing.
I used Python for the algorithms and Folium to show the paths on interactive maps.

Algorithms

1. Breadth-First Search (BFS)
   
Start from the first point.
Visit all nearby places first.
Continue until we reach the goal.
Show the path on a Folium map.
BFS uses a queue to explore all options equally.

2. Random Search
   
Walk randomly to the next place.
Different path every time.
Random search is fast but not always smart.

3. Greedy Search
   
Choose the next place based on the shortest air distance to the goal.
It uses a simple heuristic.
Sometimes faster, but not always the best path.

4. Beam Search
5. 
Like Greedy, but keeps only the top 2 best options at every step.
Faster than BFS because it looks at fewer places.
Needs a "beam width" (here set to 2).

5. A* Search
Combines best distance + tourist attraction score.
Better roads have lower scores.
Finds a nice path with interesting places.
If we change start and end points, the path also changes.

Conclusion

Each algorithm was compared by execution time and memory used:


Algorithm	                Time (ms)	          Memory (elements)
BFS	                       2	                17
Random Search             	2	                20
Beam Search	              4.5	                17
Greedy Search	            4.86	              17
