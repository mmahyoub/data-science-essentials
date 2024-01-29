import os 
import numpy as np 
import matplotlib.pyplot as plt
import logging

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

def plot_lc(result_vector, v1, v2, c1, c2):
    '''
    Arguments:
        - v1: vector 1 (np.ndarray)
        - v2: vector 2 (np.ndarray)
        - c1: coefficient 1
        - c2: coefficient 2
        - result_vector: result vector of linear combination (np.ndarray) 
    
    Output:
        - Plot of linear combination 
    '''
    plt.figure(figsize=(8, 8))
    # Plot vectors 
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='$v_1$')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='$v_2$')
    
    # Plot linear combination 
    plt.quiver(0, 0, result_vector[0], result_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label=str(c1) + '$v_1+$' + str(c2) + '$v_2$')
    plt.quiver(v1[0], v1[1], c2 * v2[0], c2 * v2[1] , angles = 'xy', scale_units = 'xy', scale = 1, color = 'k', label = str(c2) + '$v_2$' )

    plt.xlim(min((v1[0], v2[0], result_vector[0]))-2, max((v1[0], v2[0], result_vector[0])) + 2)
    plt.ylim(min((v1[1], v2[1], result_vector[1]))-2, max((v1[1], v2[1], result_vector[1])) + 2)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid()
    plt.title('Visualization of linear combination')
    # Save figure 
    figure_name = 'linear_combination.jpg'
    plt.savefig(os.path.join(os.getcwd(), figure_name), dpi = 600)

    plt.show()

def set_logging():
    logging.basicConfig(level=logging.INFO)
    console_handler =  logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

if __name__ == '__main__':
    main()
