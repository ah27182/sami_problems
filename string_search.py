import sys
from time import time
from bcolors import bcolors

def quote(string):
    return "'" + string + "'"

def color(string, color):
    return color + string + bcolors.ENDC


target_str = sys.argv[2]
answer = False
start = time()

with open(sys.argv[1], 'r') as f:

    beg = f.read(len(target_str))

    char = f.read(1)
    
    while char:
        if beg == target_str:
            print('\n' + color(quote(sys.argv[2]),bcolors.OKBLUE) + color(" was found in ", bcolors.OKGREEN) + color(sys.argv[1],bcolors.BOLD) + '\n')
            answer = True
            break
        
        beg = beg[1:] + char
        char = f.read(1)
    
    if not answer:
        print('\n' + color(quote(sys.argv[2]),bcolors.OKBLUE) + color(" was not found in ", bcolors.FAIL) + color(sys.argv[1],bcolors.BOLD) + '\n')

end = time() - start

print("Process took:{:6.2f} sec".format(end))
