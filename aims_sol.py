""""
In this problem, you will try your solution on three different datasets: small, medium, and large
To test your solution on each one of them run the following in the terminal,
for small: 
    python autograder.py -p aims -s small

for medium: 
    python autograder.py -p aims -s medium

for large: 
    python autograder.py -p aims -s large

"""

def aims(n, S):
    #   Write your solution here!
    # The preprocessing is already done for you, implement your algorithm here, you're given one input case at a time through this function.
    # n is the length of the string S
    # return result
    raise NotImplementedError

#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/aims/aims_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        n = int(fin.readline())
        S = fin.readline()[:-1]
        assert len(S) == n
        fout.write('%d\n' % aims(n, S))
    fin.close()
    fout.close()