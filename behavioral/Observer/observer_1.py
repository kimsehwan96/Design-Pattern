class Observer:
    def __init__(self):
        self.subscriber = []
        self.msg = ""

    def notify(self):
        for sub in self.subscriber:
            sub.msg = self.msg

    # 등록된 옵저버들에 노티를 할 메서드, 순회하면서 노티 메시지를 전송한다,

    def register(self, observer):
        self.subscriber.append(observer)

    # 옵저버를 등록하는 메서드

    def unregister(self, observer):
        self.subscriber.remove(observer)

    # 옵저버를 삭제하는 메서드


class Subscriber:
    """
    옵저버에 추가되어서 옵저버에 종속적인 객체를 찍어낼 클래스.
    """

    def __init__(self):
        msg = ""

    def update(self):
        print(self.msg)


class Subject:
    def __init__(self):
        self.observer = []

    def notify_observer(self, info):
        for obs in self.observer:
            obs.msg = info

    def attach(self, observer):
        self.observer.append(observer)

    def detach(self, observer):
        self.observer.remove(observer)


if __name__ == "__main__":
    sub1 = Subscriber()
    sub2 = Subscriber()
    sub3 = Subscriber()

    ob = Observer()
    ob.register(sub1)
    ob.register(sub2)
    ob.register(sub3)

    sub = Subject()

    sub.attach(ob)

    sub.notify_observer("noti msg 1")
    ob.notify()

    sub1.update()
    sub2.update()
    sub3.update()
