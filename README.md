# Publis-PC-battery-status-over-BLE-

# Bluetooth Battery Percentage Monitor

This is a Python script to monitor the battery percentage of a Windows/Mac/Linux PC and send the data over Bluetooth Low Energy (BLE) to a mobile device running the NRF Connect app. This script uses the `psutil` library to read the battery percentage and the `bluepy` library to communicate with the BLE device.

## Installation

### Ubuntu

1. Clone this repository: `git clone https://github.com/your-username/battery-monitor.git`
2. Run the setup script: `bash ubuntu.sh`

### Windows

1. Download and install Python 3 from the official website: https://www.python.org/downloads/
2. Clone this repository: `git clone https://github.com/your-username/battery-monitor.git`
3. Run the setup script by double-clicking on the `windows.bat` file.

### macOS

1. Clone this repository: `git clone https://github.com/your-username/battery-monitor.git`
2. Run the setup script: `bash mac.sh`

## Usage

1. Connect your BLE device to your mobile device and open the NRF Connect app.
2. Find the service UUID and characteristic UUID of the BLE device using NRF Connect.
3. Get the MAC address of the BLE device.
4. Open a terminal window and navigate to the directory where the `main.py` file is located.
5. Run the command: 


## Finding Service UUID, Characteristic UUID, and MAC Address

### On the PC side

1. Make sure your BLE device is turned on and in range of your computer.
2. Install a BLE scanner tool on your computer, such as nRF Connect for Desktop or BlueZ.
3. Open the BLE scanner tool and start scanning for BLE devices.
4. When you see your device in the list of scanned devices, click on it to see its details.
5. Look for the service UUID and characteristic UUID of your device in the details section.
6. Note the MAC address of your device, which is usually displayed in the format AA:BB:CC:DD:EE:FF.

### On the mobile side

1. Make sure your BLE device is turned on and in range of your mobile device.
2. Install a BLE scanner app on your mobile device, such as nRF Connect or LightBlue Explorer.
3. Open the BLE scanner app and start scanning for BLE devices.
4. When you see your device in the list of scanned devices, click on it to see its details.
5. Look for the service UUID and characteristic UUID of your device in the details section.
6. Note the MAC address of your device, which is usually displayed in the format AA:BB:CC:DD:EE:FF.
