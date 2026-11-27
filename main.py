import atexit

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
        return self.viewer.is_running()

    def sync(self):
        self.viewer.sync()

browser_window = BrowserWindow()
mujoco.viewer.launch_passive = browser_window          # 之后所有「打开窗口」的单元格，都改成送到浏览器
atexit.register(lambda: browser_window.viewer is not None and browser_window.viewer.close())   # 关掉笔记本时，顺手把查看器关好
