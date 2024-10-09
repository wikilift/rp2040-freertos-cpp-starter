# Raspberry Pi Pico FreeRTOS and C/C++ ready to go 🚀

This project provides a ready-to-use setup for developing with the Raspberry Pi Pico using FreeRTOS and C/C++. It includes scripts to automate the process of flashing the firmware and opening a serial terminal to monitor the output.

  

## Cloning the Project

  

To get started, clone the project repository from GitHub:

  

```sh

git  clone  https://github.com/wikilift/rp2040-freertos-cpp-base.git

cd  rp2040-freertos-cpp-base

```

## Requirements📚

-  **CMake**: Used to generate build files for the project.

-  **Raspberry Pi Pico SDK**: Includes necessary tools and libraries for Raspberry Pi Pico development.

-  **GNU Arm Embedded Toolchain**: Required to compile firmware for Raspberry Pi Pico.

-  **FreeRTOS-Kernel**: Make sure the FreeRTOS-Kernel directory is present in your Pico SDK. For example, the path should look like:
``bash
			pi-pico/sdk/FreeRTOS-Kernel``


## Building the Project

Before using the flash script, you need to compile the project manually. 
  You can do this in one of two ways:
  - Using `make` from the command line:
  ```bash
  mkdir -p build
cd build
cmake ..
make
```
-**Using the Raspberry Pi Pico Extension in VSCode:**

-   Open the root folder of the project as your workspace.
-   Use the "Build" button from the Pico SDK extension toolbar.
-   Make sure the Raspberry Pi Pico SDK and `CMakeLists.txt` are correctly set up in your environment.

You can use the provided Python script to automate the build process.

This script will create the build directory, run `cmake`, and then `ninja` to build the project.

  

## Flash Script
The provided script `flash.py` automates the process of flashing the `.uf2` firmware file to a Raspberry Pi Pico and then opens a serial terminal to monitor its output. This script is particularly useful for developers who want to speed up the testing and debugging process of their microcontroller projects.
  
  

## Script Requirements📚

  

To run the script, ensure you have the following installed:

  

-  **Python 3.x**: Required to run the script.

-  **Minicom**: Serial communication tool. Install on Linux with:

``sh

sudo apt-get install minicom

``

  

-  **PySerial**: Serial communication library. Install with:

`pip install pyserial`

  

  
  
  

## Usage👁️

  

### Script Parameters

  

The script accepts several parameters to customize its operation:

  

-  `-c`, `--cmake`: Path to the `CMakeLists.txt` file. Default is `CMakeLists.txt`.

-  `-p`, `--port`: Serial port of the Raspberry Pi Pico. Default is `/dev/ttyACM0`.

-  `-m`, `--mount`: Mount point for the Raspberry Pi Pico in bootloader mode. Default is `/media/dinux`.

-  `-b`, `--build`: Path to the directory containing the `.uf2` file. Default is `build/src`.

-  `-B`, `--baud`: Baud rate for the serial connection. Default is `115200`.

  

### Example Execution📚

```py

python flash.py -c path/to/CMakeLists.txt -p /dev/ttyACM0 -m /media/dinux -b build/src -B 115200

```

This command will flash the `.uf2` file to the Raspberry Pi Pico connected to the port `/dev/ttyACM0`, and then open `minicom` at 115200 baud to monitor the serial output.

  

### Flashing Process Description📕

  

1.  **Get Project Name**: The script looks for the line `set(ProjectName <name>)` in the `CMakeLists.txt` file to identify the project name.

2.  **Enter Bootloader Mode**: The Raspberry Pi Pico is rebooted into bootloader mode by sending a serial command at 1200 baud.

3.  **Wait for Mount**: The script waits until the Pico is mounted at the specified mount point (`/media/userOS/RPI-RP2`).

4.  **Copy Firmware**: Once mounted, the `.uf2` file is copied to the mounted directory.

5.  **Open Serial Terminal**: Finally, the script opens `minicom` to monitor the serial output from the Pico.

### Notes📜

  

- Ensure `minicom` is properly configured for your environment.

- If you experience issues with serial port permissions, you may need to add your user to the `dialout` group:

`sudo usermod -aG dialout $USER`

  **Adding Global Libraries**:  
To include a library globally, copy the library files to the `pi-pico/sdk/lib` directory and add its subdirectory path to your `CMakeLists.txt` file using:
```bash
add_subdirectory(${PICO_SDK_PATH}/lib/your_library_name)
```
## License

  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.