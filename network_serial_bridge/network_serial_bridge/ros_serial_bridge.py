import rclpy
import serial

from rclpy.node import Node
from network_serial_bridge_msgs.msg import ByteArray

class SerialBridgeNode(Node):

  def __init__(self):
    super().__init__('serial_bridge')
    
    self.declare_parameter('port', '/dev/ttyUSB0')
    self.declare_parameter('baud', 115200)
          
    serial_port_name = self.get_parameter('port').get_parameter_value().string_value
    serial_baud_rate = self.get_parameter('baud').get_parameter_value().integer_value
  
    self.serial = serial.Serial(serial_port_name, serial_baud_rate)
    
    self.data_subscriber = self.create_subscription(
      ByteArray,
      '/input_topic',
      self.data_callback,
      10)
  
  def data_callback(self, msg):
    self.serial.write(msg.data)

def main(args=None):
  rclpy.init(args=args)
  
  serial_bridge_node = SerialBridgeNode()
  
  rclpy.spin(serial_bridge_node)
  
  serial_bridge_node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
