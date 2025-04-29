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
		self.insertnodespath = []
		self.insertnodeschar = []
		self.delnodespath = []

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
		self.insertnodespath.append(path)
		self.insertnodeschar.append(character)

	def insert_by_path(self,path,character):
		current = self.root
		for i in path[:-1]:
			if i==0 and current.child[i] is None:
				current.child[i] = Node(i,'\0')
				current.child[i].parent = current
			current = current.child[i]
		current.child[path[-1]] = Node(path[-1],character)
		current.child[path[-1]].parent = current
		self.insertnodespath.append(path)
		self.insertnodeschar.append(character)

	def delete_by_path(self,path):
		current = self.root
		for i in path[:-1]:
			if i==0 and current.child[i] is None:
				current.child[i] = Node(i,'\0')
				current.child[i].parent = current
			current = current.child[i]
		current = current.child[path[-1]]
		current.character = '\0'
		self.delnodespath.append(path)

	def delete_by_index(self,index):
		curr_index = -1
		traverse_list = [self.root]
		while(traverse_list):
			current = traverse_list.pop()
			if current.parent_Num is not None and current.parent_Num>0:
				curr_index+=1
				if curr_index == index:
					current1 = current
					break
			for i in range(collab_lim-1,-1,-1):
				if current.child[i] is not None:
					traverse_list.append(current.child[i])
		current1.character = '\0'
		path = []
		pos = current1
		while(pos.parent is not None):
			path.append(pos.parent_Num)
			pos = pos.parent
		path.reverse()
		self.delnodespath.append(path)




	def tree_representation_string(self):
		out = []
		traverse_list = [self.root]
		while(traverse_list):
			current = traverse_list.pop()
			if current.character != '\0':
				out.append(current.character)
			for i in range(collab_lim-1,-1,-1):
				if current.child[i] is not None:
					traverse_list.append(current.child[i])
		return "".join(out)




class Client:
	#Client id is a number between 1-9
	def __init__(self,Client_id):
		self.Client_id = Client_id
		self.string_tree = Tree()
	def insert(self,index,character):
		self.string_tree.insert_by_index(index,character,self.Client_id)
	def delete(self,index):
		self.string_tree.delete_by_index(index)
	def catchup(self,client_other):
		for i in range(len(client_other.string_tree.insertnodespath)):
			if client_other.string_tree.insertnodespath[i] not in self.string_tree.insertnodespath:
				self.string_tree.insert_by_path(client_other.string_tree.insertnodespath[i],client_other.string_tree.insertnodeschar[i])
		for i in range(len(client_other.string_tree.delnodespath)):
			if client_other.string_tree.delnodespath[i] not in self.string_tree.delnodespath:
				self.string_tree.delete_by_path(client_other.string_tree.delnodespath[i])
	def sync(self,client_other):
		self.catchup(client_other)
		client_other.catchup(self)
	def get(self):
		return self.string_tree.tree_representation_string()



# nod = Node(0,'y')
# print("a",nod.character)

# rep = Tree()
# rep.insert_by_index(0,'f',6)
# rep.insert_by_index(1,'g',6)
# rep.insert_by_index(2,'5',6)
# rep.insert_by_index(2,'l',9)
# print(rep.tree_representation_string())
# rep.delete_by_index(0)
# print(rep.tree_representation_string())


# client1 = Client(1)
# client1.insert(0,'f')
# client1.insert(1,'g')
# client1.insert(2,'5')
# client1.insert(2,'l')
# print(client1.get())

# client2 = Client(2)

# client2.catchup(client1)

# client2.insert(0,'F')
# client2.insert(1,'G')
# client2.insert(2,'L')
# client2.insert(2,'5')
# print(client2.get())

c1 = Client(1)
c1.insert( 0 ,'T')
c1.insert( 1 ,'h')
c1.insert( 2 ,'i')
c1.insert( 3 ,'s')
c1.insert( 4 ,' ')
c1.insert( 5 ,'i')
c1.insert( 6 ,'s')
c1.insert( 7 ,' ')
c1.insert( 8 ,'t')
c1.insert( 9 ,'h')
c1.insert( 10 ,'e')
c1.insert( 11 ,' ')
c1.insert( 12 ,'s')
c1.insert( 13 ,'t')
c1.insert( 14 ,'a')
c1.insert( 15 ,'r')
c1.insert( 16 ,'t')
c1.insert( 17 ,' ')
c1.insert( 18 ,'o')
c1.insert( 19 ,'f')
c1.insert( 20 ,' ')
c1.insert( 21 ,'a')
c1.insert( 22 ,' ')
c1.insert( 23 ,'l')
c1.insert( 24 ,'o')
c1.insert( 25 ,'n')
c1.insert( 26 ,'g')
c1.insert( 27 ,' ')
c1.insert( 28 ,'a')
c1.insert( 29 ,'n')
c1.insert( 30 ,'d')
c1.insert( 31 ,' ')
c1.insert( 32 ,'b')
c1.insert( 33 ,'o')
c1.insert( 34 ,'r')
c1.insert( 35 ,'i')
c1.insert( 36 ,'n')
c1.insert( 37 ,'g')
c1.insert( 38 ,' ')
c1.insert( 39 ,'e')
c1.insert( 40 ,'s')
c1.insert( 41 ,'s')
c1.insert( 42 ,'a')
c1.insert( 43 ,'y')

c2 = Client(2)
c2.sync(c1)

c3 = Client(3)
c3.sync(c1)