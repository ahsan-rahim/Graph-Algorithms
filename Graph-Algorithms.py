from queue import PriorityQueue 
import heapq as HQ
import sys



orig_stdout = sys.stdout
sys.stdout = open('outputFile.txt', 'w')
#This line creates a file called outputFile and appends every print statment to the file.



'''
1st graph was hardcoded for testing but read from file

Undirectedgraph = {
    'A' : {'heu':15 , 'B':3 , 'H':4 },
    'B' : {'heu':14 , 'A':3 , 'C':4 , 'H':5},
    'C' : {'heu':10 ,'B':4 , 'D':8, 'G':3 },
    'D' : {'heu':2 , 'C':8, 'E':2, 'F':3 , 'G':8},
    'E' : {'heu':0 , 'D':2},
    'F' : {'heu':5 ,'D':3, 'G':4 },
    'G' : {'heu':9 , 'C':3, 'D':8, 'F':4, 'H':2},
    'H' : {'heu':11 , 'A':4 ,'B':5 , 'G': 2},
    
    
    
    'heu': {}


}





Directedgraph = {
    'A' : {'heu':15 , 'B':3 , 'H':4 },
    'B' : {'heu':14  , 'C':4 , 'H':5},
    'C' : {'heu':10 , 'D':8, 'G':3 },
    'D' : {'heu':2 , 'E':2, 'F':3 , 'G':8},
    'E' : {'heu':0 },
    'F' : {'heu':5 },
    'G' : {'heu':9 ,'F':4, 'H':2},
    'H' : {'heu':11 },
    
    
    
    'heu': {}


}


'''

def addVertex( vertexName , heu):
    graph[vertexName]={'heu':heu}


def addEdge( v1 , v2 , dist):
    graph[v1].update({v2:dist});
    graph[v2].update({v1: dist});


#lamda function to make ignore heuristic while checking for neighbours. Used with filters in for loops.
Hcheck = lambda x: x!='heu'



def Astar(node , goal):
    PQ = []
    found=False
    visited={}
    prev=node
    HQ.heappush(PQ,(0, node ,0 , prev))    
    s=(0 , node, 0, prev)
    visited[node]=0; 
        
    while  len(PQ) > 0 and found==False:
        prev=s
        s=HQ.heappop(PQ)
        if(s[1] not in visited or s[0]<= visited[s[1]]):
            print(s[1] , s[2])
            if s[1]== goal:
                found=True
            
            if(found==False):   
                for neighbour in filter(Hcheck, graph[s[1]]):
                    if( neighbour != s[3]  ):
                     #   print(graph[s[1]][neighbour] , s[0] , graph[neighbour]['heu'] , graph[s[1]]['heu'])
                        cost= graph[s[1]][neighbour] + s[2] + graph[neighbour]['heu']
                        distance=cost-graph[neighbour]['heu'] 
                        if( neighbour not in visited or cost < visited[neighbour]):
                            HQ.heappush(PQ ,( cost , neighbour , distance , s[1]) )
                            visited[neighbour]=cost
                     




def UCS(node , goal):
    PQ = []
    visited={}
    found=False
    HQ.heappush(PQ,(0, node))    
    s=(0 , node)
    visited[node]=0;     
    while  len(PQ) > 0 and found==False:
        prev=s
        s=HQ.heappop(PQ)
        if(s[1] not in visited or s[0]<= visited[s[1]]):
            print(s)
            if s[1]== goal:
                found=True
            if(found==False):
                
                for neighbour in filter(Hcheck, graph[s[1]]):
                    if( neighbour != prev[1]  ):
                        
                        cost= graph[s[1]][neighbour] + s[0]
                        
                        if( neighbour not in visited or cost < visited[neighbour]):
                            HQ.heappush(PQ ,( cost , neighbour) )
                            visited[neighbour]=cost
                     






def BestFS(node , goal, cost , prev):
    global found
    minCost=sys.maxsize
    minNeighbour=None
    print(node , cost)
    

    
    if(node==goal):
        found=True;
    elif found!= True:
        for neighbour in filter(Hcheck, graph[node]):
             if(neighbour!=prev):
                 totalCost= graph[neighbour]['heu'] + graph[node][neighbour]  + cost
                 
                 if totalCost < minCost:
                     minNeighbour= neighbour
                     minDistance= graph[node][neighbour]+cost
                     minCost=totalCost
        if(found!= True and minNeighbour!= None):
           # print(minNeighbour,minCost)
            BestFS( minNeighbour , goal , minDistance , node )

    
    
    









# Array to keep track of visited nodes.

def dfs(node , goal , cost=0):
    global found
    if node not in visited:
        print(node , cost)
        visited.append(node)
        if(node==goal):
            found=True;
        else:
            for neighbour in filter(Hcheck, graph[node]):
                
                if(found!= True):
                    dfs( neighbour , goal , cost + graph[node][neighbour])
            
            






def bfs( node , goal):
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    
    visited.append(node)
    queue.append((node , 0))

    while queue:
      s = queue.pop(0) 
      print (s) 
      if( s==goal):
          break;
      for neighbour in filter(Hcheck, graph[s[0]]):
          if neighbour not in visited:
              visited.append(neighbour)
              queue.append((neighbour , graph[s[0]][neighbour] + s[1]))
              if(neighbour==goal):
                  break;







found=False;
def DLS(node , goal, depth , cost=0):
   global found
   if node not in visited and found==False:
        print(node , cost)
        visited.append(node)  
        if(node==goal):
            found=True;
            
      
   if(depth>0 and found == False):
      for neighbour in filter(Hcheck, graph[node]):
          DLS( neighbour , goal , depth-1 , cost + graph[node][neighbour])
        

def IDS(node , goal):
     for i in range(2, len(graph)):
         DLS(node, goal , i)



#Driver code which reads from input file
with open("input.txt") as file:
    T=int(file.readline())
    for x in range(T):
        N=int(file.readline())
        A=65
        graph={}
    
        heuristics=  file.readline().split()
        
        for i  in range(N):
            addVertex(chr(65+i) , int(heuristics[i]))
        e=int(file.readline())
        
        for i in range(e):
            line=file.readline().split()
            addEdge(line[0] , line[1] , int(line[2]))
       # print(graph)
        node , goal = file.readline().split()
        print('\nA*: for graph number ' , x+1)
        Astar(node , goal)
        
        
        print('\nUCS  for graph number ' , x+1)
        UCS(node , goal)
        
        if(x!=2):
            found=False
            print('\nBest first Search  for graph number ' , x+1)
            BestFS(node, goal , 0 , node)
        else: print('\nBest First Search gets stuck in an infinite loop in 3rd graph \n')
        
        visited = []
        found=False
        print("\nDFS  for graph number " , x+1)                    
        dfs(node, goal)
        print('\n')
        
        visited=[]        
        found=False
        print("\nIDS for graph number " , x+1)  
        IDS(node , goal)
        
                
        print("\nBFS  for graph number " , x+1)           
        bfs(node, goal)
        print('\n')
                
sys.stdout.close()
sys.stdout=orig_stdout
print("File was successfully written!")









         