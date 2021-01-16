# 추상 팩토리
- factory method pattern 의 일반화 버전
- 객체 생성을 group화 시켜서 한다.
- 객체 생성 용이의 장점, 메모리 사용성 향상, 퍼포먼스 향상에 대한 장점이 있다.

```python3
# FrogWorld 클래스는 추상 팩토리 
# WizardWorld 클래스 또한 추상 팩토리
# GameEnvironment 클래스는 게임의 엔트리포인트. 

class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounter {obstacle} and {act} !'
        print(msg)
    
class Bug:
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eats it'

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()

# 위자드 게임

class Wizard:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act} !'
        print(msg)

class Ork:
    def __str__(self):
        return 'an evil ork'
    
    def action(self):
        return 'kills it'

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

# 게임의 환경. 엔트리포인트 시작
# 
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle) 
    
def validate_age(name):
    age = input(f'Welcome {name}. How old are you ?')
    age = int(age)
    if age < 0:
        print(f'Age {age} is invalid, plz try again...')
        return (False, age)
    return (True, age)
    
def main():
    name = input("Hello. What's your name ?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
```

- 추상팩토리.