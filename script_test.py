from multiprocessing import Pool
import sys

def f(x):
    x = float(x)
    return x*x*x

if __name__ == '__main__':
    # print(f(sys.argv[1]))
    test_list = sys.argv[1:]
    with Pool(4) as p:
        print(p.map(f, test_list))