import math
import argparse


# Function for calculating the P-Norm of an array
def p_norm(*args):
    if len(args) == 1:
        output = math.sqrt(sum([abs(i) ** 2 for i in args[0]]))
    else:
        if args[1] != 0:  # When p!=0
            output = math.pow(sum([abs(i) ** args[1] for i in args[0]]), 1 / args[1])
        else:  # L0 Norm case (p=0)
            output = len(list(filter(lambda x: x != 0, args[0])))
    return print("Norm of", args[0], "is", "{:0.2f}".format(output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=float, nargs='+',
                        help='integer array input')
    parser.add_argument('--p', nargs='?', type=int)
    arguments = parser.parse_args()
    p = arguments.p
    numlist = arguments.integers
    if p is None:
        p_norm(numlist)
    else:
        p_norm(numlist,p)
