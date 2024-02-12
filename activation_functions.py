'''
Activation functions. An essential part of any deep learning model.

'''
import matplotlib.pyplot as plt
import numpy as np
import imageio
import warnings
warnings.filterwarnings('ignore')

def main():
    '''Create gif animation out of the activation functions and their derivativs plots'''
    x_vector = np.linspace(-5,5, 500)
    frames = []
    labels = {0: 'sigmoid', 1:'relu', 2:'leaky relu'}
    activations = {
        0: {'f': sigmoid, 'der': sigmoid_derivative},
        1: {'f': relu, 'der': relu_derivative},
        2: {'f': leaky_relu, 'der': leaky_relu_derivative}
    }

    for i in range(3):
        f = [activations[i]['f'](x) for x in x_vector]
        der = [activations[i]['der'](x) for x in x_vector]
        plt.plot(x_vector, f, color = 'blue', linewidth = 3, label = labels[i])
        plt.plot(x_vector, der, color = 'orange', linewidth = 3, label = labels[i] + ' derivative')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        if i == 0:
            plt.ylim([0,1.2])
        else:
            plt.ylim([min(min(f), min(der)), max(max(f), max(der))])
        plt.xlim([-5.3,5.3])
        if i == 2:
            plt.title(labels[i] + ' activation function: alpha = 0.2')
        else:
            plt.title(labels[i] + ' activation function')
        plt.grid()
        plt.legend()
        plt.savefig(f"frame_{i}.png")
        plt.close()
        frames.append(imageio.imread(f"frame_{i}.png"))

    # save in current directory
    imageio.mimsave("activation_functions.gif", frames, duration = 1500)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def leaky_relu(x, alpha=0.2):
    return np.maximum(alpha * x, x)

def leaky_relu_derivative(x, alpha=0.2):
    return np.where(x > 0, 1, alpha)

if __name__ == "__main__":
    main()