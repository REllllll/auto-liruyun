from liru_class import LiRuClass
from unit import Unit
from video import Video

def test():
    video1 = Video("无穷级数-1", False)
    video2 = Video("无穷级数-2", False)
    video3 = Video("多元微分-1", False)
    video4 = Video("多元微分-2", False)
    unit1 = Unit("无穷级数", [video1, video2])
    unit2 = Unit("多元微分", [video3, video4])
    class1 = LiRuClass("高等数学",[unit1, unit2])
    unit1.set_parent(class1)
    unit2.set_parent(class1)
    video1.set_parent(unit1)
    video2.set_parent(unit1)
    video3.set_parent(unit2)
    video4.set_parent(unit2)
    for unit in class1:
        for video in unit:
            if video.check_play():
                print("播放完成")

if __name__ == "__main__":
    test()