


class Stack2:

  stackRef = []
  def __init__(self):
    self.items = []
    self.maxLen = 99
    self.topIndex = -1
   
    

  def push(self, number):
    if(self.topIndex == self.maxLen):
      print("Error in push-stack is full")
    else:
      self.items.append(number)
      self.topIndex += 1
      

  def pop(self):
    if(self.empty()):
      print("Error in pop-stack is empty")
    else:
      self.topIndex -= 1

  def top(self):
    if(self.isEmpty()):
      print("Error in top-stack is empty")
    else:
      return self.items[self.topIndex]
      
  
  def empty(self):
    return (self.topIndex == -1)

  def __str__(self):
    temp_str = str(self.items)
    return temp_str
