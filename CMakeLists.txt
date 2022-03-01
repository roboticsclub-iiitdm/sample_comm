cmake_minimum_required(VERSION 3.0.2)
project(sample_comm)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs)

include_directories(${catkin_INCLUDE_DIRS})

# add_executable(${PROJECT_NAME}_node src/sample_comm_node.cpp)

# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )