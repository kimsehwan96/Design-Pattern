# 다른 객체를 직접 만들어 넘겨주는 객체를 따로 만드는 방법

from collections import deque

class Unit:
    def __init__(self):
        pass

    def spwan(self):
        pass

    def delete(self):
        pass

class Marine(Unit):
    def __init__(self):
        pass


class Firebat(Unit):
    def __init__(self):
        pass

class UnitFactory: #유닛을 분류하는 단일 책임을 지는 팩토리 클래스
    def create(self, unit_name):
        if unit_name == "Marine":
            return Marine()
        elif unit_name == "FireBat":
            return Firebat()
## 유닛 인스턴스를 생성하는 팩토리

class Map: #이 맵은 이렇게 되면 유닛을 생성한다는 책임 외에 유닛을 분류한다는 팩토리 클래스에서 갖고있는 이런 책임을 안가지니까, 단일책임원칙을 잘 지킨다.
    def __init__(self, map_file:deque):
        while map_file:
            unit = UnitFactory.create(map_file.popleft())
    
    #이후 기타 코드들
