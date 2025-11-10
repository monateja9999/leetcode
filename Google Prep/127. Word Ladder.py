class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        neighbours = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        q = collections.deque([beginWord])
        visited = set([beginWord])
        level = 1
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return level
                for j in range(len(curr)):
                    pattern = curr[:j] + "*" + curr[j + 1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            level += 1
        return 0 