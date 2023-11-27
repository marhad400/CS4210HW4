#-------------------------------------------------------------------------
# AUTHOR: Mark Haddad
# FILENAME: perceptron.py
# SPECIFICATION: Iterating through learning rates and dats shuffling, comparing performance of Perceptrons and MLPs
# FOR: CS 4210- Assignment #4
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier #pip install scikit-learn==0.18.rc2 if needed
import numpy as np
import pandas as pd

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]

df = pd.read_csv('optdigits.tra', sep=',', header=None) #reading the data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to form the feature data for training
y_training = np.array(df.values)[:,-1]  #getting the last field to form the class label for training

df = pd.read_csv('optdigits.tes', sep=',', header=None) #reading the data by using Pandas library

X_test = np.array(df.values)[:,:64]    #getting the first 64 fields to form the feature data for test
y_test = np.array(df.values)[:,-1]     #getting the last field to form the class label for test

highest_accuracy = 0

for rate in n: #iterates over n

    for bool in r: #iterates over r

        #iterates over both algorithms
        #-->add your Pyhton code here
        perceptron = Perceptron(eta0=rate, shuffle=bool, max_iter=1000)
        ml_perceptron = MLPClassifier(activation='logistic', learning_rate_init=rate, hidden_layer_sizes=(25,))

        algorithms = [perceptron, ml_perceptron]

        for algorithm in algorithms: #iterates over the algorithms

            #Create a Neural Network classifier
            #if Perceptron then
            #   clf = Perceptron()    #use those hyperparameters: eta0 = learning rate, shuffle = shuffle the training data, max_iter=1000
            #else:
            #   clf = MLPClassifier() #use those hyperparameters: activation='logistic', learning_rate_init = learning rate,
            #                          hidden_layer_sizes = number of neurons in the ith hidden layer - use 1 hidden layer with 25 neurons,
            #                          shuffle = shuffle the training data, max_iter=1000
            #-->add your Pyhton code here
            if algorithm == perceptron:
                clf = perceptron
            else:
                clf = ml_perceptron

            #Fit the Neural Network to the training data
            clf.fit(X_training, y_training)

            #make the classifier prediction for each test sample and start computing its accuracy
            #hint: to iterate over two collections simultaneously with zip() Example:
            #for (x_testSample, y_testSample) in zip(X_test, y_test):
            #to make a prediction do: clf.predict([x_testSample])
            #--> add your Python code here
            correct = 0
            total = 0
            predictions = clf.predict(X_test)
            for (x_testSample, y_testSample, prediction) in zip(X_test, y_test, predictions):
                if prediction == y_testSample:
                    correct += 1
                total += 1


            #check if the calculated accuracy is higher than the previously one calculated for each classifier. If so, update the highest accuracy
            #and print it together with the network hyperparameters
            #Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=0.01, shuffle=True"
            #Example: "Highest MLP accuracy so far: 0.90, Parameters: learning rate=0.02, shuffle=False"
            #--> add your Python code here
            accuracy = correct/total
            if accuracy > highest_accuracy:
                highest_accuracy = accuracy
            
            if algorithm == perceptron:
                print(f"Highest Perceptron accuracy so far: {highest_accuracy}, Parameters: learning rate={rate}, shuffle={r}")
            else:
                print(f"Highest MLP accuracy so far: {highest_accuracy}, Parameters: learning rate={rate}, ")











