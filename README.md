# Network To Serial bridge

ROS2 nodes to implement tcp_server->ROS2->serial_port data transfer

It may be helpful for some robotics applications:

- sending commands to robot controllers or boards connected via serial port converter

- sending RTK corrections to GNSS receiver connected via serial port (in case distribuition across the robots via ROS2 transport)

## Usage

Clone repo into *src* directory of your ROS2 workspace.

Build with *colcon build* command.

There are two nodes:

### network_ros_bridge

Can be used for receiving data from tcp server. All the received data packed into output ROS2 messages without any protocol handling or processing.

Output topics:

- **/output_topic** *ByteArray* message with payload

Parameters:

- **address** TCP server address

- **port** TCP server port

Launch:

```
ros2 run network_serial_bridge network_ros_bridge --ros-args --remap output_topic:=your_topic_name -p address:=tcp_server_ip -p port:=tcp_server_port
```

example:

```
ros2 run network_serial_bridge network_ros_bridge --ros-args --remap output_topic:=serial_command -p address:=192.168.0.5 -p port:=1235
```

### ros_serial_bridge

Sends received payload via serial port.

Input topics:

- **/input_topic** *ByteArray* with payload

Parameters:

- **port** serial port name

- **baud** serial port baudrate


Launch:

```
ros2 run network_serial_bridge ros_serial_bridge --ros-args --remap input_topic:=your_topic_name -p port:=device_path -p baud:=serial_baud
```

example:

```
ros2 run network_serial_bridge ros_serial_bridge --ros-args --remap input_topic:=serial_command -p port:=/dev/ttyUSB0 -p baud:=9600
```

## Limitations

Only single way communication supported - data can be only sent to serial port. If you would like to receive data via serial and send it back to ROS2 - there are some code extension required.

## License

Distributed under the 0BSD License. See `LICENSE.txt` for more information.

