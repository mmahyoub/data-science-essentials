import os
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import warnings
import logging
warnings.filterwarnings('ignore')

def main():
    set_logging()
    
    # Gradient descent
    logging.info('Running gradient descent algorithm on f(x)...')
    x_values, y_values = run_gradient_descent()

    # Visualization for various probability distributions 
    logging.info('Visualizing the optimization path...')
    visualize_gd(x_values, y_values)
    
def f(x):
    return (x-5)**2 + 1

def gradient(x):
    return 2 * (x-5) # derivative of (x-5)**2 + 1

def run_gradient_descent():   
    x = np.random.uniform(low=-5, high=15) #initial x
    epochs = 100 # number of iterations 
    lr = 0.1 # learning rate

    x_values = []
    y_values = []

    logging.info('GD algorithm starting...')
    for epoch in range(epochs):
        g = gradient(x)  # compute gradient at x
        x = x - lr * g # update x 
        x_values.append(x)
        y_values.append(f(x))

    logging.info('GD algorithm completed...') 
    print('='*15)  
    print('Gradient descent results for minimizing f(x) = (x-5)**2 + 1}:')
    print(f'x = {x:.2f}, f(x): {f(x):.2f}')
    print('='*15) 

    return x_values, y_values

def visualize_gd(x_values, y_values):
    # Create animation for the gradient descent on (x-5)**2+1
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'ro-', label='Optimization', lw = 2)
    ax.plot(np.linspace(-5, 15, 100), f(np.linspace(-5, 15, 100)), label='Objective Function: $%s$' %r'(x-5)^2 + 1', lw = 2)

    def init():
        ax.set_xlim(-6, 16)
        ax.set_ylim( 0 , f(16) + 4)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Gradient Descent Progression')
        ax.legend()
        return line,

    def update(frame):
        line.set_data(x_values[:frame], y_values[:frame])
        return line,

    animation = FuncAnimation(fig, update, frames=len(x_values), init_func=init, blit=True, interval=10)
    video_path = os.path.join(os.getcwd(),'gradient_descent_progression.mp4')
    animation.save(video_path, writer='ffmpeg', fps=5 , dpi = 300)
    logging.info(f'Video is generated and can be accessed as: {video_path}')

def set_logging():
    logging.basicConfig(level=logging.INFO)
    console_handler =  logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

if __name__ == '__main__':
    main()