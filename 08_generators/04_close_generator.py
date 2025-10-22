def local_chai():
    yield "Masala Chai"
    yield "ginger Chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
for chai in full_menu():
    print(chai)
    
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall Closed , NO more Chai ")

stall = chai_stall()
print(next(stall))

stall.close()  # cleanup to cleaup our memory 