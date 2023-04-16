from Graph import Graph


def DFS(graph,start,end):
    stack=[[start]]
    visited=[]

    while stack:
        current_path=stack[-1]
        current_node=stack.pop()[-1]
        visited.append(current_node)

        if current_node==end:
            return current_path
        for i in graph.get(current_node):
            if i not in visited:
                current_path.append(i)
                x=current_path[:]
                stack.append(x[:])
            x.pop()

graph=Graph()
graph.addnode(1)
graph.addnode(3)
graph.addnode(2)

graph.addnode(4)
graph.addnode(5)
graph.addnode(6)

graph.addedges(1,2)
graph.addedges(1,3)
graph.addedges(2,4)
graph.addedges(2,5)
graph.addedges(3,6)
graph.addedges(3,7)
graph.addedges(4,8)
graph.addedges(4,9)
graph.addedges(5,10)
graph.addedges(5,11)
graph.addedges(6,12)
graph.addedges(6,13)
graph.addedges(7,14)
graph.addedges(7,15)



graph=graph.return_graph()

print(DFS(graph,4,6))

