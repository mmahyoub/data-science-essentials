import os 
import numpy as np 
import matplotlib.pyplot as plt
<<<<<<< HEAD
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings('ignore')
=======
>>>>>>> refs/remotes/origin/main

def main():
    # Define vectors and coefficients
    v1 = np.array([2, -1])   
    v2 = np.array([-1, 2])  
    c1 = 1               
    c2 = 2

    # Compute linear combination 
    result_vector = compute_lc_2(v1, v2, c1, c2)

    # Plot linear combination 
    plot_lc(result_vector, v1, v2, c1, c2)         

def compute_lc_2(v1,v2, c1, c2):
    '''
    Compute linear combination for two vectors. 

    Arguments:
        - v1: vector 1 (np.ndarray)
        - v2: vector 2 (np.ndarray)
        - c1: coefficient 1
        - c2: coefficient 2
    
    Output:
        - result_vector: the resultant vector of linear combination (np.ndarray)
    '''
    # Calculate the linear combination
    result_vector = c1 * v1 + c2 * v2
    return result_vector

def update(frame, lines, result_vector, v1, v2, c1, c2, legend_labels, legend_linecolors):
    if frame == 0:
        # Plot v1 
        lines.append(plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='$v_1$'))
        legend_handles = [plt.Line2D([0], [0], color=color, linewidth=2) for color in [legend_linecolors[0]]]
        plt.legend(handles=legend_handles, labels=legend_labels, loc='upper left')
    elif frame == 1:
        # Plot v2
        lines.append(plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='royalblue', label='$v_2$'))
        legend_handles = [plt.Line2D([0], [0], color=color, linewidth=2) for color in legend_linecolors[0:2]]
        plt.legend(handles=legend_handles, labels=legend_labels, loc='upper left')
    elif frame == 2:
        # Plot linear combination (c1 * v1)
        lines.append(plt.quiver(0, 0, c1 * v1[0], c1 * v1[1], angles='xy', scale_units='xy', scale=1, color='firebrick', label=str(c1) + '$v_1$'))
        legend_handles = [plt.Line2D([0], [0], color=color, linewidth=2) for color in legend_linecolors[0:3]]
        plt.legend(handles=legend_handles, labels=legend_labels, loc='upper left')
    elif frame == 3:
        # Plot linear combination (c2 * v2)
        lines.append(plt.quiver(c1 * v1[0], c1 * v1[1], c2 * v2[0], c2 * v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label=str(c2) + '$v_2$'))
        legend_handles = [plt.Line2D([0], [0], color=color, linewidth=2) for color in legend_linecolors[0:4]]
        plt.legend(handles=legend_handles, labels=legend_labels, loc='upper left')
    elif frame == 4:
        # Plot linear combination (c1 * v1 + c2 * v2)
        lines.append(plt.quiver(0, 0, result_vector[0], result_vector[1], angles='xy', scale_units='xy', scale=1, color='orange', label=str(c1) + '$v_1+$' + str(c2) + '$v_2$'))
        legend_handles = [plt.Line2D([0], [0], color=color, linewidth=2) for color in legend_linecolors[0:5]]
        plt.legend(handles=legend_handles, labels=legend_labels, loc='upper left')

def plot_lc(result_vector, v1, v2, c1, c2):
    plt.figure(figsize=(8, 8))
    plt.xlim(min((v1[0], v2[0], result_vector[0]))-2, max((v1[0], v2[0], result_vector[0])) + 2)
    plt.ylim(min((v1[1], v2[1], result_vector[1]))-2, max((v1[1], v2[1], result_vector[1])) + 2)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Linear Combination Visualization')
    plt.grid()
    
    # Create a list to store the lines for animation
    lines = []
    legend_labels = ['$v_1$', '$v_2$', str(c1) + '$v_1$', str(c2) + '$v_2$', str(c1) + '$v_1+$' + str(c2) + '$v_2$']
    legend_linecolors = ['red', 'royalblue', 'firebrick', 'blue', 'orange']
    
    # Use FuncAnimation to animate the drawing of quivers
    ani = FuncAnimation(plt.gcf(), update, fargs=(lines, result_vector, v1, v2, c1, c2, legend_labels, legend_linecolors), frames=5, repeat=False)

    # Save figure 
<<<<<<< HEAD
    figure_name = 'linear_combination_animation.gif'
    ani.save(os.path.join(os.getcwd(), figure_name), writer='pillow', fps=0.5)
=======
    figure_name = 'linear_combination.jpg'
    plt.savefig(os.path.join(os.getcwd(), figure_name), dpi = 600)

    plt.show()
>>>>>>> refs/remotes/origin/main

if __name__ == '__main__':
    main()
