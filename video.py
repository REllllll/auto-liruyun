class Video:

    def __init__(self, title: str, mark: bool):
        self._title = title  # 视频标题
        self._mark = mark  # 视频完成情况标记，False表未完成；True表完成
        self._voice = True  # 视频静音情况标记，默认为True表示不静音
        self._speed = 1.0  # 视频播放速度，默认为1.0表1倍速
        self._play = False  # 视频播放状态，默认为False表暂停
        self._parent = None  # 用于指向Video节点的父节点


    def set_parent(self, parent):
        self._parent = parent

    def gain_mark(self) -> bool:
        """
        获取当前视频完成的情况
        """
        pass

    def set_speed(self, speed: float) -> float:
        """
        修改播放的速度
        """
        self._speed = speed
        return self._speed

    def set_voice(self, voice: bool) -> bool:
        """
        修改音量状态，是否静音
        """
        self._voice = voice
        return self._voice

    def change_play(self) -> bool:
        """
        单击播放键
        """
        self._play = not (self._play)
        return self._play

    def check_play(self):
        """
        判断是否播放完成
        """
        return True
