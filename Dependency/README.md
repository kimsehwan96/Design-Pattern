# 의존성과 관련된 패턴

## 의존성이란 무엇인가요?

```python3
class Repo:
    def get(self):
        return session.query(User).get(1)

class Usecase:
    def __init__(self):
        self.repo = Repo()
```

- 위 코드를 보면 `Usecase` 라는 클래스에서 Repo 클래스의 객체를 찍어내서 사용한다.
- 이런 것을 대상으로 Repo와 Usecase는 서로 의존성이 있다고 하며 `강한 결합` 상태라고 이야기 할 수 있다.
- Repo의 코드나 동작이 변경되면, 꼼짝없이 Usecase 또한 변경해야 하므로 매우 리팩토링하기 힘들고 거지같은 상황이 아닐 수 없다.

- 모든 객체 사이에는 느슨한 결합이 이루어 져야 한다.
    - 느슨한 결합이란 서로 상호작용 하지만, 서로의 세부 내용에 대해서 알 지 못해도 정상적으로 동작하는 관계를 의미한다.

## 의존성 주입!

```python3
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

```

- 객체 지향을 잘 알진 못하더라도 항상 고민하던 부분이 이 부분인 것 같다.
- 어떻게 해야 객체 간 상호작용은 원활하게 하는데, 서로 강한 결합을 하지 않아 리팩토링시 서로 영향을 주지 않을까?
- 나에게 주어진 숙제는 강한결합과 느슨한 결합의 차이, 및 실전 예제.
- 의존성을 어떻게 풀어나가야 하는지 이 컨셉에 대해서 많이 공부를 해야겠다.