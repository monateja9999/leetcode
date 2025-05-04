from typing import (
    List,
)
import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:

        alien_dict = collections.defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
               indegree[char] = 0
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            parse_len = min(len(w1),len(w2))
            if w1[:parse_len] == w2[:parse_len]:
                if len(w1) > len(w2):
                    return ""
            else:
                for j in range(parse_len):
                    if w1[j] != w2[j]:
                        if w2[j] not in alien_dict[w1[j]]:
                            alien_dict[w1[j]].add(w2[j])
                            indegree[w2[j]] += 1
                        break
        
        res =""
        heap = []

        for key in indegree:
            if indegree[key] == 0:
                heapq.heappush(heap, key)
        
        while heap:
            letter = heapq.heappop(heap)
            res += letter
            for nei in alien_dict[letter]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heapq.heappush(heap, nei)

        return "".join(res) if len(res) == len(indegree) else ""