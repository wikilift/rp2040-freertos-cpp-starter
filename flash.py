import serial
import time
import os
import re
import shutil
import argparse
import subprocess

def get_project_name(cmake_file):
    project_name = None
    pattern = re.compile(
        r'set\s*\(\s*ProjectName\s+["\']?([^"\')\s]+)["\']?\s*\)',
        re.IGNORECASE
    )
    with open(cmake_file, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                project_name = match.group(1).strip()
                break
    return project_name


def enter_bootloader(port):
    print("Putting Raspberry Pi Pico in boot mode...")
    try:
        ser = serial.Serial(port, 1200)
        ser.close()
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return False
    return True

def wait_for_bootloader_mount(mount_point):
    print("Waiting for Raspberry Pi Pico to mount...")
    counter = 0
    while True:
        if os.path.exists(mount_point):
            mounts = os.listdir(mount_point)
            for mount in mounts:
                if "RPI-RP2" in mount:
                    print(f"Raspberry Pi Pico is ready at {mount_point}/{mount}")
                    print("Copying firmware")
                    return os.path.join(mount_point, mount)
        time.sleep(1)
        counter += 1
        if counter > 9:
            raise Exception("Timeout exception")

def copy_uf2_to_mount(project_name, build_path, mount_path):
    uf2_file = os.path.join(build_path, f"{project_name}.uf2")
    if os.path.isfile(uf2_file):
        shutil.copy(uf2_file, mount_path)
        print(f"Copied {uf2_file} to {mount_path}\nPico is ready to go!")
    else:
        print(f"{uf2_file} does not exist")

def open_serial_terminal(port, baud_rate=115200):
    try:
        subprocess.run(['gnome-terminal', '--', 'minicom', '-D', port, '-b', str(baud_rate)])
    except Exception as e:
        print(f"Failed to open serial terminal: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flash Raspberry Pi Pico with UF2 file")
    parser.add_argument('-c', '--cmake', default='CMakeLists.txt', help='Path to CMakeLists.txt file')
    parser.add_argument('-p', '--port', default='/dev/ttyACM0', help='Serial port of Raspberry Pi Pico')
    parser.add_argument('-m', '--mount', default='/media/dinux', help='Mount point for Raspberry Pi Pico')
    parser.add_argument('-b', '--build', default='build/src', help='Path to the directory containing the .uf2 file')
    parser.add_argument('-B', '--baud', default=115200, type=int, help='Baud rate for the serial connection')

    args = parser.parse_args()

    cmake_file = args.cmake
    port = args.port
    mount_point = args.mount
    build_path = args.build
    baud_rate = args.baud

    project_name = get_project_name(cmake_file)
    if project_name:
        if enter_bootloader(port):
            try:
                mount_path = wait_for_bootloader_mount(mount_point)
                if mount_path:
                    copy_uf2_to_mount(project_name, build_path, mount_path)
                    time.sleep(1)
                    open_serial_terminal(port, baud_rate) 
                else:
                    print("Cannot mount Pico in boot mode, please check wiring")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Failed to enter bootloader mode")
    else:
        print("Please first define ProjectName variable in CMakeLists.txt file")
