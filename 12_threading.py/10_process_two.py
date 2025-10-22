from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crusching some number..")
    total = 0
    for i in range(10**7):
        total+=i
    print("Done")
    
    
if __name__ == "__main__":
    start  = time.time()

    process = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in process]
    [t.join() for t in process]

    print(f"Time taken :{time.time()-start:.2f} seconds")