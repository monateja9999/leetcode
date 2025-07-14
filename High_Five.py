from collections import defaultdict
import heapq

class Solution:

    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        res =[]
        scores = defaultdict(list)
        for s_id, score in items:
            if len(scores[s_id]) < 5:
                heapq.heappush(scores[s_id], score)
            else:
                if scores[s_id][0] < score:
                    heapq.heappushpop(scores[s_id], score)
        for s_id in scores:
            res.append([s_id, sum(scores[s_id])//len(scores[s_id])])
        return res

# Driver code
if __name__ == "__main__":
    # Test input
    items = [
        [1, 91], [1, 92], [2, 93], [2, 97],
        [1, 60], [2, 77], [1, 65], [1, 87],
        [1, 100], [2, 100], [2, 76]
    ]

    # Instantiate and run
    sol = Solution()
    output = sol.highFive(items)

    # Print result
    print("Output:", output)