import numpy as np

class Classification:

    # Sigmoid function
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # Loss function
    def loss_function(self, training_set_X,training_set_y, weights, bias ):
        # Getting the number of training examples
        m = training_set_X.shape[0]

        # Evaluating the loss 
        total_loss = 0
        for i in range(m):
            x_i = training_set_X[i]
            z_i = np.dot(weights, x_i) + bias
            f_x_i = self.sigmoid(z_i)
            y_i = training_set_y[i]

            loss_for_example_i = -y_i*np.log(f_x_i) - (1-y_i)*np.log(1-f_x_i)
            total_loss = total_loss + loss_for_example_i
        total_loss = total_loss / m

        return total_loss

