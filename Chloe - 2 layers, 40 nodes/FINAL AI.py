import random
import math

#AUTIN PIPKINS 9-6-19 started: 9:00pm


#sigmoid function
def sig(x):
  return 1 / (1 + math.exp(-x))

#inputLayer
class Layer0:
  def __init__(self, val):#initial value set
    self.value = val
        
  def setValue(self, val):
    self.value = val

  def getValue(self):
    return self.value


#first layer of nodes
class Layer1:
  def __init__(self):
    self.value = .5
    self.defWeightSet()#calls to oinitialize weights

  def setValue(self, val):
    self.value = val

  def getValue(self):
    return self.value


  def setWeightSet(self, weights):#weights are ordered multipliers
    self.weightSet = weights#each weight coorisponds to a node in the prev layer

  def getWeightSet(self):
    return self.weightSet

  def defWeightSet(self):
    self.weightSet = []
    for node in layer0Nodes:
      rando = random.randint(-999999,999999)/999999.0#random float from -.999 to .999
      self.weightSet.append(rando)#adds this random float to weightSet, the lsit of weights


  def updateValue(self):#will update current value based on previous layer's lavues
    value = 0#and this node's weights that coorispond to them
    for i in range(len(layer0Nodes)):#do this n times, n = numebr of nodes in prev layer
        value = value + self.weightSet[i]*layer0Nodes[i].getValue()#a1x1+a2x2+a3x3+a4x4 (a -> weights, x -> prev layer node values)
             
    value = sig(value)#all values must be between 0-1, sigmoid corrects for that
    self.value = value

            
#see layer one
class Layer2:
  def __init__(self):
    self.value = .5
    self.defWeightSet()



  def setValue(self, val):
    self.value = val

  def getValue(self):
    return self.value



    
  def setWeightSet(self, weights):
    self.weightSet = weights

  def getWeightSet(self):
    return self.weightSet

  def defWeightSet(self):
    self.weightSet = []
    for node in layer1Nodes:
      rando = random.randint(-999999,999999)/999999.0
      self.weightSet.append(rando)

  def updateValue(self):
    value = 0
    for i in range(len(layer1Nodes)):
      value = value + self.weightSet[i]*layer1Nodes[i].getValue()
            
    value = sig(value)
    self.value = value


#see layer 1
class Layer3:
  def __init__(self):
    self.value = .5
    self.defWeightSet()

  def setValue(self, val):
    self.value = val

  def getValue(self):
    return self.value


  def setWeightSet(self, weights):
    self.weightSet = weights

  def getWeightSet(self):
    return self.weightSet

  def defWeightSet(self):
    self.weightSet = []
    for node in layer2Nodes:
      rando = random.randint(-999999,999999)/999999.0
      self.weightSet.append(rando)




  def updateValue(self):
    value = 0
    for i in range(len(layer2Nodes)):
      value = value + self.weightSet[i]*layer2Nodes[i].getValue()
            
    value = sig(value)
    self.value = value       

#will round each element of a list
def roun(lis):
    lisp = lis
    for i in range(len(lis)):
        lisp[i] = round(lis[i], 3)

    return lisp

#will post a screenshot of the nodes and weights of an AI instance
def printAI():
  print("LAYER 0\n") 
  for i in range(len(layer0Nodes)):
    print (round(layer0Nodes[i].getValue(),3), end="")
    print ("   ", end="")


  print("\n\n\nLAYER 1\n")
  for i in range(len(layer1Nodes)):
    print (round(layer1Nodes[i].getValue(),3), end="")
    print ("   ", end="")

  print("\n")

  for i in range(len(layer1Nodes)):
    print (roun(layer1Nodes[i].getWeightSet()), end="")
    print ("   ", end="")

  print("\n\n")


  print("\nLAYER 2\n")
  for i in range(len(layer2Nodes)):
    print (round(layer2Nodes[i].getValue(),3), end="")
    print ("   ", end="")

  print("\n")

  for i in range(len(layer2Nodes)):
    print (roun(layer2Nodes[i].getWeightSet()), end="")
    print ("   ", end="")

  print("\n\n")




  print("\nLAYER 3\n")
  for i in range(len(layer3Nodes)):
    print (round(layer3Nodes[i].getValue(),3), end="")
    print ("   ", end="")

  print("\n")

  for i in range(len(layer3Nodes)):
    print (roun(layer3Nodes[i].getWeightSet()), end="")
    print ("   ", end="")

  print("\n")


#makes le brain
layer0Nodes = [Layer0(0),Layer0(0),Layer0(0),Layer0(0),Layer0(0)]
layer1Nodes = [Layer1(), Layer1(),Layer1(), Layer1() ,Layer1(), Layer1(),Layer1(), Layer1(),Layer1(), Layer1(),Layer1(), Layer1(),Layer1(), Layer1()]
layer2Nodes = [Layer2(), Layer2(),Layer2(), Layer2() ,Layer2(), Layer2(),Layer2(), Layer2(),Layer2(), Layer2(),Layer2(), Layer2(),Layer2(), Layer2()]
layer3Nodes = [Layer3()]

topScoreList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
topWeightList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#generation 0
testNum = 1
while testNum < 1000:
  #make AI
  print("on test number: ", testNum)
  
  for node in layer1Nodes:
    node.defWeightSet()

  for node in layer2Nodes:
    node.defWeightSet()

  for node in layer3Nodes:
    node.defWeightSet()
    

  #do test
  problems = 0
  correct = 0
  handle = open("data.txt")
  for line in handle:#do 1000000 questions per test
    problems = problems + 1
    a = int(line.split()[0])
    b = int(line.split()[1])
    c = int(line.split()[2])
    d = int(line.split()[3])
    e = int(line.split()[4])
    answer = str(line.split()[5])#make inputs/answers from data.txt

    layer0Nodes[0].setValue(a/10)
    layer0Nodes[1].setValue(b/10)
    layer0Nodes[2].setValue(c/10)
    layer0Nodes[3].setValue(d/10)
    layer0Nodes[4].setValue(e/10)


    for node in layer1Nodes:
      node.updateValue()#updates layer one nodes based on the updated input layer

    for node in layer2Nodes:
      node.updateValue()#layer 2 reacts the the update of layer one

    for node in layer3Nodes:
      node.updateValue()#layer 3 is processed

    if layer3Nodes[0].getValue()<.5:#<.5 is the AI guessing false, >.5 is guessign true
      guess = "False"

    else:
      guess = "True"

    if guess == answer:#if it guessed forrectly, give it a point
      correct = correct +1

      
  #evaluate score
  
  newScore = correct/problems#score is a decimal of correct/number of problems(p)
  print(newScore)


  for i in range(len(topScoreList)):
    if (newScore > topScoreList[i]) and ((newScore in topScoreList) == False):
      store = topScoreList[i]
      topScoreList[i] = newScore
      newScore = store



      layer1Weights = []
      for node in layer1Nodes:
        layer1Weights.append(node.getWeightSet())

        
      layer2Weights = []
      for node in layer2Nodes:
        layer2Weights.append(node.getWeightSet())

        
      layer3Weights = []
      for node in layer3Nodes:
        layer3Weights.append(node.getWeightSet())

      newWeightSet = [layer1Weights,layer2Weights,layer3Weights]



      store = topWeightList[i]
      topWeightList[i] = newWeightSet
      newWeightSet = store
    

  testNum = testNum+1






#generation 1+
generation = 1
while generation < 1000:#number of generaitons
  print(topScoreList)
  print(topWeightList)
  testNum = 1
  while testNum < 200:


    parent1 = random.randint(0,len(topWeightList)-1)
    parent2 = random.randint(0,len(topWeightList)-1)
    parent3 = random.randint(0,len(topWeightList)-1)

    
    #genetic recombination\/\/\/\/\/
    for j in range(len(layer1Nodes)):
      newWS = []
      for i in range(len(layer1Nodes[j].getWeightSet())):
        newWS.append((((topWeightList[parent1][0][j][i])+(topWeightList[parent2][0][j][i])+(topWeightList[parent3][0][j][i]))/3)+random.randint(-999999,999999)/9999999.0)

      layer1Nodes[j].setWeightSet(newWS)




    for j in range(len(layer2Nodes)):
      newWS = []
      for i in range(len(layer2Nodes[j].getWeightSet())):
        newWS.append((((topWeightList[parent1][1][j][i])+(topWeightList[parent2][1][j][i])+(topWeightList[parent3][1][j][i]))/3)+random.randint(-999999,999999)/9999999.0)

      layer2Nodes[j].setWeightSet(newWS)



    for j in range(len(layer3Nodes)):
      newWS = []
      for i in range(len(layer3Nodes[j].getWeightSet())):
        newWS.append((((topWeightList[parent1][2][j][i])+(topWeightList[parent2][2][j][i])+(topWeightList[parent3][2][j][i]))/3)+random.randint(-999999,999999)/9999999.0)
      
      layer3Nodes[j].setWeightSet(newWS)
        




    #genetic recombination/\/\/\/\/\

    
    problems = 0
    correct = 0
    handle = open("data.txt")
    for line in handle:#do 1000000 questions per test
      problems = problems +1
      a = int(line.split()[0])
      b = int(line.split()[1])
      c = int(line.split()[2])
      d = int(line.split()[3])
      e = int(line.split()[4])
      answer = str(line.split()[5])#make inputs/answers from data.txt


      layer0Nodes[0].setValue(a/10)
      layer0Nodes[1].setValue(b/10)
      layer0Nodes[2].setValue(c/10)
      layer0Nodes[3].setValue(d/10)
      layer0Nodes[4].setValue(e/10)


      for node in layer1Nodes:
        node.updateValue()#updates layer one nodes based on the updated input layer

      for node in layer2Nodes:
        node.updateValue()#layer 2 reacts the the update of layer one

      for node in layer3Nodes:
        node.updateValue()#layer 3 is processed

      if layer3Nodes[0].getValue()<.5:#<.5 is the AI guessing false, >.5 is guessign true
        guess = "False"

      else:
        guess = "True"

      if guess == answer:#if it guessed forrectly, give it a point
        correct = correct +1


    #evaluate score
    newScore = correct/problems#score is a decimal of correct/number of problems(p)
    print("generation: ", generation, " test: ", testNum, " Score: " , newScore)


    for i in range(len(topScoreList)):
      if (newScore > topScoreList[i]) and ((newScore in topScoreList) == False):
        store = topScoreList[i]
        topScoreList[i] = newScore
        newScore = store



        layer1Weights = []
        for node in layer1Nodes:
          layer1Weights.append(node.getWeightSet())

          
        layer2Weights = []
        for node in layer2Nodes:
          layer2Weights.append(node.getWeightSet())

          
        layer3Weights = []
        for node in layer3Nodes:
          layer3Weights.append(node.getWeightSet())

        newWeightSet = [layer1Weights,layer2Weights,layer3Weights]



        store = topWeightList[i]
        topWeightList[i] = newWeightSet
        newWeightSet = store
      

    testNum = testNum+1
  generation = generation + 1















    


