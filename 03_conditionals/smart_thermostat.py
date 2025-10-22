device_status = "active"
temperature = 38
if device_status == "active":
    if temperature > 35:
        print("High Temperature alert")
    else:
        print("Temperature is Normal")
else:
    print("Device is Offline")