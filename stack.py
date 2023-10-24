

#Class definition 
class Stack2:

  stackRef = []
  def __init__(self):
    self.items = []
    self.maxLen = 99
    self.topIndex = -1
   
    

  def push(self, number):
    if(self.topIndex == maxLen):
      print("Error in push-stack is full")
    else:
      self.items.append(number)
      self.topIndex += 1
      

  def pop():
    if(self.empty()):
      print("Error in pop-stack is empty")
    else:
      self.topIndex -= 1

  def top():
    if(self.isEmpty()):
      print("Error in top-stack is empty")
    else:
      return self.items[self.topIndex]
      
  
  def empty():
    return (self.topIndex == -1)
    
