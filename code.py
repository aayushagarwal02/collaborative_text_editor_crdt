collab_lim = 10

#assume no start insert

class Node:
	def __init__(self, parent_Num,character):
		self.parent_Num = parent_Num
		self.character = character #default '\0'
		self.child = [None for i in range(collab_lim)]
		self.parent = None

class Tree:
	def __init__(self):
		self.root = Node(None,'\0')
		# self.IndexToNode = {} #aayush aayush
		self.insertnodes = []
		self.insertnodeschar = []
		self.delnodes = []

	def insert_by_index(self,index,character,Client_id):

		# calculating node for corresponding index:

		if index==0:
			current1 = self.root
		else:
			
			curr_index = -1
			traverse_list = [self.root]
			while(traverse_list):
				current = traverse_list.pop()
				if current.parent_Num is not None and current.parent_Num>0:
					curr_index+=1
					if curr_index == index-1:
						current1 = current
						break
				for i in range(collab_lim-1,-1,-1):
					if current.child[i] is not None:
						traverse_list.append(current.child[i])
		current = current1



		while(True):
			flag = True
			for i in range(0,Client_id+1):
				if current.child[i] is not None:
					flag = False
			if flag:
				break
			if current.child[0] is None:
				current.child[0] = Node(0,'\0')
				current.child[0].parent = current
			current = current.child[0]
		current.child[Client_id] = Node(Client_id,character)
		current.child[Client_id].parent = current

		"""
		Not needed anymore
		# newIndexToNode = {}
		# for i in self.IndexToNode:
		# 	if i>=index:
		# 		newIndexToNode[i+1] = self.IndexToNode[i]
		# 	else:
		# 		newIndexToNode[i] = self.IndexToNode[i]
		# newIndexToNode[index] = current.child[Client_id]

		# self.IndexToNode = newIndexToNode
		"""

		path = []
		pos = current.child[Client_id]
		while(pos.parent is not None):
			path.append(pos.parent_Num)
			pos = pos.parent
		path.reverse()
		self.insertnodes.append(path)
		self.insertnodeschar.append(character)

	# def insert_by_path


	def tree_representation_string(self):
		out = []
		traverse_list = [self.root]
		while(traverse_list):
			current = traverse_list.pop()
			out.append(current.character)
			for i in range(collab_lim-1,-1,-1):
				if current.child[i] is not None:
					traverse_list.append(current.child[i])
		return "".join(out)




class Client:
	#Client id is a number between 1-9
	def __init__(self,Client_id):
		self.Client_id = Client_id
		self.changes = []

nod = Node(0,'y')
print("a",nod.character)

rep = Tree()
rep.insert_by_index(0,'f',6)
rep.insert_by_index(1,'g',6)
rep.insert_by_index(2,'5',6)
rep.insert_by_index(2,'l',9)
print(rep.tree_representation_string())