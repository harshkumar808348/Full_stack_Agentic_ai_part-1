def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai..")
        if flavour == "unknown":
            raise ValueError("We don't Lnow that flavoude")
    except ValueError as e:
        print("Error" ,e)
        
    else:
        print(f"{flavour} chai is Served")
    finally:
        print("Next customeer please")
        
        
serve_chai("Masala")
serve_chai("unknown")