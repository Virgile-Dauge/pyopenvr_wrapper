"""Convenient and simple wrapper of pyopenvr Library.

DESCRIPTION
===========
The focus is given on the easy acces of one specific pose transformation,

FILES
=====
Reads a file, ''config.json''. :: Which is required for keeping devices numbers
 consistent with their respectives serials numbers
"""

import openvr
import json
import time
import math
import numpy as np


class OpenvrWrapper():
    def __init__(self, path='config.json'):
        # Initialize OpenVR
        self.vr = openvr.init(openvr.VRApplication_Other)

        self.devices = {}

        # Loading config file
        self.config = None
        try:
            with open(path) as json_data:
                self.config = json.load(json_data)
        except EnvironmentError:# parent of IOError, OSError
            print('required config.json not found, closing.')
            exit(1)

        poses = self.vr.getDeviceToAbsoluteTrackingPose(
            openvr.TrackingUniverseStanding, 0,
            openvr.k_unMaxTrackedDeviceCount)
        # Iterate through the pose list to find the active devices and
        # determine their type
        for i in range(openvr.k_unMaxTrackedDeviceCount):
            if poses[i].bPoseIsValid:
                device_serial = self.vr.getStringTrackedDeviceProperty(
                    i, openvr.Prop_SerialNumber_String).decode('utf-8')

                for device in self.config['devices']:
                    if device_serial == device['serial']:
                        self.devices[device['name']] = device
                        device['index'] = i

    def sample(self, target_device_key, ref_device_key=None,
               num_samples=1000, sample_rate=250):
        interval = 1/sample_rate
        rtn = {'time': [], 'x': [], 'y': [], 'z': [],
               'r_x': [], 'r_y': [], 'r_z': [], 'r_w': [],
               'roll': [], 'pitch': [], 'yaw': [],
               'matrix': []}

        sample_start = time.time()
        for i in range(num_samples):
            start = time.time()
            mat = self.get_pose(target_device_key=target_device_key,
                                ref_device_key=ref_device_key)
            # Append to dict
            rtn['time'].append(time.time()-sample_start)
            rtn['matrix'].append(np.asarray(mat))
            rtn['x'].append(mat[0][3])
            rtn['y'].append(mat[1][3])
            rtn['z'].append(mat[2][3])
            rtn['yaw'].append(180 / math.pi * math.atan(mat[1][0] /
                                                        mat[0][0]))
            rtn['pitch'].append(180 / math.pi * math.atan(
                -1 * mat[2][0] / math.sqrt(pow(mat[2][1], 2) +
                                           math.pow(mat[2][2], 2))))
            rtn['roll'].append(180 / math.pi * math.atan(mat[2][1] /
                                                         mat[2][2]))
            r_w = math.sqrt(abs(1+mat[0][0]+mat[1][1]+mat[2][2]))/2
            rtn['r_w'].append(r_w)
            rtn['r_x'].append((mat[2][1]-mat[1][2])/(4*r_w))
            rtn['r_y'].append((mat[0][2]-mat[2][0])/(4*r_w))
            rtn['r_z'].append((mat[1][0]-mat[0][1])/(4*r_w))
            sleep_time = interval - (time.time()-start)
            if sleep_time > 0:
                time.sleep(sleep_time)
        return rtn

    def get_pose(self, target_device_key, ref_device_key=None):
        poses = self.vr.getDeviceToAbsoluteTrackingPose(
            openvr.TrackingUniverseStanding, 0,
            openvr.k_unMaxTrackedDeviceCount)
        target_id = self.devices[target_device_key]['index']
        if ref_device_key is None:
            return poses[target_id].mDeviceToAbsoluteTracking.m
        else:
            ref_id = self.devices[ref_device_key]['index']
            ref = np.asarray(poses[ref_id].mDeviceToAbsoluteTracking.m)
            dev = np.ndarray((4, 4))
            dev[0:3, 0:4] = np.asarray(
                poses[target_id].mDeviceToAbsoluteTracking.m)

            dev[3:4:1, :] = [0, 0, 0, 1]
            return np.matmul(self.inverse(ref), dev)

    def inverse(self, transformation_matrix):
        """Return the inverse of the given transformation matrix."""
        transformation_matrix = np.asarray(transformation_matrix)
        # Extraction of rotation matrix
        rotation_matrix = transformation_matrix[0:3:1, 0:3:1]
        # Exraction of translation vector
        translation_vector = transformation_matrix[0:3:1, 3:4:1]
        transposed_rotation_matrix = np.transpose(rotation_matrix)

        rotated_translation_vector = -transposed_rotation_matrix.dot(
            translation_vector)

        res_transformation_matrix = np.ndarray((4, 4))
        res_transformation_matrix[0:3:1, 0:3:1] = transposed_rotation_matrix
        res_transformation_matrix[0:3:1, 3:4:1] = rotated_translation_vector
        res_transformation_matrix[3:4:1, :] = [0, 0, 0, 1]
        return res_transformation_matrix
