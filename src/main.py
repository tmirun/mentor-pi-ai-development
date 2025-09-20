#!/usr/bin/env python3
import time

from ros_robot_controller import Board

def main():
    print("启动电机前进后退测试...")

    # 初始化控制板
    try:
        board = Board(device="/dev/ttyACM0", baudrate=1000000, timeout=5)
        print("控制板初始化成功")
    except Exception as e:
        print(f"控制板初始化失败: {e}")
        return

    try:
        # 前进5秒 - 设置所有电机以1.0转速前进
        print("电机前进5秒...")
        board.set_motor_speed([[1, 1.0], [2, 1.0], [3, 1.0], [4, 1.0]])
        time.sleep(5)

        # 停止1秒
        print("停止1秒...")
        board.set_motor_speed([[1, 0], [2, 0], [3, 0], [4, 0]])
        time.sleep(1)

        # 后退5秒 - 设置所有电机以-1.0转速后退
        print("电机后退5秒...")
        board.set_motor_speed([[1, -1.0], [2, -1.0], [3, -1.0], [4, -1.0]])
        time.sleep(5)

        # 停止
        print("停止电机")
        board.set_motor_speed([[1, 0], [2, 0], [3, 0], [4, 0]])

        print("测试完成！")

    except Exception as e:
        print(f"电机控制出错: {e}")
        # 确保电机停止
        try:
            board.set_motor_speed([[1, 0], [2, 0], [3, 0], [4, 0]])
        except:
            pass

if __name__ == "__main__":
    main()
