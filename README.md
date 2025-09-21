# Mentor Pi AI Development

## ROS机器人控制器文档

### ros_robot_controller_msgs
ROS2消息定义包，包含机器人控制所需的自定义消息类型和服务：

**消息类型 (.msg)**：
- `MotorState` - 电机状态（ID和转速RPS）
- `BuzzerState` - 蜂鸣器控制（频率、开关时间、重复次数）
- `LedState` - LED控制
- `ButtonState` - 按键状态
- `BusServoState`/`SetBusServoState` - 总线舵机状态和控制
- `PWMServoState`/`SetPWMServoState` - PWM舵机状态和控制
- `Sbus` - 航模遥控信号

**服务类型 (.srv)**：
- `GetBusServoState` - 获取总线舵机状态
- `GetPWMServoState` - 获取PWM舵机状态

### ros_robot_controller
ROS2机器人控制器主包，提供与STM32硬件板通信的完整功能：

**核心功能**：
- 硬件接口：与STM32控制板进行串口通信
- 传感器数据发布：IMU、按键、电池电压、手柄、SBUS遥控
- 执行器控制：LED、蜂鸣器、电机、PWM舵机、总线舵机
- 实时处理：100Hz频率发布传感器数据

**主要文件**：
- `ros_robot_controller_node.py` - ROS2节点主程序，处理所有话题订阅/发布和服务
- `ros_robot_controller_sdk.py` - 硬件通信SDK，实现串口协议和设备控制API

该项目为基于STM32的机器人控制系统提供了完整的ROS2接口，支持多种传感器和执行器的统一控制。