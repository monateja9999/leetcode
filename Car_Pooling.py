class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0]*1001

        for i in range(len(trips)):
            passengers[trips[i][1]] += trips[i][0]
            passengers[trips[i][2]] -= trips[i][0]
        
        currPassengers = 0
        for i in range(1001):
            currPassengers += passengers[i]
            if currPassengers > capacity:
                return False
        return True

        # SOLUTION 2
        # req = sorted(trips, key=lambda x:x[1])
        # q = deque()
        # q.append(req[0])
        # people = req[0][0]
        # if people > capacity:
        #     return False
        # for i in range(1, len(req)):
        #     while q and q[0][2] <= req[i][1]:
        #         people -= q[0][0]
        #         q.popleft()
        #     people += req[i][0]
        #     if people > capacity:
        #         return False
        #     q.append(req[i])
        # return True

        # SOLUTION 3          
        # trips.sort(key=lambda x:x[1])
        # heap = []
        # passengers = 0
        # for i in range(len(trips)):
        #     while heap and heap[0][0] <= trips[i][1]:
        #         passengers -= heap[0][1]
        #         heapq.heappop(heap)
        #     passengers += trips[i][0]
        #     if passengers > capacity:
        #         return False
        #     heapq.heappush(heap, [trips[i][2],trips[i][0]])
        # return True
