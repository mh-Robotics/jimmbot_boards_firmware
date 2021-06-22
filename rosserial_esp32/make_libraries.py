#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2019, Sachin Parekh
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rospkg
import rosserial_client
from rosserial_client.make_library import *

THIS_PACKAGE = "jimmbot_boards_firmware"

__usage__ = """
make_libraries.py generates the ESP32 rosserial library files for ESP32 (ESP-IDF).
It requires the location of your esp-idf/components folder.

rosrun jimmbot_boards_firmware make_libraries.py $IDF_PATH/components
"""

# for copying files
import shutil

ROS_TO_EMBEDDED_TYPES = {
    'bool'    :   ('bool',              1, PrimitiveDataType, []),
    'byte'    :   ('int8_t',            1, PrimitiveDataType, []),
    'int8'    :   ('int8_t',            1, PrimitiveDataType, []),
    'char'    :   ('char',              1, PrimitiveDataType, []),
    'uint8'   :   ('uint8_t',           1, PrimitiveDataType, []),
    'int16'   :   ('int16_t',           2, PrimitiveDataType, []),
    'uint16'  :   ('uint16_t',          2, PrimitiveDataType, []),
    'int32'   :   ('int32_t',           4, PrimitiveDataType, []),
    'uint32'  :   ('uint32_t',          4, PrimitiveDataType, []),
    'int64'   :   ('int64_t',           8, PrimitiveDataType, []),
    'uint64'  :   ('uint64_t',          8, PrimitiveDataType, []),
    'float32' :   ('float',             4, PrimitiveDataType, []),
    'float64' :   ('double',            8, PrimitiveDataType, []),
    'time'    :   ('ros::Time',         8, TimeDataType, ['ros/time']),
    'duration':   ('ros::Duration',     8, TimeDataType, ['ros/duration']),
    'string'  :   ('char*',             0, StringDataType, []),
    'Header'  :   ('std_msgs::Header',  0, MessageDataType, ['std_msgs/Header'])
}

# need correct inputs
if (len(sys.argv) < 2):
    print(__usage__)
    exit()

# get output path
path = sys.argv[1]

if path[-1] == "/":
    path = path[0:-1]
print("\nExporting to %s" % path)

rospack = rospkg.RosPack()

# Create jimmbot_boards_firmware component folder if it doesn't exists
if not os.path.exists(path+"/jimmbot_boards_firmware/"):
    os.makedirs(path+"/jimmbot_boards_firmware/include/")
    with open(path+"/jimmbot_boards_firmware/component.mk", "w") as file:
        pass

# copy ros_lib stuff in
jimmbot_boards_firmware_dir = rospack.get_path(THIS_PACKAGE)
files = os.listdir(jimmbot_boards_firmware_dir+"/ros_lib")
for f in files:
    if os.path.isfile(jimmbot_boards_firmware_dir+"/ros_lib/"+f):
        if f.endswith(".h"):
            shutil.copy(jimmbot_boards_firmware_dir+"/ros_lib/"+f, path+"/jimmbot_boards_firmware/include/")
        else:
            shutil.copy(jimmbot_boards_firmware_dir+"/ros_lib/"+f, path+"/jimmbot_boards_firmware/")

rosserial_client_copy_files(rospack, path+"/jimmbot_boards_firmware/include/")

# generate messages
rosserial_generate(rospack, path+"/jimmbot_boards_firmware/include/", ROS_TO_EMBEDDED_TYPES)

# Move source files to parent directory
src_files = os.listdir(path+"/jimmbot_boards_firmware/include/")
for f in src_files:
    if f.endswith(".cpp"):
        shutil.move(path+"/jimmbot_boards_firmware/include/"+f, path+"/jimmbot_boards_firmware/")
