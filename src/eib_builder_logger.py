from __future__ import annotations




class EibBuilderLogger:
    def __init__(self):
        pass

    def log(self, message: str) -> None:
        """
        Logs a single message.
        """
        self.__print_log(message)

    def log_messages(self, messages: list[str]) -> None:
        """
        Logs multiple messages.
        """
        for message in messages:
            self.log(message)

    def log_error(self, error_message: str) -> None:
        """
        Logs an error message.
        """
        self.__print_log(f"Error: {error_message}")

    def log_warning(self, warning_message: str) -> None:
        """
        Logs a warning message.
        """
        self.__print_log(f"Warning: {warning_message}")

    def log_info(self, info_message: str) -> None:
        """
        Logs an informational message.
        """
        self.__print_log(f"Info: {info_message}")

    def __print_log(self, message: str) -> None:
        """
        Private method to print the log message.
        """
        print(message)
