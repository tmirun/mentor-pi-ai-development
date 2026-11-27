import atexit
from pathlib import Path
import time

import mujoco.viewer
from mujoco.studio import launch_passive, viewer_protocol


class BrowserWindow:
    """代替弹出的窗口：把画面送到浏览器里。整个笔记本只开一个，一直留着。"""

    def __init__(self, port=8090):
        self.port = port
        self.viewer = None

    def __call__(self, model, data, key_callback=None):
        if self.viewer is None or not self.viewer.is_running():
            config = viewer_protocol.ViewerConfig(gfx="web", http_port=self.port)
            self.viewer = launch_passive.launch(config)
        self.viewer.set_model(model, data=data)        # 告诉网页：现在要看的是这一份 model 和 data
        return self

    def __enter__(self):
        return self

    def __exit__(self, *error):
        return False                                   # 不关掉，下一个单元格接着用

    def is_running(self):
        return self.viewer is not None and self.viewer.is_running()

    def sync(self):
        self.viewer.sync()

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None


browser_window = BrowserWindow()
mujoco.viewer.launch_passive = browser_window          # 之后所有「打开窗口」的单元格，都改成送到浏览器
atexit.register(browser_window.close)


def main():
    model_path = Path(__file__).resolve().with_name("mentorpi.xml")
    model = mujoco.MjModel.from_xml_path(str(model_path))
    data = mujoco.MjData(model)

    try:
        with mujoco.viewer.launch_passive(model, data) as viewer:
            print(f"已加载模型：{model_path}", flush=True)
            print(f"浏览器地址：http://localhost:{viewer.port}（按 Ctrl+C 停止）", flush=True)
            while viewer.is_running():
                step_start = time.perf_counter()
                mujoco.mj_step(model, data)
                viewer.sync()
                # 按模型时间步运行，避免仿真全速占用 CPU。
                remaining = model.opt.timestep - (time.perf_counter() - step_start)
                if remaining > 0:
                    time.sleep(remaining)
    except KeyboardInterrupt:
        print("\n仿真已停止。")
    finally:
        browser_window.close()


if __name__ == "__main__":
    main()
