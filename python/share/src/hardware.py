import pyopencl as cl

def getDevices():
    devices: list[cl.Device] = list()
    platforms: list[cl.Platform] = list()
    try:
        platforms = cl.get_platforms()
    except:
        return devices
        
    for platform in platforms:
        for device in platform.get_devices():
            devices.append(device)
    return devices
