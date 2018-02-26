import sys
from time import time
from bcolors import bcolors

def quote(string):
    return "'" + string + "'"

def theme(string, color):
    return color + string + bcolors.ENDC


target_str = sys.argv[2]
answer = False
start = time()

with open(sys.argv[1], 'r') as f:

    beg = f.read(len(target_str))

    char = f.read(1)
    
    while char:
        if beg == target_str:
            print('\n' + theme(quote(sys.argv[2]),bcolors.OKBLUE) + theme(" was found in ", bcolors.OKGREEN) + theme(sys.argv[1],bcolors.BOLD))
            answer = True
            break
        
        beg = beg[1:] + char
        char = f.read(1)
    
    if not answer:
        print('\n' + theme(quote(sys.argv[2]),bcolors.OKBLUE) + theme(" was not found in ", bcolors.FAIL) + theme(sys.argv[1],bcolors.BOLD))

end = time() - start

print("Process took:{:6.2f} sec\n".format(end))
