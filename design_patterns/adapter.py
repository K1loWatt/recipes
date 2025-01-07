class Standard:
    def operation(self) -> str:
        return "Standard: The default standard's behavior."


class Special:
    def special_operation(self) -> str:
        return "special message"


class Translator(Standard, Special):
    def operation(self) -> str:
        return f"Translated message {self.special_operation()[::-1]}"


def execute_operation(standard: "Standard") -> None:
    """
    The execute_operation function supports all classes
    that follow the Standard interface.
    """

    print(standard.operation(), end="")


if __name__ == "__main__":
    standard = Standard()
    execute_operation(standard)

    translator = Translator()
    execute_operation(translator)
