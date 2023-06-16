from setuptools import setup

package_name = 'network_serial_bridge'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vladimir Leushkin',
    maintainer_email='vleushkin@gmail.com',
    description='Network to serial port bridge utilities',
    license='0BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros_serial_bridge = network_serial_bridge.ros_serial_bridge:main',
            'network_ros_bridge = network_serial_bridge.network_ros_bridge:main'
            
        ],
    },
)
