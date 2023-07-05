import matplotlib.pyplot as plt

class Plotting:
    import matplotlib.pyplot as plt

    def plot_dataset(self, x, y, title, x_label, y_label):
        plt.scatter(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()
