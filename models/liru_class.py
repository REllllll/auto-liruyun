from selenium.webdriver.remote.webelement import WebElement


class liru_class:

    def __init__(self, class_element: WebElement) -> None:
        self.class_element = class_element
        self.name = self.class_element.text

    def click(self):
        self.class_element.click()
