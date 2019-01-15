"""Example script using openvr_wrapper."""
import pose_openvr_wrapper
import pprint

if __name__ == '__main__':
    pyopenvr_wrapper = pose_openvr_wrapper.OpenvrWrapper('cfg/config.json')
    print(pyopenvr_wrapper.devices)

    samples = pyopenvr_wrapper.sample('tracker_0', samples_count=10)
    relative_samples = pyopenvr_wrapper.sample(
        ref_device_key='tracking_reference_1',
        target_device_key='tracker_0', samples_count=10)

    print(samples)
    print(relative_samples)
    print(pyopenvr_wrapper.get_devices_count('tracker'))
    print(pyopenvr_wrapper.get_devices_count())
