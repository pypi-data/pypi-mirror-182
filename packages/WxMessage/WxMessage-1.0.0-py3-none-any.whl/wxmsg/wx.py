import time
import pyautogui as pg
import pyperclip as pc


class WxMsg:
    def __init__(self, speed=1):
        # 操作间隔为1秒
        self._sped = speed
        pg.PAUSE = speed
        print('微信公众号：Python编程站\n获取更多技术文章\n可加入技术交流群\n探讨技术')

    def send(self, name, msg):
        # 打开微信
        pg.hotkey('ctrl', 'alt', 'w')
        time.sleep(self._sped)
        pg.hotkey('ctrl', 'f')

        # 找到消息发送对象
        pc.copy(name)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 发送消息
        pc.copy(msg)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 隐藏微信
        pg.hotkey('ctrl', 'alt', 'w')
