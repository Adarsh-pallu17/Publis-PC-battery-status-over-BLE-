from battery import battery
from bluepy import btle
import argparse
import sys
import time

# Parse command-line arguments
parse = argparse.ArgumentParser(description='Send battery percentage to NRF connect app')
parse.add_argument('--service_uuid', help='Service UUID of the NRF connect app', required=True)
parse.add_argument('--characteristic_uuid', help='Characteristic UUID of NRF connect app', required=True)
parse.add_argument('--mac_address', help='MAC address of the Mobile where NRF connect app is present', required=True)
args = parse.parse_args()

# Check if all required arguments are provided
if not (args.service_uuid and args.characteristic_uuid and args.mac_address):
    print('Error: all arguments are required')
    sys.exit(1)

# NRF Connect App UUIDs
NRF_CONNECT_SERVICE_UUID = args.service_uuid
NRF_CONNECT_CHARACTERISTIC_UUID = args.characteristic_uuid

while True:
    try:
        percent = battery().percent
    except Exception as e:
        print('Error getting battery percentage:', e)
        continue

    percent_bytes = percent.to_bytes(1, byteorder="little")

    try:
        peripheral = btle.Peripheral(args.mac_address)
    except Exception as e:
        print('Error connecting to BLE device:', e)
        continue

    try:
        service = peripheral.getServiceByUUID(NRF_CONNECT_SERVICE_UUID)
        characteristic = service.getCharacteristics(NRF_CONNECT_CHARACTERISTIC_UUID)[0]
    except Exception as e:
        print('Error getting service/characteristic:', e)
        peripheral.disconnect()
        continue

    try:
        characteristic.write(percent_bytes)
    except Exception as e:
        print('Error sending data to BLE device:', e)
        peripheral.disconnect()
        continue

    try:
        peripheral.disconnect()
    except Exception as e:
        print('Error disconnecting from BLE device:', e)

    # Sleep for 200ms before next iteration
    time.sleep(0.2)
