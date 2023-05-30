class Unit:

    def __init__(self, title: str, video_list):
        self._title = title  # 课程标题
        self._index = 0  # 用于当前遍历video_list的索引
        self._video_list = video_list  # 本单元的所有视频所组成的列表
        self._parent = None  # 用于指向Unit节点的父节点

    def set_parent(self, parent):
        self._parent = parent

    def __iter__(self):
        return self  # 设置为可迭代对象，迭代其子节点

    def __next__(self):
        if self._index >= len(self._video_list):
            raise StopIteration
        else:
            result = self._video_list[self._index]  # 返回当前遍历的元素
            self._index += 1  # 索引指向下一个元素
            return result
