"""Example script using openvr_wrapper."""
from wrapper import OpenvrWrapper
import pprint

if __name__ == '__main__':
    pyopenvr_wrapper = OpenvrWrapper('cfg/config.json')
    print(pyopenvr_wrapper.devices)
    samples = pyopenvr_wrapper.sample('tracker_1', num_samples=10)
    relative_samples = pyopenvr_wrapper.sample(
        ref_device_key='tracking_reference_1',
        target_device_key='tracker_1', num_samples=10)
    pretty_printer = pprint.PrettyPrinter()
    pretty_printer.pprint(samples)
    pretty_printer.pprint(relative_samples)
