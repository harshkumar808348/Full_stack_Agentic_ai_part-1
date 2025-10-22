

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type    # non local means from inside to inside function
        chai_type = "kesar"
    kitchen()
    print("After kitchen update," , chai_type)
    
update_order()