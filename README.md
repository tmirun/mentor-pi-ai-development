# Mentor Pi AI Development

## 开发方式

从 mini-ai 通过 `ssh pro-ai.home` 登录，在 pro-ai 的 `~/projects/me/mentor-pi-ai-development` 中修改和测试。提交并推送后，再回到 mini-ai 拉取同一分支。详见 [开发约定](AGENTS.md)。

## 麦克纳姆轮版 3D 模型

[`models/mecanum/`](models/mecanum/) 包含底盘（`base_link.STL`）、相机（`cam_Link.STL`）、雷达（`lidar_Link.STL`）和四个车轮（`wheel_*_Link.STL`）。每个文件是一个独立零件；整车装配位置见上游的 [`mecanum.xacro`](https://github.com/Hiwonder/MentorPi-ROS/blob/fb6d9969e935eb0e31966185158e33347951e761/simulations/mentorpi_description/urdf/mecanum.xacro)。

模型来源：[Hiwonder/MentorPi-ROS，版本 `fb6d9969`](https://github.com/Hiwonder/MentorPi-ROS/tree/fb6d9969e935eb0e31966185158e33347951e761/simulations/mentorpi_description/meshes/mecanum)。

## 原始资料目录

产品原始资料位于 `original docs/MentorPi智能视觉小车（2025版）/`，包含以下内容：

### 1 教程资料

| 编号 | 课程 | 说明 |
|------|------|------|
| 1 | MentorPi使用入门 | 认识MentorPi、开机准备、首次开机检验、手机APP遥控、无线手柄遥控 |
| 2 | Linux系统简介及使用入门 | Linux基础课程 |
| 3 | Python基础及入门实战 | Python编程语言 |
| 4 | OpenCV计算机视觉学习 | OpenCV计算机视觉 |
| 5 | ROS2开发入门 | ROS2基础课程 |
| 6 | 树莓派5主板及扩展板课程 | 树莓派5硬件 |
| 7 | Docker容器基础课程 | Docker容器基础 |
| 8 | 远程工具安装及容器进入方法 | 远程桌面工具安装与连接 |
| 9 | 运动控制课程 | 麦克纳姆轮/阿克曼底盘运动分析、IMU校准、速度控制 |
| 10 | 激光雷达课程 | 雷达介绍、测距原理、避障、跟随、警卫 |
| 11 | 深度相机基础课程 | Linux ROS深度相机 |
| 12 | 建图教程 | slam_toolbox建图、RTAB-VSLAM三维建图、远程文件传输 |
| 13 | 导航教程 | 自主导航 |
| 14 | ROS+OpenCV课程 | 颜色阈值调节、颜色识别、二维码识别、自主巡线、色块追踪、底盘跟踪 |
| 15 | MediaPipe人机交互 | 指尖轨迹识别、手部跟随、肢体体感控制、人体姿态检测 |
| 16 | 机器学习课程 | 机器学习 |
| 17 | 无人驾驶课程 | 地图铺设及道具安装 |
| 18 | 群控课程 | 多机器人群控 |
| 19 | 机器人网络配置课程 | 网络配置 |
| 20 | AI大模型课程 | 语音模块介绍与安装、AI大模型通用课程、多模态大模型、具身智能应用 |

### 2 软件工具

- 手机APP安装包
- 远程连接工具（PuTTY SSH、VNC可视化桌面）
- SD卡初始化工具
- 镜像烧录工具
- 文件传输工具
- 虚拟机安装包

### 3 源码资料

- STM32源码（`RosRobotControllerLite_ros_250811`）

### 4 硬件资料

- RRC Lite控制器
- 树莓派5主板资料
- AI大模型资料
- 深度相机资料（安思疆深度相机）
- 单目相机资料
- 编码电机资料（编码器直流减速电机310）
- 舵机资料（LFD-01舵机、HTS-25L串行总线智能舵机、LD-1501MG数字舵机）

### 5 系统镜像

- `MentorPi_MA_20250716` 系统镜像

### 6 虚拟主机

- ROS2虚拟机
- 官方虚拟机镜像
- 已配置好ROS环境的虚拟机镜像（建图导航用 / ROS附件配置完成版）

### 7 拓展资料

- ROS资料（优先看）
- Linux 树莓派学习资料
- 图像处理
- 机器学习
- 编程C++资料
- 编程Python资料

### 8 常见问题解答

- 树莓派5红灯常亮无法开机解决方法

---

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

## RRC开发板功能清单

### 基础控制功能
- **LED灯控制** - 可控制LED亮灭时间、循环次数
- **蜂鸣器控制** - 可设置频率、响声时间和循环次数

### 电机控制
- **编码器电机控制**
  - 单个电机运动控制（支持正负转速）
  - 多个电机同时运动控制
  - 单个或多个电机停止控制
  - 电机掩码停止控制

### 舵机控制
- **PWM舵机控制**
  - 多个PWM舵机同时控制（角度范围0°-180°）
  - 单个PWM舵机精确控制
  - PWM舵机位置读取
  - PWM舵机偏差设置和读取

- **总线舵机控制**
  - 总线舵机转动控制
  - 位置、电压、温度数据读取
  - 舵机上电/掉电控制
  - ID号读取和写入
  - 偏差调整和保存
  - 位置限制设置（低限位/高限位）
  - 电压限制设置
  - 温度限制设置

### 传感器数据采集
- **按键输入** - 支持按下、长按、点击、双击事件检测
- **IMU数据** - 加速度计和陀螺仪6轴数据（accel_x/y/z, gyro_x/y/z）
- **手柄数据** - 按键状态、摇杆值读取
- **SBUS航模遥控** - 16通道遥控信号接收

### 通信协议
- **串口通信** - 通过UART3口进行数据传输（波特率1000000）
- **CRC校验** - 确保数据传输可靠性
- **双向通信** - 支持上位机主动发送指令和控制板主动上传数据

### 数据格式支持
- 支持uint8_t、uint16_t、int8_t、int16_t、float等多种数据类型
- 小端模式数据传输
- 十六进制指令格式