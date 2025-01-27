""""
In this problem, you will try your solution on two different datasets: small and large
To test your solution on each one of them run the following in the terminal,
for small: 
    python autograder.py -p mars -s small

for large: 
    python autograder.py -p mars -s large

    
Additionally, there's a third file called martian_example, which you do not need to test, you can use it to understand the problem better. 
"""


def mars(day, month, year):
    #   Write your solution here!
    # The preprocessing is already done for you, implement your algorithm here, you're given one input case at a time through this function.
    # return result
    raise NotImplementedError


#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/mars/mars_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        d, m, y = map(int, fin.readline().split('.'))
        fout.write('%d\n' % mars(d, m, y))
    fin.close()
    fout.close()