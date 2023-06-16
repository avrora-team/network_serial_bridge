import rclpy
import threading
import socket

from rclpy.node import Node
from network_serial_bridge_msgs.msg import ByteArray

class NetworkBridgeNode(Node):

  def __init__(self):
    super().__init__('network_bridge')
    
    self.data_publisher = self.create_publisher(ByteArray, '/output_topic', 10)
    
    self.declare_parameter('address', '127.0.0.1')
    self.declare_parameter('port', 1234)
    
    host = self.get_parameter('address').get_parameter_value().string_value
    port = self.get_parameter('port').get_parameter_value().integer_value
    
    self.listening_thread = threading.Thread(target=self.threaded_reading, args=[host, port])
    self.listening_thread.run()
  
  def threaded_reading(self, host, port):
  
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    while True:
      data = client_socket.recv(2048)

      if (len(data)==0):
        break
               
      message = ByteArray()
      message.data = list(data)
      
      self.data_publisher.publish(message)

def main(args=None):
  rclpy.init(args=args)
  
  network_bridge_node = NetworkBridgeNode()
  
  rclpy.spin(network_bridge_node)
  
  network_bridge_node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
