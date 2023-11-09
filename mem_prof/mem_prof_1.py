import numpy as np
import time
from memory_profiler import profile

@profile
def main():
    
    mem_data = []

    for _ in range(5):

        mem_size_mb = 1024
        data = np.random.rand(mem_size_mb * 125000)
        mem_data.append(data)

        print(f'Allocated {len(mem_data)} of GB to memory')

        time.sleep(1)

if __name__ == '__main__':
    main()
