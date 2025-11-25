device_status = "active"
temperature = 45

if device_status == "active":
    if temperature > 35:
        print("WARNING!! High temperature!!")
    else:
        print("Temperature normal!!")
else:
    print("Device is offline!!")