from ds_ml_utils.classification import Classification as classification_class
import numpy as np

classification = classification_class()

def test_loss_function_1():
    # 1 zero in training_set_X
    training_set_X = np.zeros(1)
    print("training_set_X = ", training_set_X)
    # 1 zero in training_set_Y
    training_set_Y = np.zeros(1)
    print("training_set_Y = ", training_set_Y)
    # 1 zero in weights
    weights = np.zeros(1)
    print("weights = ", weights)
    # zero for the bias
    bias = 0

    # np.dot(weights, x_0) + bias = 0
    # f_x_0 = sigmoid(0) = 1/2
    # y_0 = 0
    # loss_for_example_0 = -0*np.log(1/2) - (1-0)*np.log(1-1/2) 
    #                    = -log(1/2)
    #                    = log(2)

    result = classification.loss_function(training_set_X, training_set_Y, weights, bias) 
    assert(result == np.log(2))

def test_loss_function_2():
    # 2 zeros in training_set_X
    training_set_X = np.zeros(2)
    print("training_set_X = ", training_set_X)
    # 2 zeros in training_set_Y
    training_set_Y = np.zeros(2)
    print("training_set_Y = ", training_set_Y)
    # 2 zeros in weights
    weights = np.zeros(1)
    print("weights = ", weights)
    # zero for the bias
    bias = 0

    result = classification.loss_function(training_set_X, training_set_Y, weights, bias)
    assert(result == np.log(2))

def test_loss_function_3():
    # 2 sets of 5 zeros in training_set_X
    training_set_X = np.zeros((2,5))
    print(f'''training_set_X = 
           -->{training_set_X}<--''')
    # 2 zeros in training_set_Y
    training_set_Y = np.zeros(2)
    print("training_set_Y = ", training_set_Y)
    # 5 zeros in weights
    weights = np.zeros(5)
    print("weights = ", weights)
    # zero for the bias
    bias = 0

    result = classification.loss_function(training_set_X, training_set_Y, weights, bias)
    assert(result == np.log(2))
    

