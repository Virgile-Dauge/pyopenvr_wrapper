import ast
import json
import os.path as path
steam_dir = path.expanduser('~/.steam/steam')
sf = path.join(steam_dir, 'config/steamvr.vrsettings')
with open(sf, 'r') as f:
    cfg = json.load(f)

cfg['steamvr']['forcedDriver'] = 'null'
cfg['steamvr']['activateMultipleDrivers'] = True
cfg['steamvr']['requireHmd'] = False

driver_null = {
    "enable": True,
    "id": "Null Driver",
    "serialNumber": "Null 4711",
    "modelNumber": "Null Model Number",
    "windowX": 100,
    "windowY": 100,
    "windowWidth": 1920,
    "windowHeight": 1080,
    "renderWidth": 1344,
    "renderHeight": 1512,
    "secondsFromVsyncToPhotons": 0.1,
    "displayFrequency": 90
}
cfg['driver_null'] = driver_null
with open(sf, 'w') as f:
    cfg = json.dump(cfg, f, indent=4)
