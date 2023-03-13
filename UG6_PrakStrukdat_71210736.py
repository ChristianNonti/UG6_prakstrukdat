class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.current_node = None

  def addElementHead(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.current_node = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def addElementTail(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.current_node = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def maju(self, steps):
    for i in range(steps):
      if self.current_node.next is not None:
        self.current_node = self.current_node.next
      else:
        break
    return self.current_node.data

  def mundur(self, steps):
    for i in range(steps):
      if self.current_node.prev is not None:
        self.current_node = self.current_node.prev
      else:
        break
    return self.current_node.data
  
linkedlist = LinkedList()
linkedlist.addElementHead("Jogja") #Jogja
linkedlist.addElementHead("Jakarta") #Jakarta - Jogja
linkedlist.addElementTail("Bali") #Jak
