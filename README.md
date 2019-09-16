Austin Pipkins python project

# Artificial Intellegence project

**Objective**

The goal of this project was to make a neural network and train it using test data

**Description**

The nerual network has four layers in total: one input layer, two hidden layers, and one output layer.

Each layer consists of nodes or "neurons". Each node has a value and weight set.

The value of each neuron is determined by a sumation of each node in the previous layer by its coorisponding weight in the weight set. It's value ranges form zero to one (to do this, thje sumation is inserted into the sigmoid function).

The input layer has five nodes, one for each input digit. Each of these input digits range from zero to nine, so to normalize these values to fit the zero to one node value limit, each value is divided by 10.

The two hidden layers have six neurons each. Their values are determined by the described equation.

The output layer has only one layer, whose value determines the guess of the neural network.(<50 is false, >50 is true)

**Training data**

The training data for this AI is made by another python script.

This code generates five random numbers between zero and nine, and processes those numbers through an arbitrary boolean statement.

This testing data is in the format of:
    
    # # # # # True
    # # # # # True
    # # # # # False
    ...
    
The goal of the AI is to find the pattern in the data (the boolean) and gain the ability to predict if an unseen data set falls under the true or false label.


