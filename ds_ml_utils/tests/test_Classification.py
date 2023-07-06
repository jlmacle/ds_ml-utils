import pytest
from ds_ml_utils.classification import Classification as classification_class
import numpy as np

classification = classification_class()

def test_loss_function_1():
    # 1 zero in training_set_X
    training_set_X = np.zeros(1)
    # 1 zero in training_set_Y
    training_set_Y = np.zeros(1)
    # 1 zero in weights
    weights = np.zeros(1)
    # 1 zero in bias
    bias = 0

    # np.dot(weights, x_0) + bias = 0
    # f_x_0 = sigmoid(0) = 1/2
    # y_0 = 0
    # loss_for_example_0 = -0*np.log(1/2) - (1-0)*np.log(1-1/2) 
    #                    = -log(1/2)
    #                    = log(2)

    result = classification.loss_function(training_set_X, training_set_Y, weights, bias) 
    assert(result == np.log(2))


