#!/usr/bin/env python
import asciitree
import sys

class Node(object): #came from docuemntation page 
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):# also came from documentatin page
        return self.name

    def listChildren(self): #self writen
    	ans = []
    	for i in self.children:
    		ans.append(i.name)
    	return ans

    def find(self,x): #self writen
    	for i in self.children:
    		if(i.name == x):
    			return i
    	return None

data = []
for line in sys.stdin:
	input = filter(None,line.split(' ')) #filter the ''
	data.append(input[0:-1])# strip the terminating \n


root = Node('root', [])
iterator = root
j = 1
for i in range(0,len(data)):
	if(len(data[i]) == 1):#exception for root
		continue
	
	while(data[i][j] in iterator.listChildren()):#loop through the dirs while they are already in the dict
		iterator = iterator.find(data[i][j])
		j += 1
	
	for k in range(j,len(data[i])):#dirs no longer found so start adding them to dict
		iterator.children.append(Node(data[i][k],[]))
		iterator = iterator.children[-1]

	iterator.name += " (" +str(data[i][0]) + ")" #append the request count to the leaf
	
	j = 1; #reset iterator variables
	iterator = root

print asciitree.draw_tree(root)#print the tree
