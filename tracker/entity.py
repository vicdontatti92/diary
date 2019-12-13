from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Task:
    name: str
    description: str
    complete: bool = False
    id: Optional[int] = None

    def __post_init__(self) -> None:
        self.validate_name()
        self.validate_discription()

    def validate_name(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError('name should be string')

        if len(self.name) > 30:  # noqa: WPS432
            raise ValueError('name length should be less than 31')

    def validate_discription(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError('name should be string')

        if len(self.name) > 1400:  # noqa:WPS432
            raise ValueError('discription length should be less than 1401',)

    def validate_id(self) -> None:
        if not isinstance(self.id, int):
            raise TypeError('id should be integer')


# todo:
# написать постинит
