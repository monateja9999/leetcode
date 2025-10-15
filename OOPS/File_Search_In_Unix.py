import os
from abc import ABC, abstractmethod
# Strategy Interface
class FileSearchStrategy(ABC):
    @abstractmethod
    def search(self, directory: str, criterion: str):
        pass
    def test():
        pass

# Concrete Strategy 1: Search by Name
class SearchByName(FileSearchStrategy):
    def search(self, directory: str, file_name: str):
        result = []
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                result.append(os.path.join(root, file_name))
        return result

# Concrete Strategy: Search by Extension
class SearchByExtension(FileSearchStrategy):
    def search(self, directory: str, extension: str):
        result = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    result.append(os.path.join(root, file))
        return result

# Context Class: FileSearch
class FileSearch:
    def __init__(self, strategy: FileSearchStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: FileSearchStrategy):
        self.strategy = strategy

    def search(self, directory: str, criterion: str):
        return self.strategy.search(directory, criterion)

# Driver Code
if __name__ == "__main__":
    directory = '/path/to/search'
    file_name = 'example.txt'
    extension = '.txt'

    # Initialize FileSearch with SearchByName strategy
    file_search = FileSearch(SearchByName())

    # Search by name
    result = file_search.search(directory, file_name)
    print(f"Files found: {', '.join(result)}")

    # Switch to SearchByExtension strategy
    file_search.set_strategy(SearchByExtension())

    # Search by extension
    result = file_search.search(directory, extension)
    print(f"Files with {extension} extension: {', '.join(result)}")
