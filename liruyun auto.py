import pyautogui
from PIL import ImageGrab,ImageColor,Image
import abc

class Unit():

    def __init__(self,position,type) -> None:
        self.position = position
        self.type = type
        pass
    
    def click(self):
        pyautogui.click(self.position)
        pass

    def move(self):
        pyautogui.moveTo(self.position)
        pass



def get_unit(screen : Image.Image):
    unit_list = []
    location_list = pyautogui.locateAll('liru class video button.jpg',screen,confidence=0.9)
    for location in location_list:
        unit_list.append(Unit(location,'unit'))
    return unit_list

def play_video():
    pyautogui.sleep(3)
    #move to the position of the scroll bar
    pyautogui.moveTo(pyautogui.locateOnScreen('position_scroll.jpg'))
    #scroll to the bottom
    pyautogui.scroll(-1000)
    pyautogui.click(pyautogui.locateOnScreen('play button.jpg'))
    pass

def wait_for_video():
    while True:
        pyautogui.sleep(1)
        position = pyautogui.locateOnScreen('play button.jpg')
        if position == None:
            continue
        else:
            pyautogui.sleep(1)
            break
    pass


def main():
    screen = ImageGrab.grab()
    unit_list = get_unit(screen)
    for unit in unit_list:
        unit.click()
        play_video()
        wait_for_video()
    unit.move()
    pyautogui.scroll(-1000)
    screen = ImageGrab.grab()
    unit_list = get_unit(screen)
    for unit in unit_list:
        pyautogui.scroll(-1000)
        unit.click()
        play_video()
        wait_for_video()
        unit.move()
    pass

if __name__ == '__main__':
    main()
    