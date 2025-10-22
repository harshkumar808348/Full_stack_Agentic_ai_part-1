from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")
    

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
        for i in range(3)
    ]
    
    # start all process 
    for p in chai_maker:
        p.start()
    
    
    #wait for all to complete
    for p in chai_maker:
        p.join()
        
    print("All chai serve")