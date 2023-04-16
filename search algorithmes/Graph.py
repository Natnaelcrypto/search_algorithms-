class Graph:
    def __init__(self):
        self.graph={}

    def addnode(self,node,x=0,y=0):
        if node not in self.graph:
            self.graph[node]={}
            self.graph[node]["cord"]=[x,y]
    def addedges(self,node1,node2,wight=1):
        self.addnode(node1)
        self.addnode(node2)
        self.graph[node1][node2]=wight
        self.graph[node2][node1]=wight
        
    def return_graph(self):
        return self.graph
    
    

