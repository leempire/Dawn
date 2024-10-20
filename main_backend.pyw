import os
import time
import threading
from sys import exit
from src.record import Robot
from src.scanFiles import scanFiles, getCurDirectory


class Dawn(Robot):
    timeout = 5  # 捕获最长持续时间

    def __init__(self, *args, filepath='files', **kwargs):
        self.filepath = os.path.join(getCurDirectory(), filepath)
        self.files = scanFiles(filepath)
        self.catching = 0
        self.buffer = ''
        super().__init__(*args, **kwargs)

    def response_key(self, event, key, state):
        # 超过5秒 / 结束捕获 清空缓冲区 结束捕获
        if time.time() - self.catching > self.timeout:
            self.buffer = ''
            self.catching = False
        if state == 'down':  # 按下按键
            if key == 'esc':  # ctrl + esc 退出
                if 'ctrl' in self.get_pressed():
                    exit()
            if self.catching:  # 正在捕获
                if len(key) == 1:  # 单个字符
                    self.buffer += key
                elif key == 'space':  # 结束捕获
                    threading.Thread(target=self.open, args=(self.buffer,), daemon=True).start()
                    self.catching = 0
            else:  # 未开始捕获
                if key == '`':
                    # 开始捕获
                    self.buffer = ''
                    self.catching = time.time()

    def open(self, order):
        if order in self.files:
            os.startfile(self.files[order])
        elif order == 'set':
            os.startfile(self.filepath)


if __name__ == '__main__':
    Dawn().run()
