cmake_minimum_required(VERSION 3.8)
project(ros2_np_multiarray)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(ament_cmake_python REQUIRED)

find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

find_package(std_msgs REQUIRED)



## Generate messages in the 'msg' folder
rosidl_generate_interfaces(${PROJECT_NAME}
  	"msg/Float32MultiArrayStamped.msg"
	"msg/Float64MultiArrayStamped.msg"
	"msg/Int8MultiArrayStamped.msg"
	"msg/Int16MultiArrayStamped.msg"
	"msg/Int32MultiArrayStamped.msg"
	"msg/Int64MultiArrayStamped.msg"
	"msg/UInt8MultiArrayStamped.msg"
	"msg/UInt16MultiArrayStamped.msg"
	"msg/UInt32MultiArrayStamped.msg"
	"msg/UInt64MultiArrayStamped.msg"
  DEPENDENCIES std_msgs  
)

ament_export_dependencies(rosidl_default_runtime)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
