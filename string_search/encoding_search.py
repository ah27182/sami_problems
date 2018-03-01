import sys
from time import time
from bcolors import bcolors
from encoding import chr_encode, str_encode, base, modulus

def quote(string):
    return "'" + string + "'"

def theme(string, color):
    return color + string + bcolors.ENDC

target_str = sys.argv[2]
target_encoded = str_encode(target_str)
target_length = len(target_str)

answer = False
start = time()

with open(sys.argv[1], 'r') as f:

    buf = f.read(target_length)
    encoded_buf = str_encode(buf)

    iter_chr = f.read(1)
    
    while iter_chr:
        if encoded_buf == target_encoded and buf == target_str:
            print('\n' + theme(quote(sys.argv[2]),bcolors.OKBLUE) + theme(" was found in ", bcolors.OKGREEN) + theme(sys.argv[1],bcolors.BOLD))
            answer = True
            break
        
        buf = buf[1:] + iter_chr

        encoded_buf = (encoded_buf//base + chr_encode(iter_chr) * pow(base, target_length - 1, modulus)) % modulus
        iter_chr = f.read(1)
    
    if not answer:
        print('\n' + theme(quote(sys.argv[2]),bcolors.OKBLUE) + theme(" was not found in ", bcolors.FAIL) + theme(sys.argv[1],bcolors.BOLD))

end = time() - start

print("Process took:{:6.2f} sec\n".format(end))
