from abc import ABC, abstractmethod

# Component
class FileSystemEntity(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf
class File(FileSystemEntity):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f"- File: {self.name}")

# Composite
class Directory(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, entity: FileSystemEntity):
        self.children.append(entity)

    def display(self, indent=0):
        print('  ' * indent + f"+ Directory: {self.name}")
        for child in self.children:
            child.display(indent + 1)

# Demo
if __name__ == "__main__":
    # Files
    file1 = File("resume.pdf")
    file2 = File("cover_letter.docx")
    file3 = File("notes.txt")

    # Directories
    docs = Directory("Documents")
    docs.add(file1)
    docs.add(file2)

    downloads = Directory("Downloads")
    downloads.add(file3)
    downloads.add(docs)  # Nested directory

    root = Directory("Home")
    root.add(downloads)

    # Display structure
    root.display()
