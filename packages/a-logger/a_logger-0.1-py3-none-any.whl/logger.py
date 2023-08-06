from colorama import init, Fore

init()

class Logger:
    """A class for logging messages to the console."""
    def __init__(self) -> None:
        """Initializes the Logger class."""
        pass


    def Custom(self, symbol: str, message: str) -> None:
        """Prints a custom logging message with a custom symbol.

        Args:
            message (str, required): The message to print.
            symbol (str, optional): The symbol to print. Defaults to None.
        """
        print(Fore.CYAN + "[ " + Fore.WHITE + symbol + Fore.CYAN + " ] " + Fore.WHITE + message)


    def Info(self, message) -> None:
        """Prints a info logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.BLUE + "[ " + Fore.WHITE + "&" + Fore.BLUE + " ] " + Fore.WHITE + message)


    def Success(self, message) -> None:
        """Prints a success logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.GREEN + "[ " + Fore.WHITE + "$" + Fore.GREEN + " ] " + Fore.WHITE + message)


    def Warning(self, message) -> None:
        """Prints a warn logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.YELLOW + "[ " + Fore.WHITE + "*" + Fore.YELLOW + " ] " + Fore.WHITE + message)


    def Error(self, message) -> None:
        """Prints a error logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.RED + "[ " + Fore.WHITE + "!" + Fore.RED + " ] " + Fore.WHITE + message)


    def Debug(self, message) -> None:
        """Prints a debug logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.MAGENTA + "[ " + Fore.WHITE + "^" + Fore.MAGENTA + " ] " + Fore.WHITE + message)


    def Input(self, message) -> None:
        """Prints a input logging message.

        Args:
            message (str, required): The message to print.
        """
        print(Fore.WHITE + "[ " + Fore.WHITE + ">" + Fore.WHITE + " ] " + Fore.WHITE + message, end=": ")
        return input("")