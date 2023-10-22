


class Stack2:
  topIndex
  maxLen
  stackRef = []
  def __init__(self):
    maxLen = 99
    topIndex = -1
    stackRef= [100]
    

  def push(number):
    if(topIndex == maxLen):
      print("Error in push-stack is full")
    else:
      topIndex+=1
      

  def pop():
    if(stackRef.isEmpty()):
      print("Error in pop-stack is empty")
    else:
      topIndex-=1

  def top():
    if(stackRef.isEmpty()):
      print("Error in top-stack is empty")
    else:
      return stackRef.index(topIndex)
      
  
  def empty():
    topIndex == -1
    
