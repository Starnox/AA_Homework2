from kCliqueBKT import Graph
import sys

if __name__ == '__main__':
    
    inputFile = sys.argv[1]

    with open(inputFile, 'r') as f:
        k = int(f.readline())
        n = int(f.readline())
        m = int(f.readline())
    
        # quick verification if we don't even have k * (k-1) / 2 edges then it's
        # impossible to have a k-Clique

        connections = []
        for _ in range (m):
            for line in f: # read rest of lines
                (a,b) = ([int(x) for x in line.split()])
                connections.append((a,b))
        
        graph = Graph(connections)

        ## create string for SAT

        ## we will have k*|V| variables that have the following meaning:
        ## Xiv means that the index i in the clique is occupied by vertex v
        resultSAT = ""

        ## first rule 
        ## Every node in the clique should have a vertex
        ## O(k * |V|) = O(n^2) reduction complexity -> polynomial

        
        for i in range(1,k+1):
            resultSAT = ''.join((resultSAT,'('));
            for v in range(1,n+1):
                resultSAT = ''.join((resultSAT, 'x', str(i), str(v), ' V '));
            resultSAT = resultSAT[:-3];
            resultSAT = ''.join((resultSAT, ') ^ '));
        ## second rule
        ## Every position in the clique should be occupied by unique vertexes
        ## O(k^2 * |V|) = O(n^3) reduction complexity -> polynomial
        ## clauses of type ~Xiv V ~Xjv 
        
        for v in range(1,n+1):
            for i in range(1,k):
                for j in range(i+1, k+1):
                    resultSAT = ''.join((resultSAT, "(~x", str(i), str(v), " V ", "~x", str(j), str(v), ")", " ^ "));

        ## third rule
        ## For every edge in the graph that doesn't exist we should not have in our clique
        ## both the two vertexes that describe that edge
        ## O(|V|^2 * k^2) = O(n^4) reduction complexity -> polynomial
        
        for v in range(1, n+1):
            for u in range(1,n+1):
                # if there is not an edge
                if graph.is_connected(v,u) == False:
                    for i in range(1,k):
                        for j in range(i+1,k+1):
                            resultSAT = ''.join((resultSAT, "(~x", str(i), str(v), " V ", "~x", str(j), str(u), ")", " ^ "));
        
        
        resultSAT = resultSAT[:-3]
        print(resultSAT)