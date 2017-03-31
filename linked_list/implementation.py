from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        #self.size = 0
        #appending the elements to list
        if elements:
            for elem in elements:
                self.append(elem)
         #       self.size +=1
                
    def __str__(self):
        """[1, 2, 3]"""
        if self.start == None and self.end == None:
            return '[]'
        else:
            return '[{}]'.format(', '.join([str(e) for e in self]))
            

    def __len__(self):
        counter = 0
        for i in self:
            counter += 1
        return counter

    def __iter__(self):
        self.current = self.start
        
        while self.current:
            yield self.current.elem
            self.current = self.current.next
        
        raise StopIteration
        

    def __getitem__(self, index):
        for i,element in enumerate(iter(self)):
            if i == index:
                return element
        
        raise IndexError

    def __add__(self, other):
        
        if not isinstance(other,LinkedList):
            raise TypeError
        
        new_list = LinkedList()
        
        for i in self:
            new_list.append(i)
        
        for i in other:
            new_list.append(i)
        
        return new_list

    def __iadd__(self, other):
        
        for i in other:
            self.append(i)
        return self
    
    def __ne__(self,other):
        return not self == other
        
    def __eq__(self, other):
        if type(self) == type(other) and len(self) !=len(other):
            return False
        
        pos = self.start
        other_pos = other.start
        counter =0
        while counter < len(self):
            if pos.elem != other_pos.elem:
                return False
            else:
                pos = pos.next
                other_pos = other_pos.next
                counter +=1
        
        return True

    def append(self, elem):
        new_node = Node(elem)
        new_node.next = None
        if self.start is None:
            
            self.start = new_node
            self.end = new_node
            
        else:
            self.end.next = new_node
            self.end = new_node
        #self.size +=1  

    def count(self):
        return len(self)

    def pop(self, index=None):
        
        if index == None:
            index = len(self) - 1
        
        if index  not in range(len(self)):
            raise IndexError
        
        counter =0
        current_node = self.start
        
        while current_node:
            if counter == index:
                pop = current_node.elem
            
                if index == 0:
                    if self.start.next is not None:
                        self.start = self.start.next
                    else:
                        self.start = None
                    
                elif index == len(self) - 1:
                    self.end = previous_node
                    self.end.next = None
            
                else:
                    previous_node.next = current_node.next
            
            previous_node = current_node
            current_node = current_node.next
            counter +=1    
            
        return pop
