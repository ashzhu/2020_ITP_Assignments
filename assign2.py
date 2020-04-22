from collections import defaultdict
seq = defaultdict(list)
sequence = input('Please input a sequence')
while bool(sequence):
    rc = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    tmp = ''
    i = 0
    test = 1
    for nt in sequence:
        test *= nt.upper() in ['A','T','G','C']
    if test != 1:
        print('Please enter a valid sequence')
        break
    else:
        seq[i] = sequence
        i += 1
    
    sequence = input('Please input a sequence')