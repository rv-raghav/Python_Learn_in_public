# You're building a smart thermostat alert system:
# if the device_status is "active"
# And temperatre > 35 -> warn: "high temperature alert!"
# else: "temperature normal"
# if device is off -> "Device is offline"

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("high temperature alert")
    else:
        print("temperature is normal")
else:
    print("device is offline")