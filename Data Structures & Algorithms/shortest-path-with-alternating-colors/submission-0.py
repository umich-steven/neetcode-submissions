from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        The input is n nodes plus lists of edges, which means it’s a graph, and 
        the word “shortest” on an unweighted graph almost always means BFS.
        """
        node_list = defaultdict(list)
        for i in redEdges:
            a, b = i
            node_list[a].append((b, "red"))
        for j in blueEdges:
            a, b = j
            node_list[a].append((b, "blue"))
        
        arr = [-1] * n
        queue = deque([(0, 0, None)])
        visited = set()

        while queue:
            node, distance, color = queue.popleft()
            if arr[node] == -1:
                arr[node] = distance

            for nxt, edge_color in node_list[node]:
                if edge_color != color and (nxt, edge_color) not in visited:
                    visited.add((nxt, edge_color))
                    queue.append((nxt, distance + 1, edge_color))

        return arr
            


       
        
