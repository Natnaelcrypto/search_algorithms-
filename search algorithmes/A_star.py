from Graph import Graph

def hurstic(start,end):
    x1,y1=start
    x2,y2=end
    return abs(x1-x2)+abs(y1-y2)


def A_star(graph,start,end,hurstic):
    stack=[([start],0)]
    visited=[]
    count_step=0
    while stack:
        current=stack.pop()
        count_step+=1
        current_value=current[0][-1]
        visited.append(current_value)
        if current_value==end:
            return current,count_step
        
        end_cord=graph[end]["cord"]

        for i in graph.get(current_value):
            if i!="cord" and i not in visited:
                start_cord=graph[i]["cord"]
                length=hurstic(start_cord,end_cord)
                cost=graph[current_value][i] + length
                path=current[0][:]
                path.append(i)
                stack.append((path,cost))
                stack=sorted(stack, key=lambda x: x[1])
                stack.reverse()


graph=Graph()

graph.addnode(1,1,1)
graph.addnode(2,2,0)
graph.addnode(3,0,3)
graph.addnode(4,3,1)
graph.addnode(5,2,4)
graph.addnode(6,4,2)
graph.addnode(7,4,4)
graph.addnode(8,2,2)

graph.addedges(1,3,3)
graph.addedges(1,2,1)
graph.addedges(1,4,4)
graph.addedges(1,7,5)
graph.addedges(2,3,2)
graph.addedges(2,4,4)
graph.addedges(4,5,2)
graph.addedges(6,5,2)
graph.addedges(5,3,5)
graph.addedges(7,6,2)
graph.addedges(8,4,3)
graph.addedges(8,6,1)

graph1=graph.return_graph()

print(A_star(graph1,2,7,hurstic))
