from selenium import webdriver
from selenium.webdriver.common.by import By


class LiRuClass:

    def __init__(self):
        self._driver = webdriver.Chrome()  # 该属性存储一个网站
        self._title = None  # 课程标题
        self._index = 0  # 用于当前遍历unit_list的索引
        self._unit_list = None  # 本课程的所有单元所组成的列表
        self._parent = None  # 根节点没有父节点

    def __iter__(self):
        return self  # 设置为可迭代对象，迭代其子节点

    def __next__(self):
        if self._index >= len(self._unit_list):
            raise StopIteration
        else:
            result = self._unit_list[self._index]  # 返回当前遍历的元素
            self._index += 1  # 索引指向下一个元素
            return result
