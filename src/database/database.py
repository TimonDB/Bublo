from abc import abstractmethod, ABC
from typing import Optional

from src.database.tables import Person


class Database(ABC):

    @abstractmethod
    def get_person(self, id) -> Optional[Person]:
        pass

    @abstractmethod
    def insert_or_update(self, id):
        pass
