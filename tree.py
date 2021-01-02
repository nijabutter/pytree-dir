import os

class Tree:

	def __init__(self):
		self.fileCount = 0
		self.dirCount = 0
	def search(self, dir, tabcount=0, isSub=False):
		try:
			files = os.scandir(dir)
		except:
			print("Error searching:", dir)
		else:
			for f in files:
				print("│  " * tabcount, end="")
				print("└──", f.name)
				if f.is_dir():
					self.dirCount += 1
					self.search(f.path, tabcount=tabcount+1, isSub=True)
				else:
					self.fileCount += 1

tree = Tree()
tree.search("/etc")
print(f"\nDirectories: {tree.dirCount} Files: {tree.fileCount}")