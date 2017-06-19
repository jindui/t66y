# coding= utf-8
from multiprocessing import Pool

def f(x,y):
    print x,y

if __name__ == '__main__':
    pool = Pool(processes=4)
    print pool.map(f,[["12","34"],["56","78"]])