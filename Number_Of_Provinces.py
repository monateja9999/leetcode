class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        rows, cols =  len(isConnected), len(isConnected)

        par = [i for i in range(rows)]
        rank = [1] * rows

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            
            return 1
        
        res = rows
        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] == 1:
                    res -= union(row,col)
        return res