
from Graph import Graph


def ID(graph,start,end):
    stack=[([start],0)]
    depth=0
    
    while stack:
        current_node=stack.pop()
        if current_node[0][-1]==end:
            return current_node[0]
        if len(stack)==0:
            depth+=1
            stack=deepening(graph,start,depth)


def deepening(graph,start,depth):
    stack=[([start],0)]
    ans=[]
    
    while True:
        current=stack.pop(0)
        for i in graph.get(current[0][-1]):
            current_path=current[0][:]
            current_path.append(i)
            if current[1]+1>depth:
                return ans
            stack.append([current_path,current[1]+1])
            ans.append([current_path,current[1]+1])

            
            






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

print(ID(graph,1,6))
