from abc import ABC, abstractmethod
from typing import TypeVar, Generic


Command = TypeVar('Command')  # Comando
Result = TypeVar('Result')  # Resultado de comando

class CommandWithResultHandler(ABC, Generic[Command, Result]):
    @abstractmethod
    def handle(self, cmd: Command) -> Result:
        """Maneja un comando y devuelve un resultado."""
        pass


