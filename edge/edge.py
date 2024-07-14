import edgex_device_sdk_python as edgex

class AuroraAxiomEdge:
    def __init__(self):
        self.device_service = edgex.DeviceService()

    def add_device(self, device_name, device_profile_name, device_address):
        self.device_service.add_device(device_name, device_profile_name, device_address)

    def read_device_data(self, device_name):
        device = self.device_service.get_device(device_name)
        return device.read_value()

edge = AuroraAxiomEdge()
