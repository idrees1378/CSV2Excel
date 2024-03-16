from __future__ import annotations


class EibBuilderLogger:
    def __init__(self):
        pass

    def __print_log(self, message: str):
        print(message)

    def log(self, message: str):
        self.__print_log(message)

    def log_messages(self, messages: list[str]):
        for message in messages:
            self.log(message)
