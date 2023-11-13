import numpy as np
import multiprocessing as mp
from memory_profiler import profile

@profile
def get_ram(mem_mb):
    return np.random.rand(mem_mb * 125000)

@profile
def main():
    with mp.Pool(2) as pool:
        pool.map(get_ram, [512, 1024])

if __name__ == '__main__':
    main()
 