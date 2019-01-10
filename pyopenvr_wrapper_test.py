"""Example script using openvr_wrapper."""
from wrapper import OpenvrWrapper
import pprint

if __name__ == '__main__':
    pyopenvr_wrapper = OpenvrWrapper('cfg/config.json')
    print(pyopenvr_wrapper.devices)
    samples = pyopenvr_wrapper.sample('tracker_0', samples_count=10)
    relative_samples = pyopenvr_wrapper.sample(
        ref_device_key='tracking_reference_1',
        target_device_key='tracker_0', samples_count=10)
    pretty_printer = pprint.PrettyPrinter()
    pretty_printer.pprint(samples)
    pretty_printer.pprint(relative_samples)
    print(pyopenvr_wrapper.get_devices_count('tracker'))
    print(pyopenvr_wrapper.get_devices_count())
