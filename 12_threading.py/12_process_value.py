from multiprocessing import Process,Value

def increment(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value+=1


if __name__ == "__main__":
    counter = Value('i' , 0)
    process =[Process(target=increment , args=(counter,))for _ in range(4)]
    [p.start() for p in process ]
    [p.join() for p in process] 
    
    print("final counter value: " , counter.value)