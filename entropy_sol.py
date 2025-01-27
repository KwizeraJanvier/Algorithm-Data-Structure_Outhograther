
""""
To test your solution run the following in the terminal: 
    python autograder.py -p entropy
"""
import numpy as np

def entropy(alpha):

    #   Write your solution here!
    # The preprocessing is already done for you, implement your algorithm here, you're given one input case at a time through this function.
    # return result
    raise NotImplementedError


#################   DO NOT CHANGE BELOW ###########################
INPUT_NAME = 'datasets/entropy/entropy.in'
OUTPUT_NAME = 'datasets/entropy/entropy_sol.out'
def run_code():
    f = open(INPUT_NAME, 'r')
    
    fout = open(OUTPUT_NAME, 'w')
    
    n_tests = int(f.readline())
    for i in range(n_tests):
        alpha = float(f.readline())
        p_str = entropy(alpha)
        fout.write(str(p_str) + '\n')
    f.close()
    fout.close()







