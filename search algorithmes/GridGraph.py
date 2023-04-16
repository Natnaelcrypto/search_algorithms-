class Graph:
    def __init__(self,width,height):
        self.grid=[]
        self.graph={}
        self.width=width
        self.height=height

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append("##")

   
    def addedges(self,node1,node2,wight=1):
        self.graph[node1][node2]=wight
        self.graph[node2][node1]=wight
        self.grid[node1][node2]=" +"
        self.grid[node2][node1]=" +"

        
    def printGrid(self):
        for i in range(self.height):
            for j in range(self.width):
                
                print(f'{self.grid[i][j]}', end=' ')

            print()

    



    