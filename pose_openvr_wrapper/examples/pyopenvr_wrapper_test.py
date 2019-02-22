"""Example script using openvr_wrapper."""
import pose_openvr_wrapper
from pose_transform import Transform
# from pose_transform import rotation_matrix
import pprint
import numpy as np
import time

if __name__ == '__main__':
    pyopenvr_wrapper = pose_openvr_wrapper.OpenvrWrapper('../config.json')
    print(pyopenvr_wrapper.devices)

    # samples = pyopenvr_wrapper.sample('tracker_0', samples_count=10)
    # relative_samples = pyopenvr_wrapper.sample(
    #     ref_device_key='tracking_reference_1',
    #     target_device_key='tracker_0', samples_count=10)
    while True:
        # corrected_matrices = {key: Transform(
        #     pyopenvr_wrapper.get_corrected_transformation_matrix(
        #         key, samples_count=1000)) for key in pyopenvr_wrapper.devices}

        deux_en_un = Transform(
            pyopenvr_wrapper.get_corrected_transformation_matrix(
                target_device_key='tracking_reference_0',
                ref_device_key='tracker_2',
                samples_count=1))
        # un_par_un = corrected_matrices['tracking_reference_0'].relative_transform(
        #       corrected_matrices['tracker_0'])
        # print(un_par_un.matrix - deux_en_un.matrix)
        print(deux_en_un)
        # time.sleep(0.5)
        # Transform(
        #     pyopenvr_wrapper.get_corrected_transformation_matrix(
        #         key, samples_count=1)) for key in pyopenvr_wrapper.devices
        # print(corrected_matrices['tracker_2'].relative_transform(
        #       corrected_matrices['tracking_reference_0']))
        # print(corrected_matrices['tracking_reference_0'].relative_transform(
        #       corrected_matrices['tracker_2']))


    # print(samples)
    # print(relative_samples)
    # print(pyopenvr_wrapper.get_devices_count('tracker'))
    # print(pyopenvr_wrapper.get_devices_count())
    # pprint.pprint(matrices)
    # pprint.pprint(corrected_matrices)
