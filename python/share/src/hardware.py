import pyopencl as cl

def getDevices():
    devices: list[cl.Device] = list()
    for platform in cl.get_platforms():
        for device in platform.get_devices():
            devices.append(device)
    return devices
