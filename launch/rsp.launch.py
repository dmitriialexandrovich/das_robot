# Необходимые включения
import os
import xacro
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('das_robot')) # Получаем адрес пакета с описанием робота 
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro') # Получаем файл xacro для парсинга 
    robot_description_config = xacro.process_file(xacro_file).toxml() # Парсим файл описания робота для передачи в robot_state_publisher

    params = {'robot_description': robot_description_config} # Создаем переменную с параметрами для ноды
    node_robot_state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen', parameters=[params]) # Создаем ноду
    return LaunchDescription([node_robot_state_publisher]) # Возвращаем готовую ноду