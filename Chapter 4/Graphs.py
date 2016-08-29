graph = {
		 'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set([])
         }

# 4.2 Simple DFS
def routeExists(graph, start, end):
	if _routeExists(graph, start, end) == None:
		return False
	return True

def _routeExists(graph, start, end, visited=None):
 	if visited == None:
 		visited = set()
 
 	if start == end:
 		return True

 	visited.add(start)

 	for n in graph[start] - visited:
 		res = _routeExists(graph, n, end, visited) 
 		if res != None:
 			return res

print(routeExists(graph,"A","B"))
print(routeExists(graph,"A","C"))
print(routeExists(graph,"A","D"))
print(routeExists(graph,"A","E"))
print(routeExists(graph,"A","F"))
print(routeExists(graph,"B","B"))
print(routeExists(graph,"C","D"))
print(routeExists(graph,"D","E"))
print(routeExists(graph,"E","C"))
print(routeExists(graph,"F","D"))
print("------")
print(routeExists(graph,"G","A"))
print(routeExists(graph,"G","B"))
print(routeExists(graph,"G","C"))
print(routeExists(graph,"G","D"))
print(routeExists(graph,"G","E"))
print(routeExists(graph,"G","F"))
