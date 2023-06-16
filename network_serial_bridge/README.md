# ROS2Serial bridge

Utilities to implement tcp_server->ROS2->serial_port data transfer

It may be helpful for some robotics applications:

- sending commands to robot controllers or boards connected via serial port converter

- sending RTK corrections to GNSS receiver connected via serial port (in case distribuition across the robots via ROS2 transport)

There are two nodes:

## ros_serial_bridge

input data:

*byte array* with payload

Sends received payload via serial port.

## network_ros_bridge

Can be used for receiving data from tcp server. All the received data packed into output ROS2 messages.

output data:

*byte array* with payload

