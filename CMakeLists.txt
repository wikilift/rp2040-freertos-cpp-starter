# == DO NEVER EDIT THE NEXT LINES for Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.0.0)
set(toolchainVersion 13_2_Rel1)
set(picotoolVersion 2.0.0)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
cmake_minimum_required(VERSION 3.12)

# Name project
SET(ProjectName freeRtos_Base_CPP)

# Set any variables required for importing libraries
SET(FREERTOS_KERNEL_PATH "/home/dinux/.pico-sdk/FreeRTOS-Kernel")

# Import those libraries
include(pico_sdk_import.cmake)
include(${FREERTOS_KERNEL_PATH}/portable/ThirdParty/GCC/RP2040/FreeRTOS_Kernel_import.cmake)

# Define project
project(${ProjectName} LANGUAGES C CXX)

# Initialize the Raspberry Pi Pico SDK
pico_sdk_init()
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
# Add subdirectories
add_subdirectory(src)

target_compile_definitions(${ProjectName} PRIVATE PICO_ENTER_USB_BOOT_ON_EXIT=1)
# if you have anything in "lib" folder then uncomment below - remember to add a CMakeLists.txt
# file to the "lib" directory
#add_subdirectory(lib)