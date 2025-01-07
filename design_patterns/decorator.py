class Base:
    def execute(self) -> str:
        pass


class Core(Base):
    def execute(self) -> str:
        return "Core"


class Decorator(Base):
    _base: Base = None

    def __init__(self, base: Base) -> None:
        self._base = base

    @property
    def base(self) -> Base:
        return self._base

    def execute(self) -> str:
        return self._base.execute()


class DecoratorA(Decorator):
    def execute(self) -> str:
        return f"DecoratorA({self.base.execute()})"


class DecoratorB(Decorator):
    def execute(self) -> str:
        return f"DecoratorB({self.base.execute()})"


def run(base: Base) -> None:
    print(f"RESULT: {base.execute()}", end="")


if __name__ == "__main__":
    basic = Core()
    run(basic)
    decorator_A = DecoratorA(basic)
    decorator_B = DecoratorB(decorator_A)
    print("Client: Now I've got a wrapped component:")
    run(decorator_B)
