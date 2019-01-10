from wrapper import OpenvrWrapper
import argparse
import pprint
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', help='device to read', type=str,
                    default='tracker_0', choices=['tracker_0', 'tracker_1',
                                                  'tracker_2'])

parser.add_argument('-r', '--reference', help='ref lighthouse', type=str,
                    default='tracking_reference_1',
                    choices=['tracking_reference_0', 'tracking_reference_1'])

parser.add_argument('-f', '--frequency', help='read frequency', type=float,
                    default=250)

parser.add_argument('-s', '--samples', help='number of samples to read',
                    type=int, default=1000)

parser.add_argument('-fi', '--file', help='file to write',
                    type=str)

parser.add_argument('-n', '--lighthouses_count', help='currently visible '
                    'lighthouses count', type=int)

args = parser.parse_args()

pretty_printer = pprint.PrettyPrinter(indent=4)

vr = OpenvrWrapper('cfg/config.json')
pretty_printer.pprint(vr.devices)

if args.lighthouses_count:
    lighthouses_count = args.lighthouses_count
else:
    lighthouses_count = vr.get_devices_count('tracking_reference')

if args.file:
    data = vr.sample(target_device_key=args.device,
                     ref_device_key=args.reference,
                     samples_count=args.samples,
                     sampling_frequency=args.frequency)
    pose_dataframe = pd.DataFrame(data=data)
    pose_dataframe = pose_dataframe.assign(lighthouses_count=pd.Series(
        [lighthouses_count]*len(pose_dataframe)).values)
    pose_dataframe.to_csv('{}_raw'.format(args.file), index=False)
    pretty_printer.pprint(pose_dataframe)
    print("translation {} succesfully written to {}".format(
        '{0}-{1}'.format(args.reference, args.device), args.file))
else:
    while(1):
        data = vr.sample(target_device_key=args.device,
                         ref_device_key=args.reference,
                         samples_count=args.samples,
                         sampling_frequency=args.frequency)
        print('roll', np.mean(data['roll']))
        print('pitch', np.mean(data['pitch']))
        print('yaw', np.mean(data['yaw']))
        print('x', np.mean(data['x']))
        print('y', np.mean(data['y']))
        print('z', np.mean(data['z']))
