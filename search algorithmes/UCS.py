from Graph import Graph


def UCS(graph,start,end):
    stack=[(0,[start])]
    visited=[]
    const=0
    while stack:
        current=stack.pop()
        const+=1
        visited.append(current[1][-1])
        if current[1][-1]==end:
            return current[1],current[0],const
        for i in graph.get(current[1][-1]):
            if i not in visited:
                weight=graph[current[1][-1]][i]
                path=current[1][:]
                path.append(i)
                stack.append((current[0]+weight,path))
                stack=sorted(stack, key=lambda x: x[0])
                stack.reverse()

            
                
                



            
            
                    




graph=Graph()
graph.addnode(1)
graph.addnode(3)
graph.addnode(2)

graph.addnode(4)
graph.addnode(5)
graph.addnode(6)

graph.addedges(1,2,3)
graph.addedges(1,12,2)
graph.addedges(1,3,2)
graph.addedges(2,4,4)
graph.addedges(2,5,5)
graph.addedges(3,6,2)
graph.addedges(3,7,1)
graph.addedges(4,8,3)
graph.addedges(4,9,4)
graph.addedges(5,10,5)
graph.addedges(5,11,2)
graph.addedges(6,13,6)
graph.addedges(6,12,1)
graph.addedges(7,14,5)
graph.addedges(7,15,3)


graph=graph.return_graph()

print(UCS(graph,1,12))
