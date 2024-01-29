import os
import math 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging
import warnings
warnings.filterwarnings('ignore')

def main():
    '''
    . For entropy code refer to the etropy() function.
    . For visualization, refer to visualize_entropy() function. 

    '''

    # Initiate logging
    set_logging()

    # Entropy
    logging.info('Testing entropy function on uniformly distributed outcomes...')
    probabilities = [0.25,0.25,0.25,0.25]
    print('='*20)
    print(f'entropy([0.25,0.25,0.25,0.25]) = {entropy(probabilities):.4f}')  # test entropy function 
    print('='*20)

    # Visualization for various probability distributions 
    logging.info('Generating a video animation for entropy of various probability distributations...')
    visualize_entropy()

def entropy(probabilities):
    '''
    . Compute entropy of a radnom variable given its probability distribution
    . Normalize entropy to [0,1] range
    '''
    curated_probabilities = [1e-10 if p == 0.0 else p for p in probabilities] #avoid math domain error when p = 0.0
    e = -sum(p * math.log2(p) for p in curated_probabilities)
    n = len(curated_probabilities)
    max_e = math.log2(n)
    normalized_e = e/max_e

    return normalized_e

def visualize_entropy():
    # Animation
    probabilities = [
        [1.0, 0.0, 0.0, 0.0],
        [0.6, 0.4, 0.0, 0.0],
        [0.5, 0.4, 0.1, 0.0],
        [0.4, 0.3, 0.2, 0.1],
        [0.25, 0.25, 0.25, 0.25]
    ]
    fig, ax = plt.subplots()
    bars = ax.bar(range(1, len(probabilities[0]) + 1), probabilities[0])

    def init():
        ax.set_xlim(0, len(probabilities[0]) + 1)
        ax.set_xticklabels(['', '$%s$' %r'x_1', '$%s$' %r'x_2', '$%s$' %r'x_3', '$%s$' %r'x_4', ''])
        ax.set_ylim(0, 1.1)
        ax.set_xlabel('Outcome')
        ax.set_ylabel('Probability')
        ax.set_title('Normalized Entropy')
        return bars
    
    def update(frame):
        for bar, h in zip(bars, probabilities[frame]):
            bar.set_height(h)
        
        ax.set_title(f'Normalized Entropy = {entropy(probabilities[frame]):.4f}' + f'\n Probabilities = {probabilities[frame]}')
        return bars

    animation = FuncAnimation(fig, update, frames=len(probabilities), init_func=init, blit=True, interval=5)
    video_path = os.path.join(os.getcwd(),'entropy.mp4')
    animation.save(video_path, writer='ffmpeg', fps=0.5 , dpi = 300)
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