# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyummeter']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'pyummeter',
    'version': '0.2.0',
    'description': 'Python UM-Meter interface',
    'long_description': '[![CircleCI](https://dl.circleci.com/status-badge/img/gh/valletw/pyummeter/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/valletw/pyummeter/tree/main)\n\n# Python UM-Meter interface\n\nSupport RDTech UM24C, UM25C, UM34C.\n\n## Library usage\n\nOpen an UM-Meter interface and request data:\n\n```python\nfrom pyummeter import UMmeter, UMmeterInterfaceTTY\n\nwith UMmeter(UMmeterInterfaceTTY("/path/to/serial/port")) as meter:\n    data = meter.get_data()\n    print(f"{data[\'voltage\']} V / {data[\'power\']} W")\n```\n\nIt is also possible to export the data to a CSV file:\n\n```python\nfrom datetime import datetime\nfrom pyummeter import UMmeter, UMmeterInterfaceTTY\nfrom pyummeter.export_csv import ExportCSV\n\ncsv = ExportCSV("/path/to/csv")\nwith UMmeter(UMmeterInterfaceTTY("/path/to/serial/port")) as meter:\n    csv.update(datetime.now(), meter.get_data())\n```\n\nList of data available:\n\n- `model`: UM-Meter model name (*exported to CSV*)\n- `voltage`: Voltage (V) (*exported to CSV*)\n- `intensity`: Intensity (A) (*exported to CSV*)\n- `power`: Power (W) (*exported to CSV*)\n- `resistance`: Resistance (Ohm) (*exported to CSV*)\n- `usb_voltage_dp`: USB Voltage D+ (V) (*exported to CSV*)\n- `usb_voltage_dn`: USB Voltage D- (V) (*exported to CSV*)\n- `charging_mode`: Charging mode short name (*exported to CSV*)\n- `charging_mode_full`: Charging mode full name\n- `temperature_celsius`: Temperature (°C) (*exported to CSV*)\n- `temperature_fahrenheit`: Temperature (°F)\n- `data_group_selected`: Selected data group (index)\n- `data_group`: Data for each data group (list) (*exported to CSV, only the selected group*)\n  - `capacity`: Capacity (Ah)\n  - `energy`: Energy (Wh)\n- `record_capacity_threshold`: [Record mode] Capacity threshold (Ah) (*exported to CSV*)\n- `record_energy_threshold`: [Record mode] Energy threshold (Wh) (*exported to CSV*)\n- `record_intensity_threshold`: [Record mode] Intensity threshold (A) (*exported to CSV*)\n- `record_duration`: [Record mode] Duration (seconds) (*exported to CSV*)\n- `record_enabled`: [Record mode] Enable status (*exported to CSV*)\n- `screen_index`: Screen index\n- `screen_timeout`: Screen timeout\n- `screen_brightness`: Screen brightness\n- `checksum`: Checksum of all data\n\nMeter control managed (not available on all model):\n\n- Screen control:\n  - Change (next/previous)\n  - Rotate\n  - Set timeout (0 to 9 minutes)\n  - Set brightness (0 to 5)\n- Data group control:\n  - Select (0 to 9, next)\n  - Clear\n- Record threshold (0 to 300 mA)\n\n## Running example\n\n### Bluetooth initialisation\n\n```shell\n$ sudo killall rfcomm\n$ rfkill block bluetooth\n$ rfkill unblock bluetooth\n$ sudo bluetoothctl\n[bluetooth] power on\n[bluetooth] agent on\n[bluetooth] scan on\n[bluetooth] pair <MAC>\n$ sudo rfcomm connect /dev/rfcomm0 <MAC>\n```\n\n### Demo application usage\n\n```shell\npoetry install\npoetry run task demo -t /dev/rfcomm0\n```\n',
    'author': 'William Vallet',
    'author_email': 'valletw@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/valletw/pyummeter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
