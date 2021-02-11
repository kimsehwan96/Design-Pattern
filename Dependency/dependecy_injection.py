import abc
import inspect
from functools import wraps

class Repo:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass

class MySQLRepo(Repo):
    def get(self):
        print('Mysql repo')

providers = {
    Repo: MySQLRepo
}

def inject(func): #inject 데코레이터 . insepct의 getfullargspec 메서드를 활용하면 주어진 객체의 인자에 관한 정보 추출 가능.
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations

        for k, v in annotations.items(): # 객체의 모든 annotaion 을 추출한다.
            if v in providers: # 추출한 annotaion 중 규칙에 맞는 annotation이 있으면 인자에 주입시킬 객체를 너어준다,
                kwargs[k] = providers[v]()
        return func(*args, **kwargs) #실제 함수를 실행하고, 데코레이터를 종료한다.
        
    return wrapper

class Usecase:
    @inject
    def __init__(self, repo: Repo) -> None:
        self.repo = repo

# ABC를 활용하여 인터페이스 클래스인 Repo를 만들었다.

if __name__ == "__main__":
    usecase = Usecase()
    usecase.repo.get()